from gi.repository import Gtk, Gio, Adw


@Gtk.Template(resource_path='/com/bedsteler20/Pickaxe/window.ui')
class PickaxeWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PickaxeWindow'

    label = Gtk.Template.Child()
    avatar: Adw.Avatar = Gtk.Template.Child()

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
