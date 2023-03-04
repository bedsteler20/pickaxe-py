#!/usr/bin/env python
import os
import sys
import signal
import locale
import gettext


VERSION = '@VERSION@'
pkgdatadir = '@pkgdatadir@'
localedir = '@localedir@'
sourceroot = '@sourceroot@'

sys.path.insert(1, pkgdatadir)
signal.signal(signal.SIGINT, signal.SIG_DFL)
locale.bindtextdomain('pickaxe', localedir)
locale.textdomain('pickaxe')
gettext.install('pickaxe', localedir)

if os.environ.get("DEBUG_MODE") == "1":
    try:
        import debugpy
        debugpy.connect(5678)
    except:
        pass

if __name__ == '__main__':
    import gi
    gi.require_version('Gtk', '4.0')
    gi.require_version('Adw', '1')
    gi.require_version('WebKit2', '5.0')

    from gi.repository import Gio
    resource = Gio.Resource.load(os.path.join(
        pkgdatadir, 'pickaxe.gresource'))
    resource._register()

    from pickaxe import main
    sys.exit(main.main(VERSION))
