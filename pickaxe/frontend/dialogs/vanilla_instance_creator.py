from gi.repository import Adw, Gtk, GObject
from minecraft_launcher_lib.utils import get_version_list

from pickaxe.backend.helpers.async_utils import async_call


@Gtk.Template.from_resource("/com/bedsteler20/Pickaxe/vanilla_instance_creator.ui")
class VanillaInstanceCreator(Adw.Bin):
    __gtype_name__ = "VanillaInstanceCreator"

    name_entry: Adw.EntryRow = Gtk.Template.Child()
    version_combo: Adw.ComboRow = Gtk.Template.Child()
    version_model: Gtk.StringList = Gtk.Template.Child()

    def __init__(self, parent: GObject.GObject, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent
        self.parent.create_btn.connect("clicked", self.on_create_btn)
        self.name_entry.connect("changed", self.on_name_change)
        async_call(get_version_list, self.on_has_versions)

    def on_has_versions(self, result, err):
        for version in result:
            if version["type"] == "release":
                self.version_model.append(version["id"])

    def on_name_change(self, *args):
        if self.name_entry.get_text() != "":
            self.parent.create_btn.set_sensitive(True)
        else:
            self.parent.create_btn.set_sensitive(False)

    def on_create_btn(self, *args):
        print("Creating instance ", self.name_entry.get_text(),
              " on version ", str(self.version_combo.get_selected_item().get_string()))
        self.parent.close()
        
