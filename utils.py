import sys

SETTING_PREFIX = 'EAUTH'


def filter_config(configs):
    return {k.replace(SETTING_PREFIX + '_', ''): v for k, v in
            configs.items() if k.startswith(SETTING_PREFIX)}


def import_module(name):
    __import__(name)
    return sys.modules[name]


def module_member(name):
    mod, member = name.rsplit('.', 1)
    module = import_module(mod)
    return getattr(module, member)


def to_setting_name(*names):
    return '_'.join([name.upper().replace('-', '_') for name in names if name])


def setting_name(*names):
    return to_setting_name(*((SETTING_PREFIX,) + names))
