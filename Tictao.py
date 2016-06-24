def is_full():
    for i in range(1,10):
        if onboard[i] =='':
            return False
    return True

def Judge(onboard,player):
    return((onboard[7]==player1 and onboard[8]==player and onboard[9]==player)  or
     (onboard[4]==player1 and onboard[5]==player and onboard[6]==player) or
     (onboard[1]==player1 and onboard[2]==player and onboard[3]==player) or
     (onboard[7]==player1 and onboard[4]==player and onboard[1]==player) or
     (onboard[8]==player1 and onboard[5]==player and onboard[2]==player) or
     (onboard[9]==player1 and onboard[6]==player and onboard[3]==player) or
     (onboard[7]==player1 and onboard[5]==player and onboard[3]==player) or
     (onboard[9]==player1 and onboard[5]==player and onboard[1]==player))
print 'Welcome'    
#who will be first
onboard =['']*10
player1 = raw_input('Please enter your choice either X or O:')
if player1 == 'X':
    player2 ='O'
elif player1 =='O':
    player2 ='X'
#while player1 !='X' or 'O':
#    if player1 == 'X':
#        player2 ='O'
#    elif player1 =='O':
#        player2 ='X'

full = False
#Lets start the game:
#Player 1 starts : Give your location where you want to put? onboard[1-9] 
while full is False:
    mark = raw_input('Player1:Enter the location :')
    mark = int(mark)
    if onboard[mark] =='':
        onboard[mark]=player1
    else :
        print('It is already filled,enter a right position')
        continue
#Check for the result
    if Judge(onboard,player1):
        full = True
        print'Congralutions,you have won!'
        break
#First check if it full
    if is_full():
        full=True
        print 'It is a tie'
        break

    #Player2
    mark = raw_input('Player2:Enter the location :')
    mark = int(mark)
    if onboard[mark] =='':
        onboard[mark]=player2
    else :
        print('It is already filled,enter a right position')
        continue
#Check for the result
    if Judge(onboard,player2):
        full = True
        print'Congralutions,you have won!'
        break
#First check if it full
    if is_full():
        full=True
        print'It is a tie'
        break



        
        
        
        
    
    

        


     


   