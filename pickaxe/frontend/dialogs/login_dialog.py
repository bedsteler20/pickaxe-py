from gi.repository import Gtk, WebKit2
from pickaxe.backend.managers.account_manager import AccountManager


class LoginDialog(Gtk.Window):
    def __init__(self, account_manager: AccountManager, **kwargs):
        super.__init__(**kwargs)
        self.account_manager = account_manager

        web_view =WebKit2.WebView()
        

