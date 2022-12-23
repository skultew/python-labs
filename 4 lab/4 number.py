library={1:"библиотека1",2:"библиотека2",3:"библиотека3"}
key1=int(input('Введите ключ(от 1 до 3): '))

def  fun4(dictionary):
    res4=dictionary.get(key1)
    print("Ответ ", res4)

fun4(library)
print()
