# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
# Функция str.capitalize(). Первый символ строки становится прописным
# Функция str.casefold(). Вернуть свернутую копию строки
# Функция str.swapcase(). Вернуть копию строки с преобразованием строчных символов в заглавные и наоборот
# Функция str.title(). Вернуть строку с заглавными буквами в словах
# Функция str.upper(). Конвертировать символы строки в верхний регистр

# x = dict()
# for item in some_iterable:
#     x[item] = item
some_dict = {x.upper(): x.lower() for x in some_iterable}

print(some_dict)
