import json
from gi.repository import Adw, Gio, Gtk, GLib


def PickaxeAboutDialog(**kwargs):
    res = Gio.resources_lookup_data(
        '/com/bedsteler20/Pickaxe/app_info.json', Gio.ResourceLookupFlags.NONE)
    js = json.loads(res.get_data().decode())
    for key in js.keys():
        kwargs[key.replace('-', '_')] = js[key]
    return Adw.AboutWindow(**kwargs)
