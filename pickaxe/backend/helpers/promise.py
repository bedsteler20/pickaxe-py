
class PromiseAlreadyCompletedException(Exception):
    pass


class Promise():
    def __init__(self):
        self.__listeners = []
        self.__catchers = []
        self.__complete = False
        self.__has_error = False
        self.__error = None
        self.__value = None

    def then(self, func) -> None:
        if (self.__complete and not self.__has_error):
            func(self.__value)
        else:
            self.__listeners.append(func)

    def catch(self, func) -> None:
        if (self.__complete and self.__has_error):
            func(self.__error)
        else:
            self.__catchers.append(func)

    def reject(self, value) -> None:
        if (self.__complete):
            raise PromiseAlreadyCompletedException
        self.__error = value
        self.__has_error = True
        for func in self.__catchers:
            func(value)
        self.__listeners = []
        self.__catchers = []
        self.__complete = True

    def resolve(self, value) -> None:
        if (self.__complete):
            raise PromiseAlreadyCompletedException
        self.__value = value
        for func in self.__listeners:
            func(value)
        self.__listeners = []
        self.__catchers = []
        self.__complete = True

    def is_complete(self) -> bool:
        return self.__complete