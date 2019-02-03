from Menu import Menu
from Game import Game
from Players import Player

yourBoard = Game(0, 9)
you = Player(0, yourBoard)
opponentBoard = Game(0, 9)
opponent = Player(1, yourBoard)
menu = Menu(you, opponent, yourBoard, opponentBoard)
menu.show()
menu.run()