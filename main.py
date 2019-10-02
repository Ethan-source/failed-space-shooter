import sys, logging, open_color, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""

NUM_ENEMIES = 5
STARTING_LOCATION = (400, 300)
BULLET_DAMAGE= 10
ENEMY_HP = 20
HIT_SCORE = 10
KILL_SCORE = 100


class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(open_color.black)



    def setup(self):
        self.center_x += self.dx
        self.center_y += self.dy
        pass 
   
 
            
def update(self, delta_time):
        pass

def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()




def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x #has the mouse follow the ball on the x axis
        self.ball.position_y = y #has the mouse follow the ball on the Y axis
        pass

def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            x= self.player.center_x
            y= self.player.center_y + 15
            bullet = bullet ((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)

        pass

def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            print("Left")
        elif key == arcade.key.RIGHT:
            print("Right")
        elif key == arcade.key.UP:
            print("Up")
        elif key == arcade.key.DOWN:
            print("Down")

def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()