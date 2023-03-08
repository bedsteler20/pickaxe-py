from pickaxe.model.base import Model


class Instance(Model):
    __gtype_name__ = 'PickaxeInstance'
    icon: str = 'minecraft'
    name: str
    version: str

class Version(Model):
    __gtype_name__ = "Version"
    snapshot: bool = False
    name: str
