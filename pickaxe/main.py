import sys
import inject

from gi.repository import Gio, Adw
from pickaxe.helpers.misc import init_xdg_data
from pickaxe.managers.account_manager import AccountManager
from pickaxe.view.about_dialog import PickaxeAboutDialog
from pickaxe.view.add_instance_dialog import AddInstanceDialog
from pickaxe.view.preferences_window import PickaxePreferencesWindow
from pickaxe.view.window import PickaxeWindow


class PickaxeApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.bedsteler20.Pickaxe',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action(
            'add_instance', self.on_add_instance_action, ['<primary>n'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = PickaxeWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        about = PickaxeAboutDialog(transient_for=self.props.active_window,
                                   modal=True)
        about.present()

    def on_preferences_action(self, widget, _):
        win = PickaxePreferencesWindow(transient_for=self.props.active_window)
        win.present()

    def on_add_instance_action(self, *_):
        win = AddInstanceDialog(transient_for=self.props.active_window)
        win.present()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    init_xdg_data()
    app = PickaxeApplication()
    inject.configure_once(lambda binder: binder
                          .bind("app", app)
                          .bind(Gio.Settings, Gio.Settings("com.bedsteler20.Pickaxe"))
                          .bind(AccountManager, AccountManager()), True)
    return app.run(sys.argv)
