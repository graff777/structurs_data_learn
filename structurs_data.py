#структуры данных и операции с ними
#списки, массивы, словари
dict={'word':'слово', 'key':'ключ','value':'количество'}
spisok=['word','key','value']
names=['Саша', 'Женя', 'Виктор']
def messaga(message):
    messs=set(message.split(' '))
    return messs

def func(slovo):
    if slovo in spisok:
        if slovo in dict.keys():
            print('good')
        else:
            print('bad')
#func('word')
#print(messaga('привет как дела?'))
sl=messaga('Саша привет, как дела?')
for i in range(0,len(sl)):
    if sl[i] in sl:
        if sl[i] in names:
            print('Всё ок')
        else:
            print('такого имени нет')
#print(sl)
