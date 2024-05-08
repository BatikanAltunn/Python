from termcolor import cprint
print("Calculator")
print("-----------")
while True:
 num1 = input("Enter a number: ")
 if not num1:
   break
 try:
   num1 = float(num1)
 except ValueError:
   print("Geçersiz sayı")
   continue
 num2 = input("Enter another Number: ")
 if not num2:
   break
 try:
   num2 = float(num2)
 except ValueError:
   print("Geçersiz sayı")
   break
     

 print("choose Operator:")
 print("1) + ")
 print("2) - ")
 print("3) / ")
 print("4) x ")

 choice = input()

 if choice == "1" :
   result = float(num1) + float(num2)
   print("Your Answer is : " + str(result))

 elif choice == "2" :
   result = float(num1) - float(num2)
   print("Your Answer is : " + str(result))
 
 elif choice == "3" :
   result = float(num1) / float(num2)
   print("Your Answer is : " + str(result))
   try:
     num2 == 0
   except ValueError:
     print ("HATA")
 elif choice == "4" :
   result = float(num1) * float(num2)
   print("Your Answer is : " + str(result))
 break
