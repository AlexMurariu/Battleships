class MenuException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class GameValidator:

    @staticmethod
    def validateBattleship(board, battleship):
        x = int(battleship.getPositionX())
        y = int(battleship.getPositionY())
        if int(battleship.getType()) == 1:
            if int(battleship.getDirection()) == 1:
                squares = 0
                while squares < 2:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x -= 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 2:
                squares = 0
                while squares < 2:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 3:
                squares = 0
                while squares < 2:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 4:
                squares = 0
                while squares < 2:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y -= 1
                        else:
                            return False
                    squares += 1
        elif int(battleship.getType()) == 2:
            if int(battleship.getDirection()) == 1:
                squares = 0
                while squares < 3:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x -= 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 2:
                squares = 0
                while squares < 3:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 3:
                squares = 0
                while squares < 3:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 4:
                squares = 0
                while squares < 3:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y -= 1
                        else:
                            return False
                    squares += 1
        elif int(battleship.getType()) == 3:
            if int(battleship.getDirection()) == 1:
                squares = 0
                while squares < 4:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x -= 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 2:
                squares = 0
                while squares < 4:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 3:
                squares = 0
                while squares < 4:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            x += 1
                        else:
                            return False
                    squares += 1
            elif int(battleship.getDirection()) == 4:
                squares = 0
                while squares < 4:
                    if (x < 1 or x > 8) or (y < 1 or y > 8):
                        return False
                    else:
                        if board.getPos(x, y) == 0:
                            y -= 1
                        else:
                            return False
                    squares += 1
        return True
