import gettext

el = gettext.translation('base', localedir='locales', languages=['el'])
el.install()
_ = el.gettext # Greek


def print_some_strings():
    print(_("Hello world"))
    print(_("This is a translatable string"))

print_some_strings()
