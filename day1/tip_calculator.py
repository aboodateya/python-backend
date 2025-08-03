print("welcome to the Tip Calculator")

#input
bill = float(input("what is the total bill?"))
tip_percent=float(input("how much tip you like to give?"))
people=int(input("how many to split the bill between?"))

#calculation
tip_amount= (tip_percent / 100)*bill
total_bill=bill+tip_amount
eachperson=total_bill / people

print(f"each individual should pay:{eachperson:.2f} JD(including tip)")
