
a = [0, 0]


def optionfunktion(): 
    return (input('Insert your option '))
    

def function(menustate, correctorfailed):
    if correctorfailed != 'false':
        return [a[0]+1, a[1]+1]
    else:
        return [a[0]+1, a[1]]

option = optionfunktion()

while option != 'stop':

    if option == 1:
     print('')
     print("Correct")
     a = function(a[0], a[1])
     print('')
     print('total attempts:')
     print(a[0])
     print('total correct attempts ')
     print(a[1])
     option = optionfunktion()
     
    else:
     print('')
     print("Incorrect")
     a = function(a[0], 'false')
     print('')
     print('total attempts:')
     print(a[0])
     print('total correct attempts ')
     print(a[1])
     option = optionfunktion()

