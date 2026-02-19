#calculateTotal
menu_items = ['a', 'b']
menu_prices = [7.50, 9.00]

def add(a, b):
    result = a + b
    return result
total = add('a', 'b')
result = float(total)
#print(result)

#------------------------------------------------
#applyDiscount
if result>=10:
    answer=result*0.9
else:
    answer=result
#print(answer)

#------------------------------------------------
#displayReceipt
username = input('What is your name? ')
print(username)
print(answer)
