#I am a programmar
#I am a programar
#I am a programer

#I make code

import time


airports = ['test']
otherairports = ['test2']
airplanetypes = ['medium narrow body', 'large narrow body', 'medium wide body']

data = {
    "UKairport": '',
    "overseasairp": '',
    "airptype": '',
    "nfirstcseat": '',
    "pfirstcseat": '',
    "pstandartcseat": ''

}


def checkingresults():
  

  val1 = data['UKairport']
  val2 = data['overseasairp']
  val3 = data['airptype']
  val4 = data['nfirstcseat']
  val5 = data['pfirstcseat']
  val6 = data['pstandartcseat']
  results = [val1, val2, val3, val4, val5, val6]
  print(results)
  if '' in results:
    return False
  else:
    return True





def dealingwith1():
#working title
  value = input('Please enter the UK airpot (example: LON)\nTo cancel, insert \'cancel\'\n')
  
  if value.lower() in airports:
    data['UKairport']= value.upper()
    print(f'Answer {value} has been saved!\n')
    complete = checkingresults()
    if complete is True:
      #do some calculations and give the result but for now:
      print('Complete!')
    else:
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
  
  if value.lower() in otherairports:
    data['overseasairp']= value.upper()
    print(f'Answer {value} has been saved!\n')
    complete = checkingresults()
    if complete is True:
      #do some calculations and give the result but for now:
      print('Complete!')
    else:
      time.sleep(2)
      menu()
  elif value == 'cancel':
    print('Selection canceled\n')
    time.sleep(2)
    menu()
  else:
    print('Not valid argument, please re-enter\n')
    time.sleep(2)
    dealingwith2()

def dealingwith3():
#working title
  value = input('Please enter the type of aircraft (example: medium narrow body)\nTo cancel, insert \'cancel\'\n')
  
  if value.lower() in airplanetypes:
    data['airptype']= value.lower()
    print(f'Answer {value} has been saved!\n')
    complete = checkingresults()
    if complete is True:
      #do some calculations and give the result but for now:
      print('Complete!')
    else:
      time.sleep(2)
      menu()
  elif value == 'cancel':
    print('Selection canceled\n')
    time.sleep(2)
    menu()
  else:
    print('Not valid argument, please re-enter\n')
    time.sleep(2)
    dealingwith3()

def dealingwith4():
#working title
  
  value = input('How many first class seats does the airplane have?\nTo cancel, insert \'cancel\'\n')
  if not value.isdigit():
    if value == 'cancel':
      print('Selection canceled\n')
      time.sleep(2)
      menu()
    else:
      print('Error, input must be a number, please re-enter')
      time.sleep(2)
      dealingwith4()
  else:
    if int(value) > 8 or int(value) <= 0:
      #Note: change numbers
      print('Number must be between 1 and 8\n')
      time.sleep(2)
      dealingwith4()
    else:   
      data['nfirstcseat']= value
      print(f'Answer {value} has been saved!\n')
      complete = checkingresults()
      if complete is True:
        #do some calculations and give the result but for now:
        print('Complete!')
      else:
        time.sleep(2)
        menu()
      
def dealingwith5():
#working title
  
  value = input('What does a first class seat cost?\nTo cancel, insert \'cancel\'\n')
  if not value.isdigit():
    if value == 'cancel':
      print('Selection canceled\n')
      time.sleep(2)
      menu()
    else:
      print('Error, input must be a number, please re-enter')
      time.sleep(2)
      dealingwith5()
  else:
    if int(value) > 8 or int(value) <= 0:
      #Note: change numbers
      print('Number must be between 1 and 8\n')
      time.sleep(2)
      dealingwith5()
    else:   
      data['pfirstcseat'] = value
      print(f'Answer {value} has been saved!\n')
      complete = checkingresults()
      if complete is True:
        #do some calculations and give the result but for now:
       print('Complete!')
      else:
        time.sleep(2)
        menu()
      
def dealingwith6():
#working title
  
  value = input('What does a standart class seat cost?\nTo cancel, insert \'cancel\'\n')
  if not value.isdigit():
    if value == 'cancel':
      print('Selection canceled\n')
      time.sleep(2)
      menu()
    else:
      print('Error, input must be a number, please re-enter')
      time.sleep(2)
      dealingwith6()
  else:
    if int(value) > 8 or int(value) <= 0:
      #Note: change numbers
      print('Number must be between 1 and 8\n')
      time.sleep(2)
      dealingwith6()
    else:   
      data['pstandartcseat']= value
      print(f'Answer {value} has been saved!\n')
      complete = checkingresults()
      if complete is True:
        #do some calculations and give the result but for now:
        print('Complete!')
      else:
        time.sleep(2)
        menu()

def taskmanager(task):
  if task == 1:
    #giving task to another function dealing with 1
    dealingwith1()
  if task == 2:
    #giving task to another function dealing with 2
    dealingwith2()
  if task == 3:
    #giving task to another function dealing with 3
    dealingwith3()
  if task == 4:
    #giving task to another function dealing with 4
    dealingwith4()
  if task == 5:
    #giving task to another function dealing with 5
    dealingwith5()
  if task == 6:
    #giving task to another function dealing with 5
    dealingwith6()
  if task == 7:
    #clearing the array
    data.fromkeys(data, '')
    print('Cleared values\n')
    time.sleep(2)
    menu()
    

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




option = menu()


