print("sales tax:")
purchase_Amount = eval(input("Enter purchased amount: "))

calculate = purchase_Amount * 0.06

tax = "{:.2f}".format(calculate)
print("Amount:" ,"Sales tax:" ,"{:.2f}".format(calculate))


