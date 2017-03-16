
from sys import maxsize as inf

class GameTree(object):
    def __init__(self, depth, playerNum, sticks, value = 0):
        self.depth = depth
        self.playerNum = playerNum
        self.sticks = sticks
        self.value = value
        self.children = []
        if sticks > 0:
            self.generateChildren()
    
    def generateChildren(self):
        if self.depth >= 0:
            for i in range(1, 3):
                s = self.sticks - i
                v = self.gameValue(s)
                subtree = GameTree(self.depth - 1, -(self.playerNum), s, v)
                self.children.append(subtree)
    
    def gameValue(self, value):
        if value == 0:
            return inf * self.playerNum
        elif value < 0:
            return inf * -(self.playerNum)
        else:
            return 0




'''
    Minimax algorithm for n-sticks game.
    tree -- an initialized game tree.
    depth -- max depth that should be calculated.
    playerNum -- players number. 1 or -1.
'''
def minimax(tree, depth, playerNum):
    if depth == 0 or abs(tree.value) == inf:
        return tree.value
    
    bestVal = inf * -(playerNum)
    
    for child in tree.children:
        val = minimax(child, depth - 1, -(playerNum))
        goal = inf * playerNum
        if abs(goal - val) < abs(goal - bestVal):
            bestVal = val
    
    return bestVal




def winCheck(sticks, playerNum):
    if sticks <= 0:
        pass
        if playerNum > 0:
            if sticks == 0:
                print("    Player 1 wins.")
            else:
                print("    Player 2 (AI) wins.")
        else:
            if sticks == 0:
                print("    Player 2 (AI) wins.")
            else:
                print("    Player 1 wins.")
        return 0
    else:
        return 1




def safeIntCast(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default




if __name__ == '__main__':
    sticks = 11
    depth = 100
    curPlayer = 1
    cont = False
    intro = """
N-Sticks Game
    Instructions:
    To win, be the player that picks up the last stick.
    You may only pick up 1 or 2 sticks each turn.
    You are player 1 and will go first.
    """
    
    print(intro)
    
    while sticks > 0:
        while not cont:
            print("%d sticks remain. How many do you take?" % sticks)
            choice = safeIntCast(input("1 or 2: "))
            
            if (choice == 1 or choice == 2) and (sticks - choice >= 0):
                cont = True
            else:
                print("Invalid input.")
        
        sticks -= choice
        cont = False
        print("Player 1 takes %d sticks." % choice)
        
        if winCheck(sticks, curPlayer):
            curPlayer *= -1
            tree = GameTree(depth, curPlayer, sticks)
            bestChoice = 1
            bestVal = -(curPlayer) * inf
            
            for i in range(len(tree.children)):
                child = tree.children[i]
                val = minimax(child, depth, -(curPlayer))
                goal = inf * curPlayer
                if abs(goal - val) < abs(goal - bestVal):
                    bestVal = val
                    bestChoice = i
            
            bestChoice += 1
            print("Player 2 takes %d sticks based on heuristic value %d." % (bestChoice, bestVal))
            sticks -= bestChoice
            winCheck(sticks, curPlayer)
            curPlayer *= -1
    print("Game over.")
    

