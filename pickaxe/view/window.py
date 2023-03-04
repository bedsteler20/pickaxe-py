from gi.repository import Gtk, Gio, Adw

import inject
from pickaxe.config import DEVEL
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
        # self.selection.set_model(
        #     self.instance_manager.instances)

    @Gtk.Template.Callback()
    def on_setup(self, factory: Gtk.SignalListItemFactory, list_item: Gtk.ListItem) -> None:
        item: Instance = list_item.get_item()
        label = Gtk.Label()
        label.set_label(item)
        list_item.set_child(label)

    @Gtk.Template.Callback()
    def on_bind(self, factory: Gtk.SignalListItemFactory, list_item: Gtk.ListItem) -> None:
        object = list_item.get_item()
        child = list_item.get_child()
        child.set_item(object.get_item())

        # for v in range(10):
        #     instance = Instance(name="Minecraft")
        #     self.content.append(InstanceCard(instance))
