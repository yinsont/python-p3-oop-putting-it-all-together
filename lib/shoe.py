#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = 'Adidas', color = 'White', size = 0, material = 'Leather', condition = 'Used'):
        self.brand = brand
        self.color = color
        self.size = size
        self.material = material
        self.condition = condition

    def get_brand(self):
        return self._brand
    
    def get_color(self):
        return self._color
    
    def get_size(self):
        return self._size
    
    def get_material(self):
        return self._material
    
    def get_condition(self):
        return self._condition
    
    def cobble(self):
        self.condition = 'New'
        print('Your shoe is as good as new!')

    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)
    pass