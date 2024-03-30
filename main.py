from transliterate.discover import autodiscover
autodiscover()
from transliterate.base import TranslitLanguagePack, registry
from transliterate import translit

class Normalize(TranslitLanguagePack):
    language_code = "normalize"
    language_name = ""
    mapping = (
        u"ĀāĒēŌōŪūȲȳĪīÜü",
        u"AaEeOoUuYyIiUu",
    )

registry.register(Normalize)


class PolishToBelarussian(TranslitLanguagePack):
    language_code = "po-be"
    language_name = "Belarusian"
    mapping = (
        u"aąbcdeęfghijkłmnoópqrstuùúvwyzżAĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUÙVWYZŹŻ",
        u"аабцдээфггійклмноопкрстуўўввызжААБЦЦДЕЕФГГІЙКЛЛМННООПКРССТУЎВВЫЗЗЖ",
    )
    pre_processor_mapping = {
        u"ć": u"ць",
        u"ś": u"сь",
        u"ń": u"нь",

        u"ie": u"е",
        u"ia": u"я",
        u"iu": u"ю",
        u"io": u"ё",

        u"je": u"е",
        u"ja": u"я",
        u"ju": u"ю",
        u"jo": u"ё",

        u"Je": u"Е",
        u"Ja": u"Я",
        u"Ju": u"Ю",
        u"Jo": u"Ё",

        u"ch": u"х",
        u"cz": u"ч",
        u"rz": u"ж",
        u"sz": u"ш",

        u"Ch": u"Х",
        u"Cz": u"Ч",
        u"Rz": u"Ж",
        u"Sz": u"Ш",

        u"x": u"кс",
        u"X": u"Кс",
        u"z̓": u"ж",
        u"Z̓": u"Ж",

        u"le": u"ле",
        u"la": u"ля",
        u"lo": u"лё",
        u"lu": u"лю",
        u"li": u"лі",
        u"l": u"ль",

        u"Le": u"Ле",
        u"La": u"Ля",
        u"Lo": u"Лё",
        u"Lu": u"Лю",
        u"Li": u"Лі",

        u"łe": u"лэ",
        u"ła": u"ла",
        u"ło": u"ло",
        u"łu": u"лу",

        u"Łe": u"Лэ",
        u"Ła": u"Ла",
        u"Ło": u"Ло",
        u"Łu": u"Лу",

        u"ź": u"зь",
        u"Ź": u"Зь"
    }


registry.register(PolishToBelarussian)

with open('Piosnki_plain.txt', 'r') as file:
    plain_text = file.read()



def transliterate_polish():
    repl = plain_text.replace(u'ē', u'e')
    repl = repl.replace(u'ā', u'a')
    repl = repl.replace(u'ū', u'u')
    repl = repl.replace(u'ü', u'u')
    repl = repl.replace(u'ō', u'o')
    repl = repl.replace(u'ī', u'i')

    translited = translit(repl, 'po-be')
    translited = translited.replace(u' се ', u'ся ')
    translited = translited.replace(u' се,', u'ся, ')
    translited = translited.replace(u' се.', u'ся. ')
    translited = translited.replace(u' се\n', u'ся\n')
    translited = translited.replace(u' ся ', u'cя ')
    translited = translited.replace(u' ся,', u'cя, ')
    translited = translited.replace(u' ся.', u'cя. ')
    translited = translited.replace(u' ся\n', u'cя\n')

    translited = translited.replace(u' ца ', u'ца ')
    translited = translited.replace(u' ца,', u'ца, ')
    translited = translited.replace(u' ца.', u'ца. ')
    translited = translited.replace(u' ца\n', u'ца\n')


    return translited



if __name__ == '__main__':
    translited = transliterate_polish()
    f = open("Piosnki.txt", 'w')
    f.write(translited)

