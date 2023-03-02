import json
from minecraft_launcher_lib.microsoft_types import CompleteLoginResponse
from gi.repository import Gio
from pickaxe.backend.helpers.change_notifier import ChangeNotifier
import inject

class AccountManager(ChangeNotifier):
    settings = Gio.Settings("com.bedsteler20.Pickaxe")

    def __init__(self):
        super().__init__()

        self.accounts: list[CompleteLoginResponse] = json.loads(
            self.settings.get_string('accounts'))

    def get_active(self):
        if len(self.accounts) >= 1:
            return self.accounts[0]
        else:
            return None

    def add_account(self, account: CompleteLoginResponse):
        self.accounts.append(account)
        self.notify()
        self.settings.set_string("accounts", json.dumps(self.accounts))

    def set_active(self, account: CompleteLoginResponse):
        self.accounts.insert(0, self.accounts.pop(account))
        self.notify()
        self.settings.set_string("accounts", json.dumps(self.accounts))

    def remove_account(self, account: CompleteLoginResponse):
        self.accounts.remove(account)
        self.notify()
        self.settings.set_string("accounts", json.dumps(self.accounts))
