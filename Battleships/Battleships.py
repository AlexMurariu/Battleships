class Battleship:

    def __init__(self, y, x, battleshipType, direction):
        self.__positionX = x
        self.__positionY = y
        self.__type = battleshipType
        self.__direction = direction

    def __str__(self):
        string = str(self.__positionX) + " " + str(self.__positionY)
        if self.__type == 1:
            string += " patrol boat "
        elif self.__type == 2:
            string += " aircraft carrier "
        elif self.__type == 3:
            string += " armored warship "
        if self.__direction == 1:
            string += " up"
        elif self.__direction == 2:
            string += " right"
        elif self.__direction == 3:
            string += " down"
        elif self.__direction == 4:
            string += " left"
        return string

    def getPositionX(self):
        return self.__positionX

    def setPositionX(self, newPositionX):
        self.__positionX = newPositionX

    def getPositionY(self):
        return self.__positionY

    def setPositionY(self, newPositionY):
        self.__positionY = newPositionY

    def getType(self):
        return self.__type

    def setType(self, newType):
        self.__type = newType

    def getDirection(self):
        return self.__direction

    def setDirection(self, newDirection):
        self.__direction = newDirection