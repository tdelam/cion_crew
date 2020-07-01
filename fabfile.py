from __future__ import with_statement
from fabric.api import *

# Environment Variables
env.hosts = ['norontcrew.cionorth.ca']
env.user = "trevor"

# Project Variables
app_name = "cion_crew"
git_name = "cion_crew"

root_dir = '/srv/virtualenvs/%s' % app_name
code_dir = '%s/%s' % (root_dir, app_name)
git_url = 'git@bitbucket.org:50c/%s.git' % git_name

source_activate_str = 'source /srv/virtualenvs/%s/bin/activate' % app_name

# Important Notes
# This fab file is for Django 1.7+ (no syncdb or --fake on migrate as they are not needed anymore)

def mkvirtualenv():
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("mkvirtualenv %s" % app_name)


def deploy():
    with settings(warn_only=True):
        mkvirtualenv()
        if run("test -d %s" % code_dir).failed:
            run("git clone %s %s" % (git_url, code_dir))

    with cd(code_dir):
        run("git pull")
        with prefix(source_activate_str):
            run('pip install -r %s/requirements.txt' % code_dir)
            run('python manage.py migrate --fake')


def auto_deploy():
    # Change settings DEBUG value to False for deployment
    local("sed -i'.backup' -e's/DEBUG = True/DEBUG = False/' %s/settings.py" % app_name)
    local("git add %s/settings.py" % app_name)
    local("git commit -q -m 'debug=false for deployment.'")
    local("git push origin master")  # Possible method arguments here for origin and master

    with settings(warn_only=True):
        mkvirtualenv()
        if run("test -d %s" % code_dir).failed:
            run("git clone %s %s" % (git_url, code_dir))

    with cd(code_dir):
        run("git pull")
        with prefix(source_activate_str):
            run('pip install -r %s/requirements.txt' % code_dir)
            run('python manage.py migrate')

    # Change DEBUG back to True for development
    local("rm %s/settings.py" % app_name)
    local("mv %s/settings.py.backup %s/settings.py" % (app_name, app_name))
    local("git add %s/settings.py" % app_name)
    local("git commit -q -m 'debug=true for development.'")
    local("git push origin master")  # Possible method arguments here for origin and master


# General Admin functions

def create_database():
    run("createdb %s" % app_name)


def create_superuser():
    with cd(code_dir):
        with prefix(source_activate_str):
            run('python manage.py createsuperuser')


def migrate():
    with cd(code_dir):
        with prefix(source_activate_str):
            run('python manage.py migrate')


def makemigrations():
    with cd(code_dir):
        with prefix(source_activate_str):
            run('python manage.py makemigrations')


def fix_permissions():
    with cd(code_dir):
        with prefix(source_activate_str):
            sudo('chown www-data:www-data %s/media' % app_name)


def restart_apache():
    sudo('/etc/init.d/apache2 reload')


def reload():
    sudo('service apache2 reload', pty=False)


def restart():
    sudo('service apache2 restart', pty=False)
