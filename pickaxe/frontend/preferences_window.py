from gi.repository import Gtk, Adw
from pickaxe.backend.managers.account_manager import AccountManager
from pickaxe.frontend.dialogs.login_dialog import LoginDialog


@Gtk.Template(resource_path='/com/bedsteler20/Pickaxe/preferences.ui')
class PickaxePreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'PickaxePreferencesWindow'

    accounts_row: Adw.ActionRow = Gtk.Template.Child()
    accounts_btn: Gtk.Button = Gtk.Template.Child()

    def __init__(self, account_manager: AccountManager, **kwargs):
        super().__init__(**kwargs)
        self.account_manager = account_manager

        self.__update_account_row()

        self.account_manager.subscribe(self.__update_account_row)
        self.accounts_btn.connect("clicked", self.__on_account_btn_clicked)

    def __update_account_row(self):
        user = self.account_manager.get_active()
        style_ctx: Gtk.StyleContext = self.accounts_btn.get_style_context()
        if user is None:
            self.accounts_btn.set_label("Login")
            style_ctx.remove_class("destructive-action")
            style_ctx.add_class("suggested-action")
            self.accounts_row.set_title("Not logged in")
        else:
            self.accounts_btn.set_label("Logout")
            style_ctx.remove_class("suggested-action")
            style_ctx.add_class("destructive-action")
            self.accounts_row.set_title(f"Logged in as {user['name']}")

    def __on_account_btn_clicked(self, *args):
        user = self.account_manager.get_active()
        if user is None:
            LoginDialog().then(
                self.account_manager.add_account)
        else:
            self.account_manager.remove_account(user)
