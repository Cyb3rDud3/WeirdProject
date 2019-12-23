import sys
import traceback
import time
from random import randrange
import random
import re

file1 = open("age.txt", "a")
file2 = open("country.txt", "a")
file3 = open("phone.txt", "a")
file4 =open("first name.txt", "a")
file5 = open("last name.txt", "a")
## todo:: file.write (with open), for loop, while loop, lamdba func, http server, little gui, selenium, self class, self arg

def home():
    global country
    global phone
    country = input('where is your home town?' + '\n')
    phone = input('what is your phone?' + '\n')
    print('\n\n' + 'first name: ' + fname +'\n' + 'last name: ' + lname + '\n' + 'age: ' + str(age) + '\n' + 'country: ' + country + '\n' +'phone: ' + phone + '\n')
    file1.write('\n' + str(age) + '\n')
    file2.write('\n' + country + '\n')
    file3.write('\n' + phone + '\n')
    file4.write('\n' + fname + '\n')
    file5.write('\n' + lname + '\n')
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    return erandom()

def erandom():
   try:
      randomint = int(input('enter a number from 1 to 10: ' + '\n'))
      if (randomint > 10 or 0 > randomint):
      	print('you need to enter a number from 1 to 10!' + '\n')
      	return erandom()
      else:
      	print('great!')
      	randomint2 = int(input('enter another number from 1 to 10: ' + '\n'))
      if (randomint2 > 10 or 0 > randomint):
      	print('you need to enter a number from 1 to 10 only!' + '\n')
      	return erandom()
      else:
      	print('great! now i multiply your numbers...')
      	print('**************************************')
      	print('input1:' + str(randomint) + 'input2: ' + str(randomint2))
      	print(str(randomint) + '*' + str(randomint2) + "==")
      	print(randomint * randomint2)
      	print('**************************************')
      	print('done!...moving next.')
      	return bet()
   except ValueError:
      print('you need to enter numbers, not letters!')
      return erandom()    

def bet():
    try:
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print('you have list of numbers who pop randomly.')
        print(str(a))
        number = int(input('enter the number that you bet on popping next: ' + '\n'))
        if (number > 10 or 0 > number):
            print('you need to enter a number from 1 to 10 only!' + '\n')
            return bet()
        else:
            print('your bet is: ' + str(number))
            money = int(input('how much money do you bet on?'))
        if (money > 100 or money < 3):
            print('that is too much or not enough money! minimum bet is 3. ')
            return bet()
        else: 
            print('your bet:' + '\n')
            print('number: ' + str(number))
            print('amount of money: ' + str(money))
            print('starting bet.....')
            print('********************************')
            winumber = random.randrange(1, 10)
            print('winning number: ' + str(winumber))
            if winumber == number:
               print('holy shit! you won!')
               print('your money is * 10!')
               print(money * 10)
               print('that is your money now! ^^^^')
               return add()
            else:
               print('you didnt won')
               return add()
    except ValueError:
        print('you need to write numbers, not letters!')
        return bet()
    except:
        traceback.print_exc() 

def add():
    try:
        global az
        az = [1, 2, 3, 4, 5]
        print(str(az))
        number2 = int(input('enter number from 1 to 10 to add to this list: '))
        if (number2 > 10 or 0 > number2):
            print('you need to enter number from 1 to 10 only!')
            return add()
        else:
            az.append(int(number2))
            print(str(az))
            return remove()
    except ValueError:
        print('you need to write numbers. not letters!')
        return add()
    except:
        traceback.print_exc() 

def remove():
    try:
        print(str(az))
        number3 = int(input('enter number from 1 to 10 to remove from this list :'))
        if (number3 > 10 or 0 > number3):
            print('you need to enter number from 1 to 10 only!')
            return remove()
        else:
            az.remove(int(number3))
            print(str(az))
            return end()
    except ValueError:
        print('ValueError' + '\n' + 'you are maybe writting in letters instead of numbers?')
        print('or you just enterd key that does not exist.')
        return remove()
    except:
        traceback.print_exc() 


def wrong():
   sys.exit('oops! something gone wrong. this project is for humanes in the age 18 to 70 only!' + '\n')    

def error():
   try:
      an = input('enter y to start again. enter n to exit' + '\n')
      if an == 'y':
        return name()
      if an == 'n':
        sys.exit('exiting.....have a nice day!' + '\n')
      else:
        print('this is not a vaild input!' + '\n\n' + 'enter y for yes. enter n for no')

   except:
        traceback.print_exc() 

def end():
      print('we hope you enjoyed this weird ass project.')
      sys.exit        

def lenerror():
	sys.exit('no input.')


def name():
    try:
       global fname, lname
       global age
       fname = input('hello!' + '\n' + 'what is your first name?' + '\n')
       lname = input('great!' + '\n' + 'what is your last name?' + '\n')
       age = int(input('what is your age? write in numbers please.' + '\n'))
       if (age < 18 or age > 70):
           return wrong()
       else:
           return home()
    except ValueError:
        print('you need to write numbers! not letters!' + '\n')
        return error()
        
    except:
        traceback.print_exc()
name()

