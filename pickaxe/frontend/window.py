from gi.repository import Gtk, Gio, Adw
from pickaxe.backend.config import DEVEL
from pickaxe.backend.model.instance import Instance
from pickaxe.frontend.widgets.instance_card import InstanceCard


@Gtk.Template.from_resource('/com/bedsteler20/Pickaxe/window.ui')
class PickaxeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PickaxeWindow'

    content: Gtk.FlowBox = Gtk.Template.Child()

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

        # for v in range(10):
        #     instance = Instance(name="Minecraft")
        #     self.content.append(InstanceCard(instance))
