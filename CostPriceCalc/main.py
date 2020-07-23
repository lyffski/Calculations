

vListPrice              = float(input("Entry your List Price: "))
ptcPurchaseDiscount     = float(input("Entry your Purchase Discount (eg. 3 % = 0.03): "))
ptcPurchaseCashDiscount = float(input("Entry your Purchase Cash Discount (eg. 4 % = 0.04): "))
rvDeliveryCost          = float(input("Entry your Delivery Cost (if none insert 0): "))


vPurchaseDiscount   = vListPrice * ptcPurchaseDiscount
rvPurchaseDiscount  = round(vPurchaseDiscount, 2)

rvTargetPurchasePrice = vListPrice - rvPurchaseDiscount

vPurchaseCashDiscount = rvTargetPurchasePrice * ptcPurchaseCashDiscount
rvPurchaseCashDiscount= round(vPurchaseCashDiscount, 2)

vCashBuyingPrice = rvTargetPurchasePrice - rvPurchaseCashDiscount
rvCashBuyingPrice = round(vCashBuyingPrice, 2)

vCostPrice = rvCashBuyingPrice + rvDeliveryCost
rvCostPrice = round(vCostPrice, 2)


print(vListPrice, "List Price")
print(rvPurchaseDiscount, "Purchase Discount")
print(rvTargetPurchasePrice, "Target Purchase Price")
print(rvPurchaseCashDiscount, "Purchase Cash Discount")
print(rvCashBuyingPrice, "Cash buying Price")
print(rvDeliveryCost, "Delivery Cost")
print(rvCostPrice, "Cost Price")

print(" ")

x = input("Press any Key to exit")
