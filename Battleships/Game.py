from copy import deepcopy
class Game:

    def __init__(self, gameState, no1):
        self.__no1 = no1
        self.__gameState = gameState
        row = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        row1 = ['1', 0, 0, 0, 0, 0, 0, 0, 0]
        row2 = ['2', 0, 0, 0, 0, 0, 0, 0, 0]
        row3 = ['3', 0, 0, 0, 0, 0, 0, 0, 0]
        row4 = ['4', 0, 0, 0, 0, 0, 0, 0, 0]
        row5 = ['5', 0, 0, 0, 0, 0, 0, 0, 0]
        row6 = ['6', 0, 0, 0, 0, 0, 0, 0, 0]
        row7 = ['7', 0, 0, 0, 0, 0, 0, 0, 0]
        row8 = ['8', 0, 0, 0, 0, 0, 0, 0, 0]
        self.__board = [row, row1, row2, row3, row4, row5, row6, row7, row8]

    def getNo1(self):
        '''
        :return numbers of 1
        '''
        return self.__no1

    def setNo1(self, no1):
        '''
        sets the number of 1
        '''
        self.__no1 = no1

    def setGameState(self, gameState):
        '''
        :param gameState:
        '''
        self.__gameState = gameState

    def getGameState(self):
        '''
        return game state
        '''
        return self.__gameState

    def setPos(self, x, y, elem):
        '''
        :param x:
        :param y:
        :param elem:
        sets the elem on pos (x, y)
        '''
        copy = deepcopy(self.__board[x])
        copy[y] = elem
        self.__board[x] = copy

    def getPos(self, x, y):
        '''
        :param x:
        :param y:
        return elem on pos (x, y)
        '''
        return self.__board[x][y]

    def getBoard(self):
        '''
        :return board
        '''
        return self.__board

    def __str__(self):
        string = ""
        for list in self.__board:
            for elem in list:
                string += str(elem) + " "
            string += "\n"
        return string