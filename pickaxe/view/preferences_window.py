from os import path
from gi.repository import Gtk, Adw, Gio
from pickaxe.helpers.misc import DATA_HOME
from pickaxe.managers.account_manager import AccountManager
from pickaxe.view.login_dialog import LoginDialog
from pickaxe.helpers.css import css
import inject


@Gtk.Template.from_resource('/com/bedsteler20/Pickaxe/preferences.ui')
class PickaxePreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'PickaxePreferencesWindow'

    settings = inject.attr(Gio.Settings)
    account_manager = inject.attr(AccountManager)

    accounts_row: Adw.ActionRow = Gtk.Template.Child()
    accounts_btn: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.account_manager.subscribe(self.set_state)
        self.accounts_btn.connect("clicked", self.__on_account_btn_clicked)
        self.set_state()

    def set_state(self, *args):
        user = self.account_manager.get_active()

        if user is None:
            self.accounts_btn.set_label("Login")
            self.accounts_row.set_title("Not logged in")
            css.remove_class(self.accounts_btn, "destructive-action")
            css.add_class(self.accounts_btn, "suggested-action")
        else:
            self.accounts_btn.set_label("Logout")
            self.accounts_row.set_title(f"Logged in as {user['name']}")
            css.remove_class(self.accounts_btn, "suggested-action")
            css.add_class(self.accounts_btn, "destructive-action")

    def __on_account_btn_clicked(self, *args):
        user = self.account_manager.get_active()
        if user is None:
            LoginDialog().then(
                self.account_manager.add_account)
        else:
            self.account_manager.remove_account(user)
