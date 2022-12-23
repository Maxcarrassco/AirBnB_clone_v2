#!/usr/bin/python3
"""ALX SE First Fabric Module."""
from datetime import datetime
from fabric.api import local
import os.path

def do_pack():
    """Generate a .tgz archive from the contents of the web_static."""
    """Folder of your AirBnB Clone."""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        local(" mkdir versions")
    local('tar -cvzf ' + file_path + ' web_static')
    if os.path.exists(file_path):
        return file_path
    return None
