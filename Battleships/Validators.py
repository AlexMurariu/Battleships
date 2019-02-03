class MenuException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class MenuValidator:

    def validateOption(self, option):
        msg = ""
        try:
            option = int(option)
            if int(option) <= 0 or int(option) > 3:
                msg += "Invalid option! \n"
        except ValueError:
            msg += "Pleas insert a number! \n"
        if msg != "":
            raise MenuException(msg)

    def validateExit(self, option):
        msg = ""
        try:
            option = int(option)
            msg += "Invalid option! \n"
        except ValueError:
            if option == "Y" or option == "y" or option == "N" or option == "n":
                pass
            else:
                msg += "Invalid option! \n"
        if msg != "":
            raise MenuException(msg)

    def validatePosition(self, pos):
        msg = ""
        try:
            if pos == None:
                msg += "Invalid position\n"
            else:
                pos = int(pos)
                if int(pos) > 8 or int(pos) < 1:
                    msg += "Invalid position \n"
        except ValueError:
            msg += "Please insert a number!\n"
        if msg != "":
            raise MenuException(msg)

    def validateType(self, type):
        msg = ""
        try:
            type = int(type)
            if int(type) > 3 or int(type) < 1:
                msg += "Invalid battleship \n"
        except ValueError:
            msg += "Please insert a number!\n"
        if msg != "":
            raise MenuException(msg)

    def validateDirection(self, direction):
        msg = ""
        try:
            direction = int(direction)
            if int(direction) > 4 or int(direction) < 1:
                msg += "Invalid direction \n"
        except ValueError:
            msg += "Please insert a number!\n"
        if msg != "":
            raise MenuException(msg)