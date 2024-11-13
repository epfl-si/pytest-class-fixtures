import inspect
import pytest


def class_fixture (*args, **kwargs):
    def class_fixturer (cls):
        @pytest.fixture(**kwargs)
        def construct():
            return cls()

        cls._pytestfixturefunction = construct._pytestfixturefunction
        return cls

    if args and inspect.isclass(args[0]):
        return class_fixturer(args[0])
    else:
        return class_fixturer
