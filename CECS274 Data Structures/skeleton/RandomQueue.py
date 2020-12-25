import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        randomNum = random.randint(0, self.n)
        x = self.a[0]
        self.a[0] = self.a[randomNum]
        self.a[randomNum] = x
        super().remove()
        return self
        # todo
        pass 
     




