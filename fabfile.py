from fabric.api import *
from fabric.utils import abort
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists

if not env.hosts:
    env.hosts = ['www-data@igor.io']

project_name = 'stackphp.com'
target_dir = '/var/www/'+project_name
backup_dir = target_dir+'-backup'
staging_dir = target_dir+'-staging'

@task(default=True)
def deploy():
    puts('> Cleaning up previous backup and staging dir')
    run('rm -rf %s %s' % (backup_dir, staging_dir))

    puts('> Preparing staging')
    run('cp -r %s %s' % (target_dir, staging_dir))

    puts('> Uploading changes')
    with cd(staging_dir):
        with hide('stdout'):
            extra_opts = '--omit-dir-times'
            rsync_project(
                env.cwd,
                './',
                delete=True,
                exclude=['.git', '*.pyc'],
                extra_opts=extra_opts,
            )

    puts('> Switching changes to live')
    run('mv %s %s' % (target_dir, backup_dir))
    run('mv %s %s' % (staging_dir, target_dir))

@task
def rollback():
    if exists(backup_dir):
        puts('> Rolling back to previous deploy')
        run('mv %s %s' % (target_dir, staging_dir))
        run('mv %s %s' % (backup_dir, target_dir))
    else:
        abort('Rollback failed, no backup exists')

@task
def reload():
    puts('> Reloading nginx and php5-fpm')
    run('service nginx reload')
    run('service php5-fpm reload')

@task
def restart():
    puts('> Restarting nginx and php5-fpm')
    run('service nginx restart')
    run('service php5-fpm restart')
