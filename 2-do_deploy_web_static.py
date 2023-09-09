#!/usr/bin/python3

'''
Distribute archive to remote servers
'''
from fabric.api import run
from fabric.api import put
from fabric.api import env
from fabric.api import sudo

env.user = 'ubuntu'
env.hosts = ['54.84.79.181', '52.3.241.176']


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
    if run('sudo mkdir -p {}'.format(destination)).failed:
        return False

    # extract files from remote archive
    tmp_location = '/tmp/web_static_20230909154905.tgz'
    if run('sudo tar -xzf {} -C {}'.format(tmp_location, destination)).failed:
        return False

    # remove temporary storage file, old symlink from remote
    run('sudo rm -r {}'.format(tmp_location))
    run('sudo rm -rf /data/web_static/current')

    # create new symlink in remote for serving webpage
    if sudo('ln -sn {} /data/web_static/current'.format(destination))\
       .succeeded:
        print('Successfuly deployed new content version')
        return True
    else:
        return False
