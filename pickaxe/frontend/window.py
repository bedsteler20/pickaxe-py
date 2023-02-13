from gi.repository import Gtk, Adw

@Gtk.Template(resource_path='/com/bedsteler20/Pickaxe/window.ui')
class PickaxeWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PickaxeWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
