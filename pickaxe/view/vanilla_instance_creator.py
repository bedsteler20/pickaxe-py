from gi.repository import Adw, Gtk, GObject
from minecraft_launcher_lib.utils import get_version_list

from pickaxe.helpers.async_utils import async_call
from pickaxe.managers.instance_manager import InstanceManager
from typing import TYPE_CHECKING
import inject

if TYPE_CHECKING:
    from pickaxe.view.add_instance_dialog import AddInstanceDialog


@Gtk.Template.from_resource("/com/bedsteler20/Pickaxe/vanilla_instance_creator.ui")
class VanillaInstanceCreator(Adw.Bin):
    __gtype_name__ = "VanillaInstanceCreator"

    instance_manager = inject.attr(InstanceManager)

    name_entry: Adw.EntryRow = Gtk.Template.Child()
    version_combo: Adw.ComboRow = Gtk.Template.Child()
    version_model: Gtk.StringList = Gtk.Template.Child()
    create_btn: Gtk.Button = Gtk.Template.Child()

    def __init__(self, window: "AddInstanceDialog", **kwargs):
        super().__init__(**kwargs)
        self.window = window
        async_call(get_version_list, self.on_has_versions)

    def on_has_versions(self, result, err):
        if err != None:
            return
        for version in result:
            if version["type"] == "release":
                self.version_model.append(version["id"])

    @Gtk.Template.Callback()
    def on_cancel(self, *args):
        self.window.close()

    @Gtk.Template.Callback()
    def on_name_change(self, *args):
        name = self.name_entry.get_text()
        self.create_btn.set_sensitive((name != "" and
                                       not self.instance_manager.has_instance(name)))

    @Gtk.Template.Callback()
    def on_create(self, *args):
        print("Creating instance ", self.name_entry.get_text(),
              " on version ", self.version_combo.get_selected_item().get_string())
        self.instance_manager.add_instance(
            self.name_entry.get_text(),
            self.version_combo.get_selected_item().get_string(),
            callback={
                "setProgress": print
            }
        )
        self.parent.close()
