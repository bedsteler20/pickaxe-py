import json
from minecraft_launcher_lib.microsoft_types import CompleteLoginResponse
from gi.repository import Gio


class AccountManager():

    def __init__(self, settings: Gio.Settings):
        self.settings = settings

        self.accounts: list[CompleteLoginResponse] = json.loads(
            self.settings.get_string('accounts'))

    def add_account(self, account: CompleteLoginResponse):
        self.accounts.append(account)
        self.settings.set_string("accounts", json.dumps(self.accounts))