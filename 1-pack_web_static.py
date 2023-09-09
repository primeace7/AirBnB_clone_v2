#!/usr/bin/python3

'''
Generate an archive of files
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    Compress web static files into an archive
    '''

    # get time of archive creation
    creation_time = datetime.now().strftime('%Y%m%d%H%M%S')

    local('mkdir -p version')

    path = "version/web_static_{}.tgz".format(creation_time)

    # create the backup file
    local('touch {}'.format(path))

    command = "tar -cvzf {} web_static".format(path)

    if local(command).succeeded:
        return path
    else:
        return None
