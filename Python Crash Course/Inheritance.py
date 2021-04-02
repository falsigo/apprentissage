from MouseClass import Mouse
from KeyboardClass import Keyboard


# def combo_maker():
#available_mouse = [Mouse.mice1, Mouse.mice2]
#available_keyboard = [Keyboard.keyboard1, Keyboard.keyboard2]


class MnK(Mouse, Keyboard):
    def __init__(self, combo_price):
        self.combo_price = combo_price

    print(str(Mouse) + str(Keyboard))
# this will make a list of mouse and keyboard from the available entries in the Mouse.py and Keyboard.py files
    #available_mouse = [Mouse.mice1, Mouse.mice2]
    #available_keyboard = [Keyboard.keyboard1, Keyboard.keyboard2]

    #available_mouse = []
    #available_keyboard = []

    # no I want to cycle between each of the list and combine all mouse with all keyboards
    # combo_maker()
    #for mice in available_mouse:
      #  for kybrd in available_keyboard:
     #       combo = [mice,kybrd]

    #for item in combo:
       # print(item)