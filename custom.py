# You can add any additional function and class you want to implement in this file
from crewmate import CrewMate 
from heap import Heap
from treasure import Treasure
from straw_hat import StrawHatTreasury
straw=StrawHatTreasury(3)
straw.add_treasure(Treasure(1,8,1))
straw.add_treasure(Treasure(2,7,2))
straw.add_treasure(Treasure(3,4,4))
straw.add_treasure(Treasure(4,1,5))
print(straw.get_completion_time())





