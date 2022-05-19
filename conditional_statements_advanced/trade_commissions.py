town = input()
sales_capacity = float(input())
commission = 0
if town == 'Sofia':
    if 0 <= sales_capacity <= 500:
        commission = 5/100 * sales_capacity
    elif 500 < sales_capacity <= 1000:
        commission = 7/100 * sales_capacity
    elif 1000 < sales_capacity <= 10000:
        commission = 8/100 * sales_capacity
    elif sales_capacity > 10000:
        commission = 12/100 * sales_capacity
    else:
        print('error')
if town == 'Varna':
    if 0 <= sales_capacity <= 500:
        commission = 4.5 / 100 * sales_capacity
    elif 500 < sales_capacity <= 1000:
        commission = 7.5 / 100 * sales_capacity
    elif 1000 < sales_capacity <= 10000:
        commission = 10 / 100 * sales_capacity
    elif sales_capacity > 10000:
        commission = 13 / 100 * sales_capacity
    else:
        print('error')
if town == 'Plovdiv':
    if 0 <= sales_capacity <= 500:
        commission = 5.5 / 100 * sales_capacity
    elif 500 < sales_capacity <= 1000:
        commission = 8 / 100 * sales_capacity
    elif 1000 < sales_capacity <= 10000:
        commission = 12 / 100 * sales_capacity
    elif sales_capacity > 10000:
        commission = 14.5 / 100 * sales_capacity
        if town == 'Plovdiv' and commission == -20:
            print('')

if commission > 0:
    print(f'{commission:.2f}')
else:
    print('error')
