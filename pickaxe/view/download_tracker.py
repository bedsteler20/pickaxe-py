from minecraft_launcher_lib.types import CallbackDict
from gi.repository import Adw, Gtk


class DownloadTracker(Adw.Window):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.callbacks: CallbackDict = {
            'setMax': self.set_max,
            'setProgress': self.set_progress,
            'setStatus': self.set_max
        }

    def setStatus(value: int):
        pass

    def set_progress(value: int):
        pass

    def set_max(value: int):
        pass
