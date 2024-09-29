'''
    Python file to implement the class CrewMate
'''
from heap import Heap
from treasure import Treasure

def compT(t1,t2):
    def priority(t):
        return t.arrival_time + t.size
    if priority(t1)<priority(t2):
        return True
    elif priority(t1)==priority(t2):
        if t1.id<t2.id:
            return True
    else: 
        return False


class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        self.load=0
        self.prev=0
        self.treasures=Heap(compT,[])

    def add_treasure(self,value):
        self.treasures.insert(value)

    def remove_treasure(self):
        self.treasures.extract()
    
