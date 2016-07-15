
import re
import os.path
from docx import opendocx, getdocumenttext
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from subprocess import Popen, PIPE


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


def document_to_text(path):
    ext = os.path.splitext(path)[1]
    filename = os.path.basename(path)

    if ext == ".doc":
        cmd = os.path.dirname(os.path.realpath(__file__)) + os.sep + "antiword" + os.sep + "antiword.exe -m CP852 " + path
        pipe = Popen(cmd, stdout=PIPE, shell=True)
        text = pipe.communicate()[0]
        return filename, unicode(re.sub("\r|\n", "", text).strip())

    elif ext == ".docx":
        document = opendocx(path)
        paratextlist = getdocumenttext(document)
        newparatextlist = []
        for paratext in paratextlist:
            newparatextlist.append(paratext)
        return filename, "".join(newparatextlist)

    elif ext == ".pdf":
        text = convert_pdf_to_txt(path)
        return filename, unicode(re.sub("\r|\n", "", text).strip())

    else:
        text = unicode(open(path, "r").read(), errors='replace').strip()
        return filename, text

