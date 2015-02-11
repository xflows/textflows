from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.utils import puts, abort

env.use_ssh_config = True
apps_to_migrate = ('workflows',)

def live():
    """ doloci live server kot aktivni """
    env.os = 'debian'
    env.hosts = ['mperice@textflows.ijs.si']
    env.branch = 'dev'

def deploy():
    """ deploy na serverju
    uporaba:
    $ fab live deploy
    """
    with prefix('source /var/www/textflows/textflows_venv/bin/activate'):
        with cd('/var/www/textflows/textflows/mothra'):
            puts(yellow("[Pulling from origin, on branch %s]" % (env.branch,)))
            run('git pull origin %s' % (env.branch,))
            run('git checkout %s' % (env.branch,))

            puts(yellow("[Installing packages]"))

            run('pip install -qr requirements.txt')

            puts(yellow("[Migrating apps]"))
            for app in apps_to_migrate:
                puts("--> [Migrating %s]" % (app,))
                run('python manage.py migrate %s --no-initial-data' % (app, ))

            puts(yellow("[Collecting static files]"))
            run("python manage.py collectstatic --noinput")

            puts(yellow("[Auto importing packages]"))
            run("python manage.py import_all")

        #with cd('/srv/django-projects/supervisor'):
        #    puts(yellow("[Restarting the run streams daemon"))
        #    run('supervisorctl restart runstreams')

        with cd('/srv/django-projects/supervisor'):
            puts(yellow("[Restarting the gunicorn daemon"))
            run('supervisorctl restart mothra')

            #puts(yellow("[Compressing]"))
            #run('python manage.py compress')

def supervisorstat():
    "supervisor statistika na serverju"
    with prefix('/var/www/textflows/textflows_venv/bin/activate'):
        with cd('/srv/django-projects/supervisor'):
            run('tail /srv/django-logs/runstreams.stdout.log')
            run('supervisorctl status')


def apache_restart():
    """restarta apache service
    primer:
    $ fab dev apache_restart
    $ fab live apache_restart
    """
    if env.os == 'ubuntu':
        sudo('service apache2 restart')
    elif env.os =='debian':
        sudo('/etc/init.d/nginx restart')
    elif env.os == 'arch':
        sudo('rc.d restart httpd')
    else:
        abort('env.os ni definiran, kaj je zdej to')
