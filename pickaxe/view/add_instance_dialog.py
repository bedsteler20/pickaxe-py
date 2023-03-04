from gi.repository import Adw, Gtk, GObject
from pickaxe.managers.instance_manager import InstanceManager
from pickaxe.view.vanilla_instance_creator import VanillaInstanceCreator


@Gtk.Template.from_resource("/com/bedsteler20/Pickaxe/add_instance.ui")
class AddInstanceDialog(Adw.PreferencesWindow):
    __gtype_name__ = "AddInstanceDialog"

    view_stack: Adw.ViewStack = Gtk.Template.Child()
    main_page: Gtk.Box = Gtk.Template.Child()
    cancel_btn: Gtk.Button = Gtk.Template.Child()
    create_btn: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pages: dict[str, Gtk.Widget] = {
            "main_page": self.main_page,
            "vanilla": VanillaInstanceCreator(self)
        }

        for name in pages.keys():
            self.view_stack.add_named(pages[name], name)

        self.view_stack.set_visible_child_name("main_page")
        self.cancel_btn.connect("clicked", lambda _: self.close())

    @Gtk.Template.Callback()
    def on_vanilla_click(self, *args):
        self.view_stack.set_visible_child_name("vanilla")
