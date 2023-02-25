from gi.repository import Gtk


def add_class(widget: Gtk.Widget, name: str) -> None:
    widget.get_style_context().add_class(name)


def remove_class(widget: Gtk.Widget, name: str) -> None:
    widget.get_style_context().remove_class(name)
