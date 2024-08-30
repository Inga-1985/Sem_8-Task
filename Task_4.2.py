# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        # Пробуем использовать значение как ключ
        try:
            result[value] = key
        except TypeError:
            # Если значение не хешируемо, используем его строковое представление
            result[str(value)] = key
    return result

if __name__ == '__main__':
    print(kwargs_to_dict(name='Илья', sername='Игушев', patronymic='Олегович',
                          task=[1, 2, 3],
                          physique={'weight': '170', 'height': '65'}))