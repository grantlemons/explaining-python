# Classes are collections of variables and functions
# Class functions can reference class variables with self.

class class_template:
    variable_template_1 = int
    
    def template_function_1(self):
        return self.variable_template_1

# Examples
# -----------------------------

class dog:
    name = 'please set name'
    state = True
    location = [0, 0]
    rotation = 0
    
    def bark(self):
        if self.state:
            print( f'{self.name}: woof!' )
        else:
            print( f'{self.name}: zzzzz' )
        
    def sleep(self):
        self.state = False
        print( f'{self.name}: zzzzz' )
    
    def wake(self):
        self.state = True
        print( f'{self.name}: tis i!' )
    
    def turn_left(self):
        if self.state:
            if self.rotation < 270:
                self.rotation += 90
            else:
                self.rotation = 0
        else:
            print( f'{self.name}: zzzzz' )
    
    def turn_right(self):
        if self.state:
            if self.rotation > 0:
                self.rotation -= 90
            else:
                self.rotation = 270
        else:
            print( f'{self.name}: zzzzz' )
        
    def walk(distance, self):
        if self.state:
            if self.rotation == 0:
                self.location[0] += distance
            if self.rotation == 90:
                self.location[1] += distance
            if self.rotation == 180:
                self.location[0] -= distance
            if self.rotation == 270:
                self.location[1] -= distance
            return self.position
        else:
            print( f'{self.name}: zzzzz' )

rover = dog()
rover.name = 'rover'
rover.location = [23, 16]
rover.rotation = 180

rufus = dog()
rufus.name = 'rufus'
rufus.state = False
rufus.location = [24, 14]
rover.rotation = 90

rover.bark()
rufus.wake()
rufus.bark()