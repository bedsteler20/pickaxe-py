from gi.repository import Gtk, Gio, Adw, GObject

import inject
from pickaxe.managers.instance_manager import InstanceManager
from pickaxe.model.instance import Instance
from pickaxe.widgets.instance_card import InstanceCard


@Gtk.Template.from_resource('/com/bedsteler20/Pickaxe/window.ui')
class PickaxeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PickaxeWindow'
    instance_manager = inject.attr(InstanceManager)

    factory: Gtk.SignalListItemFactory = Gtk.Template.Child()
    selection: Gtk.NoSelection = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = Gio.Settings(schema_id="com.bedsteler20.Pickaxe")
        self.settings.bind("width", self, "default-width",
                           Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("height", self, "default-height",
                           Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("is-maximized", self, "maximized",
                           Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("is-fullscreen", self, "fullscreened",
                           Gio.SettingsBindFlags.DEFAULT)
        model = Gio.ListStore()
        for i in self.instance_manager.instances:
            model.append(i)
        self.selection.set_model(model)

    @Gtk.Template.Callback()
    def on_setup(self, factory: Gtk.SignalListItemFactory, list_item: Gtk.ListItem) -> None:
        """Creates the widget to be displayed but does NOT know what data the widget will contain"""

        list_item.set_child(InstanceCard())

    @Gtk.Template.Callback()
    def on_bind(self, factory: Gtk.SignalListItemFactory, list_item: Gtk.ListItem) -> None:
        """binds values in the model to the widget created in `on_setup`"""
        list_item.get_child().bind(list_item.get_item())
