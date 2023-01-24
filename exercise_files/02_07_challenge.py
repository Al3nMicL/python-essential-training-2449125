import os
import time
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

    def drawSquare(self, size):
        """The function takes a size and draws a square of the given size.        
        """
        i = 0 # tracking variable
        # size variables for each side
        right_moves = 0
        down_moves = 0
        left_moves = 0
        up_moves = 0

        while i <= size: # while the tracking var is less than the size, execute this loop
            if right_moves <= size: # if the size of the side is less than or equal to the size
                scribe.right() # draw character to the given direction
                right_moves += 1 # increment the size of the side
                i += 1 # increment the tracking variable
                if right_moves == size: # once the size of the side equals the specified size
                    break # break out of the loop
        i = 0 # reset the tracker
        # draw the next side only once the previous side has reached the specified size
        while i <= size and right_moves == size: # same logic as before
            if down_moves <= size:
                scribe.down()
                down_moves += 1
                i += 1
                if down_moves == size:
                    break
        i = 0
        # repeat
        while i <= size and down_moves == size:
            if left_moves <= size:
                scribe.left()
                left_moves += 1
                i += 1
                if left_moves == size:
                    break
        i = 0
        # one last time
        while i <= size and left_moves == size:
            if up_moves <= size:
                scribe.up()
                up_moves += 1
                i += 1
                if up_moves == size:
                    break

# Create a new Canvas instance that is 30 units wide by 30 units tall 
canvas = Canvas(30, 30)

# Create a new scribe and give it the Canvas object
scribe = TerminalScribe(canvas)

# Draw a square with a specified size
scribe.drawSquare(7)
# Draw a small square
# scribe.right()
# scribe.right()
# scribe.right()
# scribe.down()
# scribe.down()
# scribe.down()
# scribe.left()
# scribe.left()
# scribe.left()
# scribe.up()
# scribe.up()
# scribe.up()
