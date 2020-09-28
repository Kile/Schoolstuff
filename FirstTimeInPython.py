
import random
from random import randint

a = [0, 0]
correctnumber = random.choice([1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15])


def optionfunktion(): 
  value = input('Insert a number between 1 and 15: ')
  if not value.isdigit():
    if value == 'stop':
      return 'stop'
    else:
      print('Error, input must be a number, please re-enter')
    optionfunktion()
  else:
    if int(value) > 15 or int(value) < 0:
      print('Number must be between 1 and 15')
      optionfunktion()
    else:   
      return int(value)
  
 
  
def function(correctorfailed):
    if correctorfailed != 'false':
        return [a[0]+1, a[1]+1]
    else:
        return [a[0]+1, a[1]]

option = optionfunktion()

while option != 'stop':

    if option == correctnumber:
     print('')
     print("Correct")
     a = function(a[1])
     print('')
     print('Total attempts:')
     print(a[0])
     print('Total correct attempts: ')
     print(a[1])
     option = optionfunktion()
     
    else:
     print('')
     print("Incorrect")
     a = function('false')
     print('')
     print('Total attempts:')
     print(a[0])
     print('Total correct attempts: ')
     print(a[1])
     option = optionfunktion()
