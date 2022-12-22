#!/usr/bin/python3
"""ALX SE First Fabric Module."""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz archive from the contents of the web_static."""
    """Folder of your AirBnB Clone."""
    time = datetime.now()
    time = datetime.strftime(time, "%Y%m%d%H%M%S")
    path = f"versions/name_{time}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf {path} web_static")

    if result.succeeded:
        return path
