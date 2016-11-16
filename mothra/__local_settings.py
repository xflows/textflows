# Local settings for mothra project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'mothra.db'), # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

USE_CONCURRENCY = False

FILES_FOLDER = os.path.join(PUBLIC_DIR, 'files/')

INSTALLED_APPS_WORKFLOWS_SUB = (
    'workflows.base',
    'workflows.latino',
    #'workflows.decision_support',
    #'workflows.segmine',
    #'workflows.subgroup_discovery',
    #'workflows.nlp',
    'workflows.lexicology',
    'workflows.nltoolkit',
    'workflows.scikit_classifiers',
    #'workflows.ilp',
    #'workflows.weka',
    #'workflows.cforange',
    #'workflows.perfeval',
    #'workflows.mysql',
    #'workflows.lemmagen',
    #'workflows.crossbee',
    #'workflows.scikit',
    #'workflows.streaming',
    #'workflows.bio3graph',
    #'workflows.noise',
    #'workflows.vipercharts',
    #'workflows.MUSE',
    #'workflows.MUSE_v3',
    #'workflows.hbp',
)

INSTALLED_APPS_EXTERNAL_PACKAGES = (
    # 'tf_core.nltoolkit',
    # 'tf_latino.latino',
    # 'tf_literature_based_discovery',
)

BROKER_URL = 'django://'
CELERY_ALWAYS_EAGER = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*f$)twxl*rdk*o@^j%^0f0r#z7=kkyw=-2v*rjdnon_j==1uw@'

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

USE_WINDOWS_QUEUE = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

#MEGAM executable path
MEGAM_EXECUTABLE_PATH = "C:\\work\\textflows-env\\MEGAM\\megam.exe"

#Paths to Stanford pos tagger model and jar
STANFORD_POS_TAGGER_MODEL = "C:\\work\\textflows-env\\english-bidirectional-distsim.tagger"
STANFORD_POS_TAGGER_JAR = "C:\\work\\textflows-env\\stanford-postagger.jar"

