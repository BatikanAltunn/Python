import time
import random
import datetime
import sys
balance = random.randint(100,1000)
activity = []
date = str(datetime.date.today())
def dotCounter(msg,wait):
  for dotcount in range(2):
      print(str(msg) + dotcount * "." )
      time.sleep(wait)

def deposit():

  global balance

  cash = input("Enter the amont of money: ")

  try:
    cash = float(cash)

  except ValueError:
    print ("Please enter a valid amount.")
    deposit()

  if cash <= 0:
    print("Amount must be positive.")
    time.sleep(2)
    deposit()

  balance += cash

  print ("You succesfully deposited " + str(cash))
  time.sleep(3)

  timeStamp = time.time()
  printableTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%H:%M')
  activity.append(str(printableTimeStamp) + "   Deposit      " + str(cash))

  dotCounter("Returning to menu",1)

def withdraw(balance):
  
  print("Balance  £  ",balance)
  Withdraw=float(input("Enter Withdraw amount £ "))
  if Withdraw>0 and Withdraw< balance:
     balance=(balance-Withdraw)
     print("Foreward Balance  £ ",balance)
  elif Withdraw>balance or Withdraw==balance:
     print("No funds in account")
  else:
     print("None withdraw made")
  return balance
    
  timeStamp = time.time()
  printableTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%H:%M')
  activity.append(str(printableTimeStamp) + "   Withdrawal   " + str(withdraw))

  dotCounter("Returning back to menu",1)

def inquiry():
  global balance

  if balance < 0:
    print("Balance:" , end= "")

  elif balance > 0:
    print("Balance:" , end= "")

  else:
    print ("Balance: " , balance)

  wait = input("\nPress Enter to continue.")
  dotCounter("Returning back to menu",0.4)

def checkActivity():

  timeStamp = time.time()
  printableTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%d/%m/%Y')
  print(printableTimeStamp)

  for action in activity:
    print (action)

  wait = input("Press enter to return to the menu.")
  dotCounter("Returning back to menu",0.3)

def login(pin_code = 0000, tries = 3, current_try = 0):
  print ("~~~Options~~~")
  print("1) Log in")
  print("2) Exit")
  choice = input()

  if not (choice <= "2" and choice >= "1"):
    print("Please enter a valid option.")
    time.sleep(2)
    login()

  if choice == "2":
    sys.exit("Thank you for using ATM Simulator.")

  while tries > 0:
    current_try = (input("Enter pin code:"))

    try:
      current_try = int(current_try)

    except ValueError:
      print("Pleasee enter an integer.")
      login()

    if current_try == pin_code:
      time.sleep(0.5)
      time.sleep(3)
      return None

    else:
      tries -= 1
      if (tries != 1):
        print ("You have " + str(tries) + " tries left.")
        if (tries == 0):

          time.sleep(0.5)
          time.sleep(15)
          login()

      else:
        print ("You have 1 try left.")

def menu():
  print("~~~Menu~~~")
  print("1) Deposit Money")
  print("2) Withdraw Money")
  print("3) Inquire Balance")
  print("4) Show Activity")
  print("5) Log Out")

  choice = input()

  if not choice <= "5" and choice >= "1":
    print("Please enter a valid option.")
    time.sleep(2)
    menu()

  if choice == "1":
    deposit()

  elif choice == "2":
    withdraw(balance)

  elif choice == "3":
    inquiry()

  elif choice == "4":
    checkActivity()

  elif choice == "5":
    login()

  menu()

dotCounter("Please wait.\nLoading",1.1)
login()
menu()




