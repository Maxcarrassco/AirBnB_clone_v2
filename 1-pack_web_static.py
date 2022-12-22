#!/usr/bin/python3
"""ALX SE First Fabric Module."""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """Generate a .tgz archive from the contents of the web_static."""
    """Folder of your AirBnB Clone."""
    if not os.path.isdir('versions'):
        local("mkdir versions")
    time = datetime.now()
    time = datetime.strftime(time, "%Y%m%d%H%M%S")
    path = f"versions/web_static_{time}.tgz"
    local(f"tar -cvzf {path} web_static")
    if os.path.exists(path):
        return path
    return None
