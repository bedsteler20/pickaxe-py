import sys

from gi.repository import Gtk, Gio
from ..frontend.window import PickaxeWindow


class PickaxeApplication(Gtk.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='com.bedsteler20.Pickaxe',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = PickaxeWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Gtk.AboutDialog(transient_for=self.props.active_window,
                                modal=True,
                                program_name='pickaxe',
                                logo_icon_name='com.bedsteler20.Pickaxe',
                                version='0.1.0',
                                authors=['Cameron Dehning'],
                                copyright='© 2023 Cameron Dehning')
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = PickaxeApplication()
    return app.run(sys.argv)
