from minecraft_launcher_lib import microsoft_account
from pickaxe.backend.helpers.promise import Promise
from pickaxe.backend.config import MS_CLIENT_ID, MS_CLIENT_SECRET, MS_REDIRECT_URL
from gi.repository import WebKit2, Gtk


def ms_login(transient_for) -> Promise:
    promise: Promise = Promise()

    win = Gtk.Dialog(transient_for=transient_for, modal=True)
    web_view = WebKit2.WebView()

    login_url = microsoft_account.get_login_url(
        MS_CLIENT_ID, MS_REDIRECT_URL)

    def on_url_change(*args):
        url: str = web_view.get_uri()
        code = microsoft_account.get_auth_code_from_url(url)

        if code is not None:
            login_data = microsoft_account.complete_login(
                MS_CLIENT_ID, MS_CLIENT_SECRET, MS_REDIRECT_URL, code)
            promise.resolve(login_data)
            win.close()

    def on_win_close(*args):
        if not promise.is_complete():
            promise.reject(None)

    win.connect('close-request', on_win_close)
    win.set_titlebar(Gtk.HeaderBar())
    web_view.connect('load-changed', on_url_change)
    web_view.load_uri(login_url)
    win.set_size_request(400, 550)
    win.set_title("Microsoft Login")
    win.set_resizable(False)
    win.set_child(web_view)
    win.show()

    return promise
