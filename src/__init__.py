"""
Find all exceptions that your code and its dependencies can raise, to make your work foolproof!
:param to_analyze: a module, function, ... to analyze for exceptions
"""
from sys import modules
from types import ModuleType
from .exception_parser import ParseExceptions

__all__ = ["ParseExceptions"]


class CallableModule(ModuleType):
    def __init__(self):
        ModuleType.__init__(self, __name__)
        self.__dict__.update(modules[__name__].__dict__)

    def __call__(self, *args, **kwargs):
        ParseExceptions(*args, **kwargs)

    mod_call = __call__
    __all__ = list(set(vars().keys()) - {"__qualname__"})


modules[__name__] = CallableModule()
