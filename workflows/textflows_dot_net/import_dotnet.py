import logging
import os
import sys
import traceback
from settings import PACKAGE_ROOT

#------------------------------------------------------------------------------
# prepare environment for loading .net components (Python.net interpreter should be used)
# see: http://pythonnet.sourceforge.net/
#------------------------------------------------------------------------------

logging.info("----------------- import_dotnet.py ------------------------>")

if sys.platform.startswith('win'):
    dllPath = os.path.join(PACKAGE_ROOT, 'bin')
    sys.path.append(dllPath)


    try:
        import clr
        import System

        # load all dll & exe files in dllPath directory
        for f in os.listdir(dllPath):
            if os.path.isfile(os.path.join(dllPath, f)) and (f.endswith(".dll") or f.endswith(".exe")):
                logging.info("Loading .NET library '%s'", f)
                try:
                    System.Reflection.Assembly.LoadFile(os.path.join(dllPath, f).replace('\\','/'))
                except System.BadImageFormatException, e:
                    pass

        # loading LATINO namespace
        import Latino
        import LatinoInterfaces
        from LatinoInterfaces import LatinoCF

        # loading LEMMAGEN namespace
        import LemmaSharpInterfaces
        from LemmaSharpInterfaces import LemmaSharpIntf

        # loading CROSSBEE namespace
        import CrossBeeInterfaces
        from CrossBeeInterfaces import CrossBeeIntf

    except Exception:
        logging.warning("DotNet assemblies could not be loaded! Probable reasons: missing dlls or wrong interpreter (see http://pythonnet.sourceforge.net). "
                        "Other functionality of ClowdFlows (besides .Net assemblies) should be OK! "
                        "Original exception: %s" % traceback.format_exc())
        pass
else:
    logging.info("DotNet assemblies were not be loaded! Available only for Windows environments.")
logging.info("<----------------- import_dotnet.py ------------------------")