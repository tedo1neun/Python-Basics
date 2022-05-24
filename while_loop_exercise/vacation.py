vacation_money = float(input())
money_balance = float(input())
spent_days = 0
days = 0

while True:
    act = input()
    money = float(input())
    days += 1
    if act == 'spend':
        spent_days += 1
        money_balance -= money
        if money_balance < 0:
            money_balance = 0

    if act == 'save':
        money_balance += money
        spent_days = 0

    if spent_days == 5:
        print("You can't save the money.")
        print(f'{days}')
        break

    if money_balance >= vacation_money:
        print(f'You saved the money for {days + spent_days} days.')
        break