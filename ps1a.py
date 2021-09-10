#Problem 1
# Name: Utpana
# Time spend:3 hours

#Problem 1
# Write a program to calculate the credit card balance after one year if a person only pays the
# minimum monthly payment required by the credit card company each month. 


outstanding_balance = int(input("Enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the annual credit card interest rate as a decimal: ")) # declare and define variables and get input from user
monthly_payment_rate= float(input("Enter the minimum monthly payment rate as a decimal: "))

months = 12
amount = 0
for i in range (0,12):
    print("Month",i+1)
    
    minimum_monthly_payment = monthly_payment_rate * outstanding_balance
    
    interest_paid = interest_rate/months*outstanding_balance
    
    principal_paid = minimum_monthly_payment - interest_paid

    
    remaining_balance = outstanding_balance - principal_paid
    outstanding_balance = remaining_balance
    amount += minimum_monthly_payment
    print("Minimum monthly payment: Rs.",round(minimum_monthly_payment,2))
    print("Principal Paid: Rs.",round(principal_paid,2))
    print("Remaining balance: Rs.",round(remaining_balance,2))
  
print("RESULT")
print("Total amount paid: Rs.",format(amount,".2f"))
print("Remaining balance: Rs.",format(remaining_balance,".2f"))
