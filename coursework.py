import time

results = ''
airports = ['LPL', 'BOH']
otherairports = ['JFK', 'ORY', 'MAD', 'AMS', 'CAI']
airplanetypes = ['medium narrow body', 'large narrow body', 'medium wide body']

data = {
    "UKairport": '',
    "overseasairp": '',
    "airptype": '',
    "nfirstcseat": '',
    "pfirstcseat": '',
    "pstandartcseat": ''

}

distance = {
    'JFK': {
        'LPL': 5326,
        'BOH': 5486
    },
    'ORY': {
        'LPL': 629,
        'BOH': 379
    },
    'MAD': {
        'LPL': 1428,
        'BOH': 1151
    },
    'AMS': {
        'LPL': 526,
        'BOH': 489
    },
    'CAI': {
        'LPL': 3779,
        'BOH': 3584
    }
}

airplaneinfo = {
    'medium narrow body': {
        'maxrange': 2650,
        'costpseat100km': 8,
        'capacity': 180,
        'minimumfseats': 8
    },
    'large narrow body': {
        'maxrange': 5600,
        'costpseat100km': 7,
        'capacity': 220,
        'minimumfseats': 10
    },
    'medium wide body': {
        'maxrange': 4050,
        'costpseat100km': 5,
        'capacity': 406,
        'minimumfseats': 14
    },

}

def checkingresults():
  
  val1 = data['UKairport']
  val2 = data['overseasairp']
  val3 = data['airptype']
  val4 = data['nfirstcseat']
  results = [val1, val2, val3, val4]
  if '' in results:
    return False
  else:
    d = distance[val2]
    reald = d[val1]
    airp = airplaneinfo[val3]
    planecapability = airp['maxrange']
    if reald > planecapability:
      return False
    else:
      return True

def calculatingresults():
  airtype = airplaneinfo[data['airptype']]
  airportov = distance[data['overseasairp']] 
  nstandartseats = airtype['capacity'] - int(data['nfirstcseat']) * 2

  priceperseat = airtype['costpseat100km'] * (airportov[data['UKairport']]/100)
  totalcost = priceperseat * (nstandartseats + int(data['nfirstcseat']))
  totalincome = int(data['nfirstcseat']) * int(data['pfirstcseat']) + (airtype['capacity'] - int(data['nfirstcseat'])*2) * int(data['pstandartcseat'])
  totalprofit = totalincome - totalcost

  print(f'''#### RESULTS ####
  
  Price per seat: {priceperseat}£
  Total cost: {totalcost}£
  Total income: {totalincome}£
  Total profit {totalprofit}£
  
#################
''')
  clearvalues()
  menu()



def dealingwith1():
#working title
  value = input('Please enter the UK airpot (example: LPL)\nTo cancel, insert \'cancel\'\n')
  
  if value.upper() in airports:
    data['UKairport']= value.upper()
    print(f'Answer {value} has been saved!\n')
    dealingwith2()
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
  
  if value.upper() in otherairports:
    data['overseasairp']= value.upper()
    print(f'Answer {value} has been saved!\n')
    
    time.sleep(2)
    menu()
  elif value == 'cancel':
    print('Selection canceled\n')
    data['UKairport'] = ''
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
    time.sleep(2)
    dealingwith4()
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
      data['airptype'] = ''
      menu()
    else:
      print('Error, input must be a number, please re-enter')
      time.sleep(2)
      dealingwith4()
  else:
    plane = airplaneinfo[data['airptype']]

    maxseats = plane['capacity']
    if int(value) > int(maxseats) or int(value) <= 0:
      print(f'Number must be not greater than {maxseats} and greater than 0\n')
      time.sleep(2)
      dealingwith4()
    else:   
      data['nfirstcseat']= value
      print(f'Answer {value} has been saved!\n')
      time.sleep(2)
      menu()
      
def dealingwith5():
#working title
  check = checkingresults
  if check is False:
    print('\nYou have not entered every data or an airplane that is not capable of flying from given airports, use the clear option to restart\n')
    return menu()
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
    if int(value) > 10000 or int(value) <= 0:
      #Note: change numbers
      print('Number must be between 0 and 10000\n')
      time.sleep(2)
      dealingwith5()
    else:   
      data['pfirstcseat'] = value
      print(f'Answer {value} has been saved!\n')
      dealingwith6()
      
      
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
    if int(value) > 10000 or int(value) <= 0:
      #Note: change numbers
      print('Number must be between 1 and 10000\n')
      time.sleep(2)
      dealingwith6()
    else:   
      data['pstandartcseat']= value
      print(f'Answer {value} has been saved!\n')
 
      checkingresults()
      calculatingresults()


def clearvalues():
  data['airptype'] = ''
  data['nfirstcseat'] = ''
  data['overseasairp'] = ''
  data['pfirstcseat'] = ''
  data['pstandartcseat'] = ''
  data['UKairport'] = ''


def taskmanager(task):
  if task == 1:
    #giving task to another function dealing with 1
    dealingwith1()
  if task == 2:
    #giving task to another function dealing with 2
    dealingwith3()
  if task == 3:
    #giving task to another function dealing with 3
    dealingwith5()
  if task == 4:
    clearvalues()
    print('Cleared values\n')
    print(data)
    time.sleep(2)
    menu()
    

def menu():
  print('''(1) Enter airport details
(2) Enter flight details
(3) Enter price details and calculate profit
(4) Reset values
(5) Exit\n''')
  value = input('What would you like to do? ')
  if not value.isdigit():
      print('Error, input must be a number, please re-enter')
      menu()
  else:
    if int(value) > 5 or int(value) <= 0:
      print('Number must be between 1 and 5')
      menu()
    else:   
      if int(value) == 5:
        print('''\n\n#################
        
Left the programm
Thanks for using Easy-Flight

#################\n\n''')
        return
      taskmanager(int(value))




option = menu()
