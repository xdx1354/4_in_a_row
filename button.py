import pygame

"""
Button class

Example of usage:
            # create an instance of class, pass data to the constructor
            btn = Button(20, 20, 80, 30, (140, 40, 70), (140, 40, 140), self.SCREEN)
            
            # set label of button if you want
            btn.setText("TEST", "corbel", 10)
            # checking if button was clicked, returns True or False
            if btn.isClicked():
                print("BTN clicked")
            pygame.display.update()


"""
class Button(object):
    def __init__(self, x, y, width, height, color, hoverColor, layer):
        """
        Constructor of self-made Button class
        :param x: x dimension of top-left corner
        :param y: y dimension of top-left corner
        :param width: width of rectangle
        :param height: height of rectangle
        :param color: default color of rectangle
        :param hoverColor: hover color of rectangle
        :param layer: background layer on which this button will be drawn
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hoverColor = hoverColor
        self.screen = layer

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(layer, hoverColor, (x, y, width, height))

        else:
            pygame.draw.rect(layer, color, (x, y, width, height))


    def setText(self, text, font, size):
        """
        Setting label of button, by default text will be centered
        :param text: Text of the label
        :param font: string with name of font from SysFont
        :param size: int, size of text
        :return:
        """
        labelFont = pygame.font.SysFont(font, size)
        labelText = labelFont.render(text, True, (0,0,0))
        self.screen.blit(labelText, (self.x + self.width/2 - labelText.get_width()/2, self.y + self.height/2 - labelText.get_height()/2))

    def isClicked(self):
        """
        Checking if button was clicked
        :return: True or False
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            return True
        else:
            return False
