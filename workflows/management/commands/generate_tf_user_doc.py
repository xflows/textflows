__author__ = 'darkoa'

import io, os

from django.core.management.base import BaseCommand

from workflows.models import *


class Command(BaseCommand):
    """
    This command generates TextFlows user documentation. In particular it generates a ReStructuredText file which can be processed with Spyhx and transformed to HTML.
    The "Example usage" field should contain links to workflows on the production TextFlows server, so the script should be run there.
    """

    help = 'This command generates TextFlows documentation. In particular it generates a ReStructuredText file which can be processed with Spyhx and transformed to HTML.'
    f = None

    titleUnderlines = '=-~`+\''

    def handle(self, *args, **options):
        self.f = io.open("docs" + os.sep + "tf_user_doc.rst", "w", encoding='utf8')

        categories = Category.objects.all()

        for c0 in categories:
            if not c0.is_basic():
                self.print_categories(c0)

        self.f.close()

    def print_categories(self, c0):
        if not c0.parent:
            if not c0.user:
                print " "*2 + c0.name
                self.f.write( unicode( self.print_section_title('Category ' + c0.name, self.titleUnderlines[0]) ) )

                for c1 in c0.children.all():
                    print " "*4 + c1.name
                    self.f.write( unicode( self.print_section_title('Category ' + c1.name, self.titleUnderlines[1]) ) )

                    for c2 in c1.children.all():
                        print " "*6 + c2.name
                        self.f.write( unicode( self.print_section_title('Category ' + c2.name, self.titleUnderlines[2]) ) )

                        for w in c2.widgets.all():
                            print " "*8 + " <W> " + w.name
                            self.print_widget(  self.create_widget_dict(w), self.titleUnderlines[3])

                    for w in c1.widgets.all():
                        print " "*6 + " [W] " + w.name
                        self.print_widget(  self.create_widget_dict(w), self.titleUnderlines[2])

                for w in c0.widgets.all():
                    print " "*4 + " [W] " + w.name
                    self.print_widget(  self.create_widget_dict(w), self.titleUnderlines[1])

    def print_section_title(self, my_title, underline_char):
        my_text = my_title + "\n"
        l = len(my_title)
        my_text += (underline_char * l) + "\n"
        return my_text

    def clean_description(self, text_value):
        res = text_value
        res = res.replace("\r\n", "\n")

        res = res.replace("\n", "\n  ")

        return res

    def get_widget_public_workflows(self, widget):
        """ Gets a list of public workflows where an abstract widget has been used.

        :param widget:
        :return: list
        """

        aw = widget

        res_wf = []
        all_widgets = aw.instances.all()
        for w in all_widgets:
            if w.workflow.public:
                res_wf.append( w.workflow )

        return res_wf


    def get_widget_io(self, widget):
        """Get inputs, parameters and outputs for one widget

        :param widget:
        :return: a tuple ( list of inputs, list of parameters, list of outputs )
        """

        inp, params, out = ([], [], [])

        # Get all inputs and parameters for widget
        inp_list = widget.inputs.all()
        for myinp in inp_list:
            s = {}
            s['text'] = "%s (%s)" % ( myinp.name, self.clean_description(myinp.description) )
            if len( myinp.description.strip() )==0 or myinp.name==myinp.description:
                s['text'] = myinp.name

            arr_opt = myinp.options.all()
            if len(arr_opt) > 0:
                s["possible_values"] = [opt.name for opt in arr_opt]

            if len(myinp.default) > 0:
                s["default_value"] = myinp.default

            if myinp.parameter==False:
                inp.append( s )
            else:
                params.append( s )

        # Get all outputs for widget
        inp_list = widget.outputs.all()
        for myout in inp_list:
            s = {}
            s['text'] = "%s (%s)" % (myout.name, self.clean_description(myout.description) )
            if len(myout.description.strip()) == 0 or myout.name == myout.description:
                s['text'] = myout.name

            out.append( s )

        return (inp, params, out)


    def create_widget_dict(self, my_widget):

        name = my_widget.name
        act  = my_widget.action
        desc = my_widget.description.strip()

        img  = my_widget.static_image.strip()

        package_name = my_widget.package
        full_img_path = "workflows" + os.sep + package_name + os.sep + "static" + os.sep + package_name + os.sep + "icons" + os.sep + "widget" + os.sep

        try:
            if len(img)>0 and not( os.path.isfile(full_img_path+img) ):
                print "Missing IMG: " + full_img_path + img

            if len(img) == 0 or not( os.path.isfile(full_img_path+img) ):
                # print "No IMG set for w: " + name
                full_img_path = 'workflows/static/widget-icons/question-mark.png'
                img = ""

            inp, params, out = self.get_widget_io(my_widget)

            vis = len( my_widget.visualization_view.strip() ) > 0

            res_dict = {'name': name, 'act':act, 'desc':desc, 'img':full_img_path + img, 'inp':inp, 'params':params, 'out':out,
            'interact':my_widget.interactive, 'vis':vis, 'publ_wf':""}

            publ_wf = self.get_widget_public_workflows(my_widget)
            if len(publ_wf)>0:
                res_dict["publ_wf"] = "http://textflows.ijs.si/workflow/%d/" % (publ_wf[0].id)

                res_dict["publ_wf_n"] = publ_wf[0].name

            return res_dict

        except Exception, e:
            print "-------Exception for widget: " + my_widget.name
            print str(e)

        return {}



    def print_widget(self, widget_dict, underline_char):
        base_dir = "../"

        self.f.write( self.print_section_title("\n" + 'Widget: ' + widget_dict["name"], underline_char) )

        self.f.write( unicode( ".. image:: " + base_dir + widget_dict['img'] + "\n") )
        self.f.write( unicode( "   :width: 50" + "\n" + "   :height: 50" + "\n") )

        if len( widget_dict['desc'] ) > 0:
            self.f.write( unicode(widget_dict['desc'] + "\n" + "\n" ) )
        else:
            print "      '%s'   <<---- missing doc." % (widget_dict["name"])

        for my_inp in widget_dict['inp']:
            self.f.write('* Input: ' + my_inp['text'] + "\n" )
            if my_inp.has_key("possible_values"):
                self.f.write(unicode("\n" + "  * Possible values: " + "\n\n" ))
                for val in my_inp["possible_values"]:
                    self.f.write('    * ' + val +  "\n" )

        for my_param in widget_dict['params']:
            self.f.write('* Parameter: ' + my_param['text'] + "\n" )
            if my_param.has_key("possible_values"):
                self.f.write(unicode("\n" + "  * Possible values: " + "\n\n" ))
                for val in my_param["possible_values"]:
                    self.f.write('    * ' + val +  "\n" )

            if my_param.has_key("default_value"):
                self.f.write(unicode("\n" + "  * Default value: " + my_param["default_value"] + "\n" ))


        for my_out in widget_dict['out']:
            self.f.write('* Output: ' + my_out['text'] + "\n" )

        if len( widget_dict['out'] ) == 0:
            if widget_dict['interact']==True:
                self.f.write(unicode('* Outputs: Interactive Popup window which shows widget\'s results and allows manipulation' + "\n" ))
            else:
                if widget_dict['vis']==True:
                    self.f.write(unicode('* Outputs: Popup window which shows widget\'s results' + "\n" ))
                else:
                    print " --- --- --- w: " + widget_dict["name"] + " GreskaNoOuputsNotInteractiveNotVis "

        if len(widget_dict['publ_wf']) > 0:
            # `Python <http://www.python.org/>`_
            self.f.write(unicode("* Example usage: `%s <%s>`_\n" % (widget_dict['publ_wf_n'], widget_dict['publ_wf']) ))


        self.f.write( unicode("\n") )

