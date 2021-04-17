# importing sys to so that we can exit the code at some point
import sys
#welcoming the user to the atm

print("Hey, Welcome!")
#we would like to set up a 4-digit pin code

print("Choose a 4 digit pin code to setup your access!")
#input function to save the typed input from the user
pin=input()
#asking the user to confirm their pincode
print("please re-enter you pin")
invalidpin=0
i=0
while(i<3):
  confirmPin=input()
  if(pin==confirmPin):
    break
  if(pin!=confirmPin):
    print("pin does not match, enter again")
    invalidpin+=1
  if(invalidpin==3):
    print("Try again!")
    break
balance=5000
j = 0
while (j==0):
  options=["1.withdraw,2.deposit, 3.check balance, 4.exit"]
  print(options,"please selct 1-4")
  selectedOption=input()
  if(selectedOption=="1"):
    print("Enter withdraw amount")
    withdrawAmount=input()
    if(int(withdrawAmount)<=balance):
      balance=balance-int(withdrawAmount)
      print("your current balance is",balance)
    else:
       print("withdraw amount is more than the balance.")
  if(selectedOption=="2"):
    print("Enter amount to deposit")
    depositAmount=input()
    if(int(depositAmount)>10000):
      print("Sorry you can not deposit more than 10000")
    else:
      balance=balance+int(depositAmount)
  if(selectedOption=="3"):
    print("Your account balance is",balance)
  if(selectedOption=="4"):
    print("goodbye")
    sys.exit()
    
    
    





