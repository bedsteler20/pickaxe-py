from gi.repository import Gtk, Adw
from pickaxe.model.instance import Instance


@Gtk.Template.from_resource('/com/bedsteler20/Pickaxe/instance_card.ui')
class InstanceCard(Adw.Bin):
    __gtype_name__ = 'InstanceCard'

    name_label: Gtk.Label = Gtk.Template.Child()
    image: Gtk.Image = Gtk.Template.Child()

    def bind(self, instance: Instance):
        instance.bind_property('name', self.name_label, 'label')
        instance.bind_property('icon', self.image, 'icon-name')
