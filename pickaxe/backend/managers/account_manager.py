from minecraft_launcher_lib.microsoft_types import CompleteLoginResponse
class AccountManager():

    def __init__(self):
        self.accounts = []

    def add_account(self, account:CompleteLoginResponse):
        print(f"adding account {account['name']}")
