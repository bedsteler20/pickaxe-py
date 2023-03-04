from os import path
import os
import json
from pickaxe.helpers.misc import DATA_HOME, get_instance_dir
from pickaxe.model.instance import Instance
from minecraft_launcher_lib import install
from minecraft_launcher_lib.types import CallbackDict
from gi.repository import Gtk


class InstanceManager():
    def __init__(self) -> None:
        self.conf_file = path.join(DATA_HOME, 'instances.json')
        self.instances = []

        self.__load()

    def add_instance(self, name: str, version: str, callback: CallbackDict | None = None):
        instance_dir = get_instance_dir(name)
        self.instances.append(Instance(name=name, version=version))
        install.install_minecraft_version(version, instance_dir, callback)
        self.__dump()

    def __dump(self):
        try:
            with open(self.conf_file, "w+") as f:
                f.write(json.dumps([i.dict() for i in self.instances]))
        except:
            pass
    def __load(self):
        try:
            with open(self.conf_file) as f:
                for instance in json.loads(f.read()):
                    self.instances.append(Instance(**instance))
        except:
            pass

    def has_instance(self, name: str) -> bool:
        for i in self.instances:
            if i["name"] == name:
                return True
        return False
