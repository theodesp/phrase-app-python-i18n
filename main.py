import gettext

el = gettext.translation('base', localedir='locales', languages=['el'], fallback=False)
el.install()
_ = el.gettext # Greek
ngettext = el.ngettext


def print_some_strings():
    print(_("Hello world"))
    print(_("This is a translatable string"))

def print_some_plural_strings(num):
    message1 = ngettext('{0} Human', '{0} Humans', num)
    message2 = ngettext('I possess {0} laptop', 'I possess {0} laptops', num)

    print(message1.format(num))
    print(message2.format(num))


print_some_plural_strings(1)
print_some_plural_strings(5)