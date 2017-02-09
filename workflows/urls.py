from django.conf.urls import include, url

import workflows.views as workflow_views

packageUrls = {}
from workflows import module_importer
def set_package_url(name, value, package):
    if name == 'urlpatterns':
        packageUrls[package] = value
module_importer.import_all_packages_libs("urls",set_package_url)

urlpatterns = []

for pck in  packageUrls:
    urlpatterns += [ url(r'^'+pck+'/', include(packageUrls[pck])), ]

urlpatterns += [
    url(r'^$', workflow_views.index, name='the index'),
    url(r'^new-workflow/$', workflow_views.new_workflow, name='new workflow'),
    url(r'^add-widget/$', workflow_views.add_widget, name='add widget'),
    url(r'^save-position/', workflow_views.save_position, name='save position'),
    url(r'^add-connection/', workflow_views.add_connection, name='add connection'),
    url(r'^delete-widget/', workflow_views.delete_widget, name='delete widget'),
    url(r'^delete-workflow/', workflow_views.delete_workflow, name='delete workflow'),
    url(r'^delete-connection/', workflow_views.delete_connection, name='delete connection'),
    url(r'^add-subprocess/', workflow_views.add_subprocess, name='add subprocess'),
    url(r'^get-subprocess/', workflow_views.get_subprocess, name='get subprocess'),
    url(r'^add-input/', workflow_views.add_input, name='add input'),
    url(r'^add-output/', workflow_views.add_output, name='add output'),
    url(r'^add-for/', workflow_views.add_for, name='add for'),
    url(r'^add-cv/', workflow_views.add_cv, name='add cv'),
    url(r'^synchronize-widgets/', workflow_views.synchronize_widgets, name='synchronize widgets'),
    url(r'^synchronize-connections/', workflow_views.synchronize_connections, name='synchronize connections'),
    url(r'^get-widget/', workflow_views.get_widget, name='get widget'),
    url(r'^get-parameters/', workflow_views.get_parameters, name='get parameters'),
    url(r'^save-parameter/', workflow_views.save_parameter, name='save parameter'),
    url(r'^get-configuration/', workflow_views.get_configuration, name='get configuration'),
    url(r'^save-configuration/', workflow_views.save_configuration, name='save configuration'),
    url(r'^get-rename/', workflow_views.get_rename_dialog, name='rename widget dialog'),
    url(r'^rename-widget/', workflow_views.rename_widget, name='rename widget'),
    url(r'^rename-workflow/', workflow_views.rename_workflow, name='rename workflow'),
    url(r'^run-widget/', workflow_views.run_widget, name='run widget'),
    url(r'^widget-results/', workflow_views.widget_results, name='widget results'),
    url(r'^widget-visualization/', workflow_views.visualize_widget, name='widget visualization'),
    url(r'^widget-iframe/(?P<widget_id>[0-9]+)/$', workflow_views.widget_iframe, name='widget iframe'),
    url(r'^get-unfinished/', workflow_views.get_unfinished, name='get unfinished'),
    url(r'^upload-handler/$', workflow_views.upload_handler, name='file upload'),
    url(r'^widget-interaction/', workflow_views.widget_interaction, name='widget interaction'),
    url(r'^finish-interaction/', workflow_views.finish_interaction, name='finish interaction'),
    url(r'^import-webservice/', workflow_views.import_webservice, name='import webservice'),

    url(r'^documentation/', workflow_views.documentation, name='documentation'),

    url(r'^get-designate-dialogs/', workflow_views.get_designate_dialogs, name='get designate dialogs'),

    url(r'^save-designation/', workflow_views.save_designation, name='save designation'),

    url(r'^get-category/', workflow_views.get_category, name='get category'),

    url(r'^widget-progress/', workflow_views.widget_progress, name='widget progress'),

    url(r'^copy-workflow/(?P<workflow_id>[0-9]+)/$', workflow_views.copy_workflow, name='copy workflow'),
    url(r'^copy-workflow-warn/(?P<workflow_id>[0-9]+)/$', workflow_views.copy_workflow_warn, name='copy workflow warn'),

    url(r'^workflow-url/', workflow_views.workflow_url, name='workflow url'),

    url(r'^unfinish-visualizations/', workflow_views.unfinish_visualizations, name='unfinish visualizations'),

    url(r'^(?P<workflow_id>[0-9]+)/$', workflow_views.open_workflow, name='open workflow'),

    url(r'^reset-widget/', workflow_views.reset_widget, name='reset widget'),
    url(r'^get-executed-status/', workflow_views.get_executed_status, name='get executed status'),
    url(r'^reset-workflow/', workflow_views.reset_workflow, name='reset workflow'),

    url(r'^export-package/(?P<packages>.+)/$', workflow_views.export_package, name='export_package'),

    url(r'^widget-inputs/(?P<widget_id>[0-9]+)/$', workflow_views.widget_inputs, name='widget inputs'),

    url(r'^workflow_results/(?P<workflow_id>[0-9]+)/$', workflow_views.workflow_results, name='workflow_results'),
]