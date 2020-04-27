from random import choice

class RandomWalk():
    '''Simulation of a Random Walk'''

    def __init__(self, numb_points = 5000):
        '''Initialize program'''
        self.numb_points = numb_points

        #list of x and y co-ordinate
        self.x_val = [0]
        self.y_val = [0]

    def get_fill():
        '''getting the value of direction and distance'''
        direction = choice([1,-1])
        distance = choice([i for i in range(5)])
        step = direction * distance
        return step

    def fill_walk(self):
        '''Deciding the direction and distance'''
        while len(self.x_val) < self.numb_points:

            x_step = RandomWalk.get_fill()
            y_step = RandomWalk.get_fill()
            
            #Removing the posibility of not going anywhere
            if x_step == 0 and y_step == 0:
                continue
            #getting ready for the next walk
            x_next = self.x_val[-1] + x_step
            y_next = self.y_val[-1] + y_step

            self.x_val.append(x_next)
            self.y_val.append(y_next)

            
