costp = int(input('Enter cost price of product: '))
sp = int(input('Enter selling price of product: '))
if sp>costp:
    print("Profit = $" , sp-costp, '. Product is being sold at a profit.')
else: 
    print('Loss = $', costp-sp, '. Product is being sold at a loss. ')