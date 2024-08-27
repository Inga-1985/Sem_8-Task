#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def remove_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Пример использования
input_lst = [1, 2, 2, 3, 4, 4, 5]
result_lst = remove_duplicates(input_lst)
print(result_lst)  # Output: [2, 4]