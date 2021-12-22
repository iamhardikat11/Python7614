
print("*******Welcome to the Tip Calculator********")

bill = float(input("Hey Customer!! Please enter the value of bills? in $"))
tip = int(input("How many tip you would like to offer: 10, 12, 15 or 20 %\n"))
num = int(input("Amongst how many people you wouild like to distribute the amount?"))
tip_percentage = tip/100.0
total_tip_amount = bill * tip_percentage
total_amount_payable = bill+total_tip_amount
bill_per_person = total_amount_payable/num

final_amount = "{:.2f}".format(bill_per_person)
print(f"The Final Payable amount is {final_amount}.")

