from minecraft_launcher_lib import microsoft_account
from pickaxe.backend.helpers.promise import Promise
from pickaxe.backend.config import MS_CLIENT_ID, MS_CLIENT_SECRET, MS_REDIRECT_URL
from gi.repository import WebKit2, Gtk


class LoginDialog(Gtk.Dialog, Promise):

    def __init__(self, **kwargs):
        Gtk.Dialog.__init__(self, **kwargs)
        Promise.__init__(self)
        self.code: None | str = None
        self.web_view = WebKit2.WebView()
        self.login_data = None
        login_url, self.state, self.code_verifier = microsoft_account.get_secure_login_data(
            MS_CLIENT_ID, MS_REDIRECT_URL)

        self.web_view.load_uri(login_url)
        self.connect('close-request', self.on_win_close)
        self.web_view.connect('notify::uri', self.on_url_change)

        self.set_size_request(400, 550)
        self.set_title("Microsoft Login")
        self.set_modal(True)
        self.set_child(self.web_view)
        self.set_resizable(False)
        self.show()

    def on_url_change(self, *args):
        url: str = self.web_view.get_uri()
        self.code = microsoft_account.get_auth_code_from_url(url)

        if self.code is not None and self.login_data is None:
            self.login_data = microsoft_account.complete_login(
                MS_CLIENT_ID, None, MS_REDIRECT_URL, self.code, self.code_verifier)
            self.resolve(self.login_data)
            self.close()

    def on_win_close(self, *args):
        if not self.is_complete():
            self.reject(None)
