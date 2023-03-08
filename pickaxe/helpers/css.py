from typing import Generic, Type, TypeVar
from gi.repository import Gtk

T = TypeVar('T')

class css:
    @staticmethod
    def add_class(widget: Gtk.Widget, name: str) -> None:
        widget.get_style_context().add_class(name)

    @staticmethod
    def remove_class(widget: Gtk.Widget, name: str) -> None:
        widget.get_style_context().remove_class(name)

