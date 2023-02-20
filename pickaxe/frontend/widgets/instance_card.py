from gi.repository import Gtk
from pickaxe.backend.model.instance import Instance


@Gtk.Template.from_resource('/com/bedsteler20/Pickaxe/instance_card.ui')
class InstanceCard(Gtk.FlowBoxChild):
    __gtype_name__ = 'InstanceCard'

    name_label: Gtk.Label = Gtk.Template.Child()

    def __init__(self, instance: Instance, **kwargs):
        super().__init__(**kwargs)
        self.name_label.set_label(instance.name)
