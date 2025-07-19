import random

class Hand:
    ## Left or Right
    name = "left"
    fingers = 1

    def __init__(self, name, fingers):
        self.name = name
        self.fingers = fingers
    
    def addFingers(self, amountToAdd):
        self.fingers += amountToAdd
    

class Person:
    leftHand = Hand("left",1)
    rightHand = Hand("right",1)
    is_human = True
    name = ''

    def __init__(self,leftHand,rightHand, name):
        self.leftHand = leftHand
        self.rightHand = rightHand
        self.name = name
        self.is_human = True
    
    def tap(self,hand,tappingHand):
        if(tappingHand.fingers + hand.fingers > 5):
            hand.fingers = (tappingHand.fingers + hand.fingers) % 5
        else:
            hand.addFingers(tappingHand.fingers)

    def split(self,handToSplit,gainingHand):
        addingFingers = round(handToSplit.fingers / 2)
        if gainingHand.fingers == 0 and handToSplit.fingers % 2 == 0:
            handToSplit.fingers -= addingFingers
            gainingHand.fingers += addingFingers
        else:
            print("can't split rn")
    
    def gameEnd(self) -> bool:
        if(self.leftHand.fingers == 0) and (self.rightHand.fingers == 0):
            return True
        
class AI(Person):
    def __init__(self,leftHand,rightHand,name):
        super().__init__(leftHand,rightHand,name)
        self.is_human = False
    
    def gameplay(self,human):
        if human.leftHand.fingers + self.leftHand.fingers == 5:
            self.tap(human.leftHand,self.leftHand)
        elif human.leftHand.fingers + self.rightHand.fingers == 5:
            self.tap(human.leftHand,self.rightHand)
        elif human.rightHand.fingers + self.rightHand.fingers == 5:
            self.tap(human.rightHand,self.rightHand)
        elif human.rightHand.fingers + self.leftHand.fingers == 5:
            self.tap(human.rightHand,self.leftHand)
        elif self.canSplit(self.leftHand,self.rightHand):
            self.split(self.leftHand,self.rightHand)
        elif self.canSplit(self.rightHand,self.leftHand):
            self.split(self.rightHand,self.leftHand)
        # else:
        #     if((self.leftHand.fingers + human.leftHand.fingers > self.leftHand.fingers + human.rightHand.fingers) or (self.leftHand.fingers + human.leftHand.fingers > self.rightHand.fingers + human.leftHand.fingers) or (self.leftHand.fingers + human.leftHand.fingers > self.rightHand.fingers + human.rightHand.fingers) and (self.leftHand.fingers != 0) and (human.leftHand.fingers != 0)):
        #         self.tap(human.leftHand,self.leftHand)
        #         print("left to left")
        #     elif((self.rightHand.fingers + human.leftHand.fingers > self.leftHand.fingers + human.rightHand.fingers) or (self.rightHand.fingers + human.leftHand.fingers > self.leftHand.fingers + human.leftHand.fingers) or (self.rightHand.fingers + human.leftHand.fingers > self.rightHand.fingers + human.rightHand.fingers) and (self.rightHand.fingers != 0) and (human.leftHand.fingers != 0)):
        #         self.tap(human.leftHand,self.rightHand)
        #         print("right to left")
        #     elif((self.rightHand.fingers + human.rightHand.fingers > self.leftHand.fingers + human.rightHand.fingers) or (self.rightHand.fingers + human.rightHand.fingers > self.leftHand.fingers + human.leftHand.fingers) or (self.rightHand.fingers + human.rightHand.fingers > self.rightHand.fingers + human.leftHand.fingers) and (self.rightHand.fingers != 0) and (human.rightHand.fingers != 0)):
        #         self.tap(human.rightHand,self.rightHand)
        #         print("right to right")
        #     elif((self.leftHand.fingers + human.rightHand.fingers > self.rightHand.fingers + human.leftHand.fingers) or (self.leftHand.fingers + human.rightHand.fingers >  self.leftHand.fingers + human.leftHand.fingers) or (self.leftHand.fingers + human.rightHand.fingers > self.rightHand.fingers + human.rightHand.fingers) and (self.leftHand.fingers != 0) and (human.rightHand.fingers != 0)):
        #         self.tap(human.rightHand,self.leftHand)
        #         print("left to right")
        else:
            choice = random.randint(1, 4)
            if (choice == 1) and (human.leftHand.fingers != 0) and (self.leftHand.fingers != 0):
                self.tap(human.leftHand,self.leftHand)
            elif (choice == 2) and (human.leftHand.fingers != 0) and (self.rightHand.fingers != 0):
                self.tap(human.leftHand,self.rightHand)
            elif (choice == 3) and (human.rightHand.fingers != 0) and (self.rightHand.fingers != 0):
                self.tap(human.rightHand,self.rightHand)
            elif (choice == 4) and (human.rightHand.fingers != 0) and (self.leftHand.fingers != 0):
                self.tap(human.rightHand,self.leftHand)
            else:
                choice = random.randint(1,4)
                self.gameplay(human)
                # print("NO good moves i guess")
        
    
    def canSplit(self,handToSplit,gainingHand) -> bool:
        if gainingHand.fingers == 0 and handToSplit.fingers % 2 == 0:
            return True
        



def game(player,other):
    if(player.leftHand.fingers == 5):
        player.leftHand.fingers = 0
    if(player.rightHand.fingers == 5):
        player.rightHand.fingers = 0
    print(f"\nCurrent Player ({player.name})'s left = {player.leftHand.fingers} right = {player.rightHand.fingers}")
    print(f"Opponent ({other.name})'s left = {other.leftHand.fingers} right = {other.rightHand.fingers}")
    action = ''
    handChoice = ''
    tapping = ''
    if(player.gameEnd() != True) and (other.gameEnd() != True):
        if player.is_human:
            action = input("Tap (t) or Split (s)")
            if(action == 't'):
                handChoice = input("Hand to Tap: Left hand (l) or Right hand (r)")
                if(handChoice == 'l'):
                    tapping = input("Tapping Hand: Left (l) or Right (r)")
                    if(tapping == 'l'):
                        other.tap(other.leftHand,player.leftHand) 
                        game(other,player)
                    elif(tapping == 'r'):
                        other.tap(other.leftHand,player.rightHand)
                        game(other,player)
                elif(handChoice == 'r'):
                    tapping = input("Tapping Hand: Left (l) or Right (r)")
                    if(tapping == 'l'):
                        other.tap(other.rightHand,player.leftHand)
                        game(other,player)
                    elif(tapping == 'r'):
                        other.tap(other.rightHand,player.rightHand)
                        game(other,player)
            elif(action == 's'):
                handChoice = input("Hand to Split: Left hand (l) or Right hand (r)")
                if(handChoice == 'l'):
                    player.split(player.leftHand,player.rightHand)
                    game(other,player)
                elif(handChoice == 'r'):
                    player.split(player.rightHand, player.leftHand)
                    game(other,player)
        else:
            player.gameplay(other)
            game(other,player)
    elif(other.gameEnd() == True):
        print(f"{player.name} is the winner!")
    else:
        print(f"{other.name} is the winner!")
        


    

def main():
    player1 = Person(Hand("left",1),Hand("right",1),"player1")
    player2 = AI(Hand("left",1),Hand("right",1),"AIplayer")

    start = random.randint(1,2)
    if (start == 1):
        game(player1,player2)
    else:
        game(player2,player1)



if __name__ == "__main__":
    main()

