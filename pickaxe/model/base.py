from gi.repository import GObject
from typing import Any, get_type_hints
global __models__

__models__ = {}


class Model(GObject.GObject):
    __gtype_name__ = 'Model'

    def __init_subclass__(cls) -> None:
        assert cls.__gtype_name__ != Model.__gtype_name__, f"A model in f{cls.__module__} doesn't have a __gtype_name__"

        __models__[cls.__gtype_name__] = cls
        for k, v in get_type_hints(cls).items():
            if hasattr(cls, k):
                default = getattr(cls, k)
            elif isinstance(v, bool):
                default = False
            else:
                default = None

            if default is not None:
                setattr(cls, k, GObject.Property(type=v, default=default))
            else:
                setattr(cls, k, GObject.Property(type=v))
        return super().__init_subclass__()

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if isinstance(v, dict):
                if '__gtype_name__' in v.keys():
                    kwargs[k] = __models__[v['__gtype_name__']](**v)
        super().__init__(**kwargs)

    def dump(self) -> dict[str, Any]:
        res = {"__gtype_name__": self.__gtype_name__}
        for n in self.list_properties():
            v = self.get_property(n.name)
            if isinstance(v, Model):
                v = v.dump()
            res[n.name] = self.get_property(n.name)
        return res

    def bind_property(
        self,
        source_property: str,
        target: GObject.Object,
        target_property: str,
        flags: GObject.BindingFlags = GObject.BindingFlags.SYNC_CREATE,
    ) -> GObject.Binding: super().bind_property(source_property, target, target_property, flags)
