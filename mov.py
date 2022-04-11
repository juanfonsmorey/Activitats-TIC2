import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
VELOCITAT = 3

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

class Pere(Ball):

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        super().__init__(position_x, position_y, change_x, change_y, radius, color)
        
        self.key=[0]*4
        #UP,DOWN,LEFT,RIGHT
        print(self.key)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x = 0

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x = 0

        if self.position_y < self.radius:
            self.change_y = 0

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y = 0
    
    def key_press(self,key):
        #self.key = key
        #print("agafant", self.key)
        if key == arcade.key.UP or key == arcade.key.W:
            self.change_y = VELOCITAT
            self.key[0]=1
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y=-VELOCITAT
            self.key[1]=1
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -VELOCITAT
            self.key[2]=1

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = VELOCITAT
            self.key[3]=1
        print(self.key)
    
    def key_release(self,key,modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.change_y = 0
            self.key[0]=0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y=-0
            self.key[1]=0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
            self.key[2]=0

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0
            self.key[3]=0
        print(self.key)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

        self.pere = Pere(50, 50, 0, 0, 5, arcade.color.ORANGE)
          
        # Create a list for the balls
        self.ball_list = []
        


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on that ball.
        self.pere.draw()
        for ball in self.ball_list:
            ball.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""

        # Use a "for" loop to pull each ball from the list, then call the update
        # method on that ball.
        self.pere.update()
        for ball in self.ball_list:
            ball.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        self.pere.key_press(key)
        

    def on_key_release(self, symbol, modifiers):
        #print("amollant ", self.pere.key)
        self.pere.key_release(symbol,modifiers)
        return super().on_key_release(symbol, modifiers)

    

def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()