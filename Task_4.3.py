# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)

# Функция меню
def menu():
    dct = {
        '1': 'Пополнить счет',
        '2': 'Снять со счета',
        '3': 'Выйти из программы'
    }
    
    for k, v in dct.items():
        print(f'{k}: {v}')

# Функция выбора меню
def select_an_operation(balance: Decimal, count: int, is_flag: bool, operations: list):
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)

    choice = input('Введите команду: ')
    if choice == '3':
        print(f'Баланс: {balance:.2f}')
        is_flag = False
        return balance, is_flag
    elif choice == '1':
        balance, operation = give_money(balance)
        operations.append(operation)
        count += 1
    elif choice == '2':
        balance, operation = get_money(balance)
        operations.append(operation)
        count += 1
    else:
        print('Неверная команда')
    
    if count % 3 == 0:
        balance *= (1 + BONUS)

    print(f'Баланс: {balance:.2f}')
    return balance, is_flag

# Функция снятия суммы
def get_money(balance: Decimal):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION
    operation = f'Снятие: {money_to_get:.2f}'

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            return balance - (money_to_get + procent), operation
        else:
            print('Недостаточно средств для снятия')
            return balance, operation

    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50')
        return balance, operation

# Функция пополнения суммы
def give_money(balance: Decimal):
    money_to_give = Decimal(input('Введите сумму пополнения: '))
    operation = f'Пополнение: {money_to_give:.2f}'

    if money_to_give % MIN_SUM == 0:
        return balance + money_to_give, operation
    else:
        print('Сумма пополнения должна быть кратна 50')
        return balance, operation

def run():
    balance = Decimal(0)
    count = 1
    is_flag = True
    operations = []
    while is_flag:
        menu()
        balance, is_flag = select_an_operation(balance, count, is_flag, operations)
    
    print("История операций:")
    for op in operations:
        print(op)

def main():
    run()

if __name__ == '__main__': 
    main()