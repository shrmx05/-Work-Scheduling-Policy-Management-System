'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate 
from heap import Heap
from treasure import Treasure

def compC(c1,c2):
    if c1.load<c2.load:
        return True
    else:
        return False
    

    


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self,m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        lst=[]
        for j in range(m):
            lst.append(CrewMate())
        self.crewmates=Heap(compC,lst)
        self.completed_treasures=[]
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        t=treasure.arrival_time
        delta=treasure.arrival_time-self.crewmates.heap[0].prev
        while len(self.crewmates.heap[0].treasures.heap)>0 and self.crewmates.heap[0].treasures.heap[0].size<delta:
            self.crewmates.heap[0].treasures.heap[0].completion_time=t - delta + self.crewmates.heap[0].treasures.heap[0].size
            delta-=self.crewmates.heap[0].treasures.heap[0].size
            top=self.crewmates.heap[0].treasures.extract()
            self.completed_treasures.append((top.id,top.completion_time))

        if len(self.crewmates.heap[0].treasures.heap)>0:
            self.crewmates.heap[0].treasures.heap[0].size-=delta
            self.crewmates.heap[0].treasures.downheap(0)
        

        self.crewmates.heap[0].load+=(treasure.size+treasure.arrival_time)

        self.crewmates.heap[0].treasures.insert(treasure)

        self.crewmates.heap[0].prev=treasure.arrival_time

        self.crewmates.downheap(0)

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        for i in self.crewmates.heap:
            current_heap=i.treasures
            while (len(current_heap.heap)>0):
                current_heap.heap[0].completion_time=i.prev + current_heap.heap[0].size 
                i.prev+=current_heap.heap[0].size
                self.completed_treasures.append((current_heap.heap[0].id,current_heap.heap[0].completion_time))
                current_heap.extract()
                
        return sorted(self.completed_treasures)

                