import io
import os
import xdg
from gi.repository import Gio
DATA_HOME = os.path.join(xdg.XDG_DATA_HOME, "pickaxe")
CONFIG_HOME = os.path.join(xdg.XDG_CONFIG_HOME, "pickaxe")


def init_xdg_data():
    if not os.path.exists(DATA_HOME):
        os.makedirs(DATA_HOME)
    if not os.path.exists(CONFIG_HOME):
        os.makedirs(CONFIG_HOME)


def get_instance_dir(name: str | None = None) -> str:
    f: str = Gio.Settings("com.bedsteler20.Pickaxe").get_string(
        "instance-location")
    f = f.replace("$XDG_DATA_HOME", str(xdg.XDG_DATA_HOME))
    if name == None:
        return f
    else:
        return os.path.join(f, name)
