import io
import os
import xdg

DATA_HOME = os.path.join(xdg.XDG_DATA_HOME, "pickaxe")
CONFIG_HOME = os.path.join(xdg.XDG_CONFIG_HOME, "pickaxe")


def init_xdg_data():
    if not os.path.exists(DATA_HOME):
        os.makedirs(DATA_HOME)
    if not os.path.exists(CONFIG_HOME):
        os.makedirs(CONFIG_HOME)

