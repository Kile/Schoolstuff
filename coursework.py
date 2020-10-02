#I am a programmar
#I am a programar
#I am a programer

#I make code

import time


airports = ['test']
otherairports = ['test2']

data = {
    "UKairport": '',
    "overseasairp": '',
    "airptype ": '',
    "nfirstcseat": '',
    "pfirstcseat": '',
    "pstandartcseat": ''

}

def menu():
  print('''(1) UK airport
(2) Overseas airport
(3) Type of aircrafts
(4) Number of first class seats
(5) Price of first class seat
(6) Price of standart class seat
(7) Reset values
(8) Exit\n''')
  value = input('What would you like to do? ')
  if not value.isdigit():
      print('Error, input must be a number, please re-enter')
      menu()
  else:
    if int(value) > 8 or int(value) <= 0:
      print('Number must be between 1 and 8')
      menu()
    else:   
      if int(value) == 8:
        print('''\n\n#################
        
Left the programm
Thanks for using Easy-Flight

#################\n\n''')
        return
      taskmanager(int(value))
#Decent code
option = menu()



def dealingwith1():
#working title
  value = input('Please enter the UK airpot (example: LON)\nTo cancel, insert \'cancel\'\n')
  
  if value in airports:
    data['UKairport']= value
    print(f'Answer {value} has been saved!\n')
    time.sleep(2)
    menu()
  elif value == 'cancel':
    print('Selection canceled\n')
    time.sleep(2)
    menu()
  else:
    print('Not valid argument, please re-enter\n')
    time.sleep(2)
    dealingwith1()

def dealingwith2():
#working title
  value = input('Please enter the overseas airpot (example: JFK)\nTo cancel, insert \'cancel\'\n')
  
  if value in otherairports:
    data['overseasairport']= value
    print(f'Answer {value} has been saved!\n')
    time.sleep(2)
    menu()
  elif value == 'cancel':
    print('Selection canceled\n')
    time.sleep(2)
    menu()
  else:
    print('Not valid argument, please re-enter\n')
    time.sleep(2)
    dealingwith1()


def taskmanager(task):
  if task == 1:
    #giving task to another function dealing with 1
    dealingwith1()
  if task == 2:
    #giving task to another function dealing with 2
    dealingwith2()
  if task == 3:
    #giving task to another function dealing with 3
    return
  if task == 4:
    #giving task to another function dealing with 4
    return
  if task == 5:
    #giving task to another function dealing with 5
    return
  if task == 6:
    #giving task to another function dealing with 5
    return
  if task == 7:
    #clearing the array
    return
    
