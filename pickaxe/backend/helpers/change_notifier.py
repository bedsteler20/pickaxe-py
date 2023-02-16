class ChangeNotifier():

    def __init__(self) -> None:
        self.__listeners = []

    def dispose(self) -> None:
        for func in self.__listeners:
            self.unsubscribe(func)

    def subscribe(self, func):
        self.__listeners.append(func)

    def unsubscribe(self, func):
        self.__listeners.remove(func)

    def notify(self):
        for func in self.__listeners:
            func()
