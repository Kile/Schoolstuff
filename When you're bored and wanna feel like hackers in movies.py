######################################################################
'''
This is designed to be used in a python shell, it looks like
the unrealisti hollywood hacker scenes where just random text in
random lenght is constantly printed. So while bored in computer science
class I let this run in the background to feel productive.
Idk, feel free to use it when you're bored as well
'''
########################################################################




import random
import time
#for optional use if you actually wanna read what happens

x = 1
c = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v', 'b','n','m', 1,2,3,4,5,6,7,8,9,10]
#A list of possible characters to output

#The actual code. If you are in a python shell you will have to define x and c
#before and import before all in one line
while x != 100000:
    l = random.randint(5,50)
    #How big you want the output to be per line
    r =[]
    while l != 0:
        r.append(random.choice(c))
        #puts a random character from our c list in the list that will be printed
        #l times
        l = l-1
    print(*r, sep='')
    #prints the list in a readable format
    #time.sleep(0.02)
    #Commented that out since I prefer it faster, you can use that though
    #for slower output
    x = x+1
