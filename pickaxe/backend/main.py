import sys

from gi.repository import Gtk, Gio
from pickaxe.backend.managers.account_manager import AccountManager
from pickaxe.frontend.dialogs.login_dialog import ms_login
from pickaxe.frontend.window import PickaxeWindow


class PickaxeApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.bedsteler20.Pickaxe',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

        self.settings = Gio.Settings("com.bedsteler20.Pickaxe")
        self.account_manager = AccountManager(self.settings)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = PickaxeWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        about = Gtk.AboutDialog(transient_for=self.props.active_window,
                                modal=True,
                                program_name='pickaxe',
                                logo_icon_name='com.bedsteler20.Pickaxe',
                                version='0.1.0',
                                authors=['Cameron Dehning'],
                                copyright='© 2023 Cameron Dehning')
        about.present()

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')
        login_manager = ms_login(self.props.active_window)
        login_manager.then(self.account_manager.add_account)

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = PickaxeApplication()
    return app.run(sys.argv)
