import re

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'

exm = re.findall(r'\\wwood\+\?,', text)
print('Список всех упоминаний шаблона:', exm)
