#foodprice1=7
#foodprice2=10
#totalcost=foodprice1+foodprice2
#print (totalcost)

#------------------------------------------------
#calculateTotal
foodprice1 = input("First choice ")
foodprice2 = input("Second choice ")
a = float(foodprice1)
b = float(foodprice2)
def add(a, b):
    result = a + b
    return result
total = add(a, b)
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
