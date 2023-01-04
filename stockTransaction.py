#ellena carmean
#9/1/22
#computer programming
#in this program we are displaying information about joes stock transaction
total_shares = 2000
stock_paid = 40.00
stock_sold = 42.75
sub_total_paid = 2000 * 40.00
sub_total_sold = 2000 * 42.75
commission = 0.3
commission_paid = sub_total_paid * commission
commission_recieved = sub_total_sold * commission
final_total_paid = total_shares * 40 + commission_paid
final_total_sold = total_shares * 42.75 + commission_recieved

print("amount paid for the stock: $", stock_paid)
print("commission paid on the purchase: $", commission_paid)
print("amount the stock sold for: $", stock_sold)
print("commission paid on the sale: $", commission_recieved)
print("profit (or loss if negative): $", final_total_paid - final_total_sold)
