from gi.repository import GObject
from typing import Any, get_type_hints

class Model(GObject.GObject):
    __gtype_name__ = 'Model'

    def __init_subclass__(cls) -> None:
        for k, v in get_type_hints(cls).items():
            setattr(cls, k, GObject.Property(type=v))
        return super().__init_subclass__()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def dict(self) -> dict[str, Any]:
        res = {}
        for n in self.list_properties():
            res[n.name] = self.get_property(n.name)
        return res


