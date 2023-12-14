# This is a modified version of https://github.com/DontShaveTheYak/deep-ast (https://pypi.org/project/deep-ast/)
# License: GNU General Public License v3 (GPLv3)
# All credits goes to Levi Blaney - @shady_cuz, shadycuz@gmail.com
import ast
from collections.abc import Callable
import inspect
from types import ModuleType, FunctionType
from typing import Any
from .deep_ast import DeepMixin


class ParseExceptions(DeepMixin, ast.NodeVisitor):
    def __init__(self, obj: Any) -> None:
        self.found_exceptions = set()
        super().__init__()
        
        if isinstance(obj, ModuleType):
            for obj in obj.__dict__.values():
                if inspect.isfunction(obj):
                    self.deep_visit(obj)
                elif isinstance(obj, ModuleType):
                    pass  # TODO : this should be recursive
                elif inspect.isclass(obj):
                    for m_obj in obj.__dict__.values():
                        if inspect.isfunction(m_obj):
                            self.deep_visit(m_obj)
        elif isinstance(obj, Callable):
            self.deep_visit(obj)

    def _add_exception(self, obj):
        if obj not in self.found_exceptions:
            self.found_exceptions.add(obj)
            name, args = obj
            print(name + " : " + args.strip())

    def visit_Raise(self, node):
        exception_obj = node.exc

        if isinstance(exception_obj, (ast.Call, ast.Name)):
            name = exception_obj.id if isinstance(exception_obj, ast.Name) else exception_obj.func.id
            if hasattr(exception_obj, "args"):
                args = ", ".join([a.value for a in exception_obj.args if hasattr(a, "value")])
            else:
                args = ""

            self._add_exception((name, args))
            return self.generic_visit(node)

        self._add_exception(("EmptyRaise", ""))
        return self.generic_visit(node)
