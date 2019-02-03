from GameValidators import GameValidator

class Player:

    def __init__(self, turn, game):
        self.__validator = GameValidator
        self.__turn = turn
        self.__game = game

    def addBattleship(self, board, battleship, battleshipList):
        '''
        :param board:
        :param battleship:
        :param battleshipList:
        :return True if battleship can be added or False if not
        '''
        for elem in battleshipList:
            if elem == battleship.getType():
                return False

        battleshipList.append(battleship.getType())
        x = int(battleship.getPositionX())
        y = int(battleship.getPositionY())
        if self.__validator.validateBattleship(board, battleship) == True:
            if int(battleship.getType()) == 1:
                if int(battleship.getDirection()) == 1:
                    squares = 0
                    while squares < 2:
                        board.setPos(x, y, 1)
                        x -= 1
                        squares += 1
                elif int(battleship.getDirection()) == 2:
                    squares = 0
                    while squares < 2:
                        board.setPos(x, y, 1)
                        y += 1
                        squares += 1
                elif int(battleship.getDirection()) == 3:
                    squares = 0
                    while squares < 2:
                        board.setPos(x, y, 1)
                        x += 1
                        squares += 1
                elif int(battleship.getDirection()) == 4:
                    squares = 0
                    while squares < 2:
                        board.setPos(x, y, 1)
                        y -= 1
                        squares += 1
            elif int(battleship.getType()) == 2:
                if int(battleship.getDirection()) == 1:
                    squares = 0
                    while squares < 3:
                        board.setPos(x, y, 1)
                        x -= 1
                        squares += 1
                elif int(battleship.getDirection()) == 2:
                    squares = 0
                    while squares < 3:
                        board.setPos(x, y, 1)
                        y += 1
                        squares += 1
                elif int(battleship.getDirection()) == 3:
                    squares = 0
                    while squares < 3:
                        board.setPos(x, y, 1)
                        x += 1
                        squares += 1
                elif int(battleship.getDirection()) == 4:
                    squares = 0
                    while squares < 3:
                        board.setPos(x, y, 1)
                        y -= 1
                        squares += 1
            elif int(battleship.getType()) == 3:
                if int(battleship.getDirection()) == 1:
                    squares = 0
                    while squares < 4:
                        board.setPos(x, y, 1)
                        x -= 1
                        squares += 1
                elif int(battleship.getDirection()) == 2:
                    squares = 0
                    while squares < 4:
                        board.setPos(x, y, 1)
                        y += 1
                        squares += 1
                elif int(battleship.getDirection()) == 3:
                    squares = 0
                    while squares < 4:
                        board.setPos(x, y, 1)
                        x += 1
                        squares += 1
                elif int(battleship.getDirection()) == 4:
                    squares = 0
                    while squares < 4:
                        board.setPos(x, y, 1)
                        y -= 1
                        squares += 1

            return True
        else:
            battleshipList.pop()
            return False

    def hit(self, x, y, boardObj, copyBoardObj, board):
        '''
        :param x:
        :param y:
        :param boardObj:
        :param copyBoardObj:
        :param board:
        :return -4, -4 if hit outside, -1, -1 if hit water, -2, -2 if hit an already hit zone
        '''
        if x >= 1 or x <= 8 and y >= 1 or y <= 8:
            if board.getBoard()[y][x] == 0:
                boardObj.setPos(y, x, 2)
                copyBoardObj.setPos(y, x, 2)
                return [-2, -2]
            elif board.getBoard()[y][x] == 1:
                boardObj.setPos(y, x, 3)
                copyBoardObj.setPos(y, x, 3)
                boardObj.setNo1(boardObj.getNo1() - 1)
                return [x, y]
            else:
                return [-1, -1]
        else:
            return [-4, -4]

    def rotateHit(self, x, y, boardObj, board, uselessBoard, directionList):
        '''
        :param x:
        :param y:
        :param boardObj:
        :param board:
        :param uselessBoard:
        :param directionList:
        :return the new position of x and y if you hit a boat or the same x and y, and a direction list
        '''
        copieX = x
        copieY = y
        if directionList == [1, 1, 1, 1]:
            return [-3, -3, directionList]
        else:
            if directionList[0] == 0:
                y -= 1
                if y >= 1 or y <= 8:
                    hitBox = self.hit(x, y, boardObj, uselessBoard, board)
                    if hitBox == [-1, -1]:
                        directionList[0] = 1
                        return [copieX, copieY, directionList]
                    elif hitBox == [-2, -2]:
                        directionList[0] = 1
                        return [copieX, copieY, directionList]
                    else:
                        return [x, y, directionList]
                else:
                    directionList[0] = 1
                    return [copieX, copieY, directionList]
            elif directionList[1] == 0:
                x += 1
                if x >= 1 or x <= 8:
                    hitBox = self.hit(x, y, boardObj, uselessBoard, board)
                    if hitBox == [-1, -1]:
                        directionList[1] = 1
                        return [copieX, copieY, directionList]
                    elif hitBox == [-2, -2]:
                        directionList[1] = 1
                        return [copieX, copieY, directionList]
                    else:
                        return [x, y, directionList]
                else:
                    directionList[1] = 1
                    return [copieX, copieY, directionList]
            elif directionList[2] == 0:
                y += 1
                if y >= 1 or y <= 8:
                    hitBox = self.hit(x, y, boardObj, uselessBoard, board)
                    if hitBox == [-1, -1]:
                        directionList[2] = 1
                        return [copieX, copieY, directionList]
                    elif hitBox == [-2, -2]:
                        directionList[2] = 1
                        return [copieX, copieY, directionList]
                    else:
                        return [x, y, directionList]
                else:
                    directionList[2] = 1
                    return [copieX, copieY, directionList]
            elif directionList[3] == 0:
                x -= 1
                if x >= 1 or x <= 8:
                    hitBox = self.hit(x, y, boardObj, uselessBoard, board)
                    if hitBox == [-1, -1]:
                        directionList[3] = 11
                        return [copieX, copieY, directionList]
                    elif hitBox == [-2, -2]:
                        directionList[3] = 1
                        return [copieX, copieY, directionList]
                    else:
                        return [x, y, directionList]
                else:
                    directionList[3] = 1
                    return [copieX, copieY, directionList]