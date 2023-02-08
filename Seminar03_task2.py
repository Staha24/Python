import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))

english_text = {1: 'AEIOULNSTR',
                2: 'DG',
                3: 'BCMP',
                4: 'FHVWY',
                5: 'K',
                8: 'JX',
                10: 'QZ',
                }
russian_text = {1: 'АВЕИНОРСТ',
                2: 'ДКЛМПУ',
                3: 'БГЁЬЯ',
                4: 'ЙЫ',
                5: 'ЖЗХЦЧ',
                8: 'ШЭЮ',
                10: 'ФЩЪ',
                }
text = input('Введите слово: ').upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in russian_text.items() if i in v]))
else:
	print(sum([k for i in text for k, v in english_text.items() if i in v]))
