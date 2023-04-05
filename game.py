import random
javab = random.randint(1,99)
name = input('what is your name? ')
hads = input('what is your hads? ')
hads = int(hads)

while hads != javab:
    #print ('hads is' , type(hads) , ' and jaab is' , javab)
    if hads > javab:
        print ("mine is smaller")
    else:
        print ("mine is larger")
    hads = input('what is your hads? ') 
    hads = int(hads)
    
    print('wooooow' , name ,'you did it!')

