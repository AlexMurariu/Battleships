import unittest
from Players import *
from Game import *
from Battleships import *

class Test(unittest.TestCase):

    def testGetters(self):
        trump = Battleship(1, 4, 3, 2)
        kim_jong_un = Battleship(8, 5, 2, 3)

        posTrumpX = trump.getPositionX()
        posKimX = kim_jong_un.getPositionX()
        posTrumpY = trump.getPositionY()
        posKimY = kim_jong_un.getPositionY()
        battleshipTrump = trump.getType()
        battleshipKim = kim_jong_un.getType()
        dirTrump = trump.getDirection()
        dirKim = kim_jong_un.getDirection()

        self.assertEqual(posTrumpX, 4)
        self.assertEqual(posKimX, 5)
        self.assertEqual(posTrumpY, 1)
        self.assertEqual(posKimY, 8)
        self.assertEqual(battleshipTrump, 3)
        self.assertEqual(battleshipKim, 2)
        self.assertEqual(dirTrump, 2)
        self.assertEqual(dirKim, 3)

    def testSetters(self):
        trump = Battleship(2, 2, 1, 2)

        trump.setPositionX(4)
        posTrumpX = trump.getPositionX()

        trump.setPositionY(1)
        posTrumpY = trump.getPositionY()

        trump.setType(3)
        battleshipTrump = trump.getType()

        trump.setDirection(2)
        dirTrump = trump.getDirection()

        kim_jong_un = Battleship(3, 3, 1, 3)

        kim_jong_un.setPositionX(5)
        posKimX = kim_jong_un.getPositionX()

        kim_jong_un.setPositionY(8)
        posKimY = kim_jong_un.getPositionY()

        kim_jong_un.setDirection(3)
        dirKim = kim_jong_un.getDirection()

        kim_jong_un.setType(2)
        battleshipKim = kim_jong_un.getType()

        self.assertEqual(posTrumpX, 4)
        self.assertEqual(posKimX, 5)
        self.assertEqual(posTrumpY, 1)
        self.assertEqual(posKimY, 8)
        self.assertEqual(battleshipTrump, 3)
        self.assertEqual(battleshipKim, 2)
        self.assertEqual(dirTrump, 2)
        self.assertEqual(dirKim, 3)

    def testAddBattleShip(self):
        yourBoard = Game(0, 9)
        you = Player(0, yourBoard)
        trump = Battleship(1, 1, 3, 2)
        kim_jong_un = Battleship(8, 8, 2, 2)
        self.assertEqual(you.addBattleship(yourBoard, trump, []), True)
        self.assertEqual(you.addBattleship(yourBoard, kim_jong_un, []), False)

    def testHit(self):
        yourBoard = Game(0, 9)
        you = Player(0, yourBoard)
        trump = Battleship(1, 1, 3, 2)
        you.addBattleship(yourBoard, trump, [])
        self.assertEqual(you.hit(1, 1, yourBoard, yourBoard, yourBoard), [1, 1])
        self.assertEqual(you.hit(2, 2, yourBoard, yourBoard, yourBoard), [-2, -2])
        self.assertEqual(you.hit(1, 1, yourBoard, yourBoard, yourBoard), [-1, -1])

if __name__ == "__main__":
      unittest.main()