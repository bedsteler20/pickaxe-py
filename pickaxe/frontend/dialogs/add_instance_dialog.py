from gi.repository import Adw, Gtk
from pickaxe.backend.managers.instance_manager import InstanceManager
from pickaxe.frontend.dialogs.vanilla_instance_creator import VanillaInstanceCreator
# from pickaxe.frontend.dialogs.vanilla_instance_creator import VanillaInstanceCreator


@Gtk.Template.from_resource("/com/bedsteler20/Pickaxe/add_instance.ui")
class AddInstanceDialog(Adw.PreferencesWindow):
    __gtype_name__ = "AddInstanceDialog"

    view_stack: Adw.ViewStack = Gtk.Template.Child()
    main_page: Adw.PreferencesPage = Gtk.Template.Child()
    vanilla: Adw.ActionRow = Gtk.Template.Child()
    cursed: Adw.ActionRow = Gtk.Template.Child()
    modded: Adw.ActionRow = Gtk.Template.Child()
    cancel_btn: Gtk.Button = Gtk.Template.Child()
    create_btn: Gtk.Button = Gtk.Template.Child()

    def __init__(self, instance_manager: InstanceManager, **kwargs):
        super().__init__(**kwargs)
        self.vanilla.connect("activated", self.on_vanilla_click)
        self.cursed.connect("activated", self.on_cursed_click)
        self.modded.connect("activated", self.on_modded_click)
        self.view_stack.add_named(self.main_page, "main_page")
        self.view_stack.add_named(VanillaInstanceCreator(
            parent=self, instance_manager=instance_manager), "vanilla")
        self.view_stack.set_visible_child_name("main_page")
        self.cancel_btn.connect("clicked", lambda _: self.close())

    def on_vanilla_click(self, *args):
        self.view_stack.set_visible_child_name("vanilla")

    def on_cursed_click(self, *args):
        pass

    def on_modded_click(self, *args):
        pass
