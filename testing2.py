#!/usr/bin/python3

'''
Distribute archive to remote servers
'''
from fabric.api import run
from fabric.api import put
from fabric.api import env

env.user = 'root'
env.hosts = ['localhost']


def do_deploy(archive_path):
    '''
    Deploy an archive to specified location in remote servers
    '''

    # try to upload the archive to remote server, return false if failed
    if put("{}".format(archive_path), '/tmp/').failed:
        return False

    raw_name = archive_path.lstrip('versions/').rstrip('.tgz')
    destination = '/data/web_static/releases/{}'.format(raw_name)

    # create storage folder for archived files in remote
    if run('mkdir -p {}'.format(destination)).failed:
        return False

    # extract files from remote archive
    if run('tar -xzf /tmp/{} {}'.format(archive_path, destination)).failed:
        return False

    # remove temporary storage file, old symlink from remote
    run('rm -r /tmp/{}'.format(archive_path))
    run('rm -r /data/web_static/current')

    # create new symlink in remote for serving webpage
    if run('ln -sn {} /data/web_static/current'.format(destination)).succeeded:
        print('Successfuly deployed new content version')
        return True
    else:
        return False
