Item_Name = "Tv Stand"
Retail_price = 325.0 
Wholesale_price = 200.0
Profit = Retail_price - Wholesale_price
Sale_price = Retail_price - (Retail_price * 0.25)
Sale_profit = Sale_price - Wholesale_price
print ("Item Name:", Item_Name)
print("Retail Price: ${:.1f}".format(Retail_price))
print("Wholesale Price: ${:.1f}".format(Wholesale_price))
print("Profit: ${:.1f}".format(Profit))
print("Sale Price: ${:.2f}".format(Sale_price))
print("Sale_profit: ${:.2f}".format(Sale_profit))