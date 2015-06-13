import random

player_number = 77
random_number = 100

global_high = 101
global_low = 0

def compare(player_number,random_number):
    global global_high, global_low
    print "My guess is "+str(random_number)
    if random_number == player_number :
        print " Well thats my number "+str(random_number)
    elif random_number <= player_number:
        print "Choose Greater"
        print ""
        global_low = random_number + 1
        greater_number(global_high,global_low)
    elif random_number >= player_number:
        print "Choose Lesser"
        print ""
        global_high = random_number - 1
        lesser_number(global_high,global_low)      
    
def greater_number(high,low):
    global random_number
    random_number = random.randrange(low,high)
    #print "Ran Num in greater fun : "+str(random_number)
    compare(player_number,random_number)
    
def lesser_number(high,low):
    global random_number
    random_number = random.randrange(low,high)
    #print "Ran Num in lower fun : "+str(random_number)
    compare(player_number,random_number)
    
compare(player_number,random_number)
    
