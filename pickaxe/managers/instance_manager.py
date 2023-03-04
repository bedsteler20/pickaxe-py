from os import path
import os
import json
from pickaxe.helpers.misc import DATA_HOME, get_instance_dir
from pickaxe.model.instance import Instance
from minecraft_launcher_lib import install
from minecraft_launcher_lib.types import CallbackDict
from gi.repository import Gio


class InstanceManager():
    def __init__(self) -> None:
        self.conf_file = path.join(DATA_HOME, 'instances.json')

        self.__load()

    def add_instance(self, name: str, version: str, callback: CallbackDict | None = None):
        instance_dir = get_instance_dir(name)
        self.instances.append({
            "name": name,
            "version": version
        })
        install.install_minecraft_version(version, instance_dir, callback)
        self.__dump()

    def __dump(self):
        open(self.conf_file, "w+").write(json.dumps(self.instances))

    def __load(self):

        try:
            self.instances: list[Instance] = json.loads(
                open(self.conf_file, "r").read())
        except:
            self.instances = []

    def has_instance(self, name: str) -> bool:
        for i in self.instances:
            if i["name"] == name:
                return True
        return False
