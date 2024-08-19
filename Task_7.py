# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2000
# Output: YES

year = int(input('Input the year to check: '))

if year%4 ==0 and year%100 != 0 or year%400 ==0:

print('YES')
  else:
print('NO')

# a = 'Python'
# b = 'Hello world!'
# v = '\nПривет\n, меня зовут Вася, \nмне 28 лет!\n'
# # my_sep = '-||-'
# # print(a,b,v)
# # print(a,b,v, sep=my_sep , end='\n')
# print(a, end=v)
# print(b, end=v)
# print(v)
# # print()
# print(*'Python', sep='\n') # -> print('P', 'y', 't', 'h', 'o', 'n')
# print(*['P','y','t','h','o','n'], sep='~') # -> print('P', 'y', 't', 'h', 'o', 'n')
# Николай Мануилов name = "John"
# print('Hi, %s.' % name) #- Hi, John
# print('Hi, {name}'.format(name=name)) # - Hi, {name}
# print(f'Hi, {name}.')# - Hi, John.
# x = 2+5 * 90 // 12 **23
# print(2+5 * 90 // 12 **23)
# print(f'{2+5 * 90 // 12 **23}')
# print(f'{2+5 * 90 // 12 **23 = }')
# print(f'{x = }')