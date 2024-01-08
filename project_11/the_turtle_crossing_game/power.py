import random
from turtle import Turtle
STARTING_MOVE_DISTANCE = 5



class Power():
    def __init__(self):
        self.powers = []
        self.treasure_speed = STARTING_MOVE_DISTANCE


    def special_power(self):
        random_chance = random.randint(1, 50)
        if random_chance == 1:
            treasure = Turtle('square')
            treasure.shapesize(1, 1)
            treasure.penup()
            treasure.color('medium blue')
            random_y = random.randint(-250, 250)
            treasure.goto(300, random_y)
            self.powers.append(treasure)

    def move_treasure(self):
        for treasure in self.powers:
            treasure.backward(STARTING_MOVE_DISTANCE)



