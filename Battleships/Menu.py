from Validators import *
from Battleships import Battleship
from Game import Game

import random

class Menu:

    def __init__(self, you, opponent, yourBoard, opponentBoard):
        self.__you = you
        self.__opponent = opponent
        self.__yourBoard = yourBoard
        self.__opponentBoard = opponentBoard
        self.__validator = MenuValidator()

    def show(self):

        print("                  Menu               \n")
        print("              Start Game(1)            ")
        print("                 Help(2)               ")
        print("                 Exit(3)               ")

    def help(self):
        print("This it the battleship game. A strategy game where you will be given two 8X8 boards, one for you")
        print("and one for your opponent. The goal of the game is to destroy all of your opponent's battleships.")
        print("At the start of the game you will be able to place your battleships anywhere on the board. You have")
        print("to choose between three types of battleships, a patrol boat made by two squares, an aircraft carrier")
        print("made by three squares and an armored warship made by four squares. In order to win the game you have")
        print("destroy, which means to hit every part of the battleship, all enemy battleships.\n")
        print("Map knowledge: 0 - water, 1 - your battleships, 2 - missed, 3 - hit")

    def convert(self, letter):
        if letter < 'A' or letter > 'H':
            return -1
        letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for index  in range(len(letterList)):
            if letter == letterList[index]:
                return index + 1

    def startTurnPlayer(self):
        arrangements = 3
        battleshipList = []
        while arrangements > 0:
            print("Opponent's board")
            print(self.__opponentBoard)
            print("Your board")
            print(self.__yourBoard)
            while True:
                try:
                    positionX = self.convert(input("Give the x position:"))
                    self.__validator.validatePosition(positionX)
                    positionY = input("Give the y position:")
                    self.__validator.validatePosition(positionY)
                    battleshipType = input("Choose battleship:")
                    self.__validator.validateType(battleshipType)
                    direction = input("Choose direction:")
                    self.__validator.validateDirection(direction)
                    battleship = Battleship(positionX, positionY, battleshipType, direction)
                    if self.__you.addBattleship(self.__yourBoard, battleship, battleshipList) == False:
                        print("Invalid arrangement!")
                        break
                    else:
                        arrangements -= 1
                        break
                except MenuException as exc:
                    print(str(exc))
                    break

        print("Opponent's board")
        print(self.__opponentBoard)
        print("Your board")
        print(self.__yourBoard)

    def startTurnOpponent(self, copyBoard):

        posListX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        posListY = [1, 2, 3, 4, 5, 6, 7, 8]
        battleshipList = [1, 2, 3]
        directionList = [1, 2, 3, 4]
        pick = random.SystemRandom()
        battleShipList = []
        arrangements = 3

        while arrangements > 0:
            while True:
                try:
                    positionX = self.convert(pick.choice(posListX))
                    self.__validator.validatePosition(positionX)
                    positionY = pick.choice(posListY)
                    self.__validator.validatePosition(positionY)
                    battleship = pick.choice(battleshipList)
                    self.__validator.validateType(battleship)
                    direction = pick.choice(directionList)
                    self.__validator.validateDirection(direction)
                    battleshipObj = Battleship(positionX, positionY, battleship, direction)
                    if self.__opponent.addBattleship(self.__opponentBoard, battleshipObj, battleShipList) == False:
                        print(self.__opponentBoard)
                        break
                    else:
                        arrangements -= 1
                        battleship += 1
                        direction += 1
                        break
                except MenuException as exc:
                    print(str(exc))
                    break

        print("Opponent's board")
        print(copyBoard)
        print("Your board")
        print(self.__yourBoard)

    def playerTurn(self, copyBoard, board):
        print("Opponent's board")
        print(copyBoard)
        print("Your board")
        print(self.__yourBoard)

        while True:
            try:
                positionX = self.convert(input("Give x:"))
                self.__validator.validatePosition(positionX)
                positionY = input("Give y:")
                self.__validator.validatePosition(positionY)
                positionY = int(positionY)
                if self.__you.hit(positionX, positionY, self.__opponentBoard, copyBoard, board) == [-1, -1]:
                    print("Position unavailable!")
                else:
                    break
            except MenuException as exc:
                print(str(exc))

    def opponentTurn(self, board):
        uselessCopy = Game(0, 9)

        positionListX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        positionListY = [1, 2, 3, 4, 5, 6, 7, 8]

        pick = random.SystemRandom()

        while True:
            positionX = self.convert(pick.choice(positionListX))
            self.__validator.validatePosition(positionX)
            positionY = pick.choice(positionListY)
            self.__validator.validatePosition(positionY)
            lastPos = self.__opponent.hit(positionX, positionY, self.__yourBoard, uselessCopy, board)
            return lastPos

    def run(self):
        copyBoard = Game(self.__opponentBoard.getGameState(), self.__opponentBoard.getNo1())

        positionX = -1
        positionY = -1
        directionList = [0, 0, 0, 0]
        uselessCopy = Game(0, 9)

        while True:
            try:
                option = input("\nChoose option:")
                self.__validator.validateOption(option)
                if int(option) == 1:
                    self.startTurnPlayer()
                    self.startTurnOpponent(copyBoard)
                    while self.__yourBoard.getGameState() == 0 and self.__opponentBoard.getGameState() == 0:
                        yourBoard = self.__yourBoard
                        opponentBoard = self.__opponentBoard

                        self.playerTurn(copyBoard, opponentBoard)

                        if yourBoard.getNo1() == 0:
                            self.__yourBoard.setGameState(1)
                            print("                     Game over!                      \n")
                            print("                    You lost!                          ")
                            return
                        if opponentBoard.getNo1() == 0:
                            self.__opponentBoard.setGameState(1)
                            print("                     Game over!                      \n")
                            print("                     You won!                          ")
                            return

                        if positionX == -1 and positionY == -1:
                            while True:
                                if positionX == -1 and positionY == -1:
                                    opTurn = self.opponentTurn(yourBoard)
                                    positionX = opTurn[0]
                                    positionY = opTurn[1]
                                else:
                                    break
                        elif positionX == -2 and positionY == -2:
                            opTurn = self.opponentTurn(yourBoard)
                            positionX = opTurn[0]
                            positionY = opTurn[1]
                        elif positionX == -3 and positionY == -3:
                            opTurn = self.opponentTurn(yourBoard)
                            positionX = opTurn[0]
                            positionY = opTurn[1]
                            directionList = [0, 0, 0, 0]
                        elif positionX == -4 and positionY == -4:
                            while True:
                                if positionX == -1 and positionY == -1:
                                    opTurn = self.opponentTurn(yourBoard)
                                    positionX = opTurn[0]
                                    positionY = opTurn[1]
                                    break
                                else:
                                    break
                        else:
                            while True:
                                print(positionX, positionY)
                                rotate = self.__opponent.rotateHit(positionX, positionY, self.__yourBoard,
                                                                   yourBoard, uselessCopy, directionList)
                                if rotate != None:
                                    positionX = rotate[0]
                                    positionY = rotate[1]
                                    directionList = rotate[2]
                                    break
                                else:
                                    positionX = -1
                                    positionY = -1
                                    if positionX == -1 and positionY == -1:
                                        opTurn = self.opponentTurn(yourBoard)
                                        positionX = opTurn[0]
                                        positionY = opTurn[1]
                                        break
                                    else:
                                        break

                        if yourBoard.getNo1() == 0:
                            self.__yourBoard.setGameState(1)
                            print("                     Game over!                      \n")
                            print("                    You lost!                          ")
                            return
                        if opponentBoard.getNo1() == 0:
                            self.__opponentBoard.setGameState(1)
                            print("                     Game over!                      \n")
                            print("                     You won!                          ")
                            return
                elif int(option) == 2:
                    self.help()
                elif int(option) == 3:
                    print("Are you sure you want to exit the game?")
                    print("Press Y for yes or N for no.")
                    while True:
                        try:
                            exitOption = input("-")
                            self.__validator.validateExit(exitOption)
                            if exitOption == "Y" or exitOption == "y":
                                return
                            else:
                                break
                        except MenuException as exc:
                            print(str(exc))
            except MenuException as exc:
                print(str(exc))