'''
    Python file to implement the class CrewMate
'''
from heap import Heap, comparator_priority

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self, id):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.id = id
        self.load = 0
        self.treasure_heap = Heap(comparator_priority, [])
        pass
    
    # Add more methods if required
    def add(self, treasure):
        self.treasure_heap.insert(treasure)
        self.load = sum([x.rem_size for x in self.treasure_heap.heap])
    def update_load(self):
        self.load = sum([x.rem_size for x in self.treasure_heap.heap])

