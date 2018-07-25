def tip():
    bill = int(input("Insert your bill amount!"))
    tip = .2 * bill
    totalBill = bill + tip
    return totalBill

print (tip())

"""
def tip(bill, percent):
    tip = percent * bill
    total = bill + tip
    return totalBill

myCheck = tip(44.65,.20)
print(myCheck)
myCheck = str(myCheck)
print("My total is $" + myCheck "!")

"""
