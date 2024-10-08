'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap, comparator_load
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
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
        self.treasury = []
        self.crewmate_heap = Heap(comparator_load,[CrewMate(i) for i in range(m)])
        # Write your code here
        pass
    
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
        
        # Write your code here
        treasure.initialise_remsize()
        self.treasury.append(treasure)
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        self.crewmates_util = []
        self.time = 0
        for i in range(len(self.treasury)):
            self.treasury[i].initialise_remsize()
            self.add_to_crewmate_heap(self.treasury[i])
            if (i != len(self.treasury)-1) and (self.treasury[i+1].arrival_time == self.treasury[i].arrival_time):
                continue
            elif i != len(self.treasury)-1:
                self.process(self.treasury[i].arrival_time,self.treasury[i+1].arrival_time)
                self.time = self.treasury[i+1].arrival_time
            else:
                self.time = self.treasury[i].arrival_time
                self.process_to_completion(self.time)
        for i in self.treasury:
            i.initialise_remsize()
        return sorted(self.treasury, key = lambda x: x.id)
    # You can add more methods if required
    def add_to_crewmate_heap(self, value):
        # for i in self.crewmate_heap.heap:
        #     print('crewmate' , i.id, 'load', i.load)
        a = self.crewmate_heap.extract()
        a.add(value)
        # print('treasure', value.id, 'added to crewmate ',a.id)
        if a not in self.crewmates_util:
            self.crewmates_util.append(a)
        self.crewmate_heap.insert(a)
        # for i in self.crewmate_heap.heap:
        #     print('after addition :', 'crewmate' ,i.id,  [(x.id,x.rem_size) for x in i.treasure_heap.heap])

    def process(self, cur_time, next_time):
        for i in self.crewmates_util:
            iter = next_time - cur_time
            tm = cur_time
            while i.treasure_heap.top() and iter > 0:
                if iter < i.treasure_heap.top().rem_size:
                    i.treasure_heap.top().rem_size -= iter
                    # print('crewmate', i.id, [(x.id,x.rem_size) for x in i.treasure_heap.heap])
                    iter -= iter 
                elif iter >= i.treasure_heap.top().rem_size:
                    # if i.treasure_heap.top().id == 5:
                    #     print('iter at this pt', iter, 'treasure_rem_time', i.treasure_heap.top().rem_size)
                    a = i.treasure_heap.top().rem_size
                    i.treasure_heap.top().completion_time = tm + a
                    # print('crewmate', i.id, [(x.id,x.rem_size) for x in i.treasure_heap.heap])
                    i.treasure_heap.top().rem_size = 0
                    iter -= a
                    tm += a
                    i.treasure_heap.extract()
                i.update_load()
    def process_to_completion(self, time):
        for i in self.crewmates_util:
            run_time = time
            while i.treasure_heap.top():
                i.treasure_heap.top().completion_time = run_time + i.treasure_heap.top().rem_size
                run_time += i.treasure_heap.top().rem_size
                i.treasure_heap.top().rem_size -= i.treasure_heap.top().rem_size
                # print('crewmate', i.id, [(x.id,x.completion_time) for x in i.treasure_heap.heap])
                i.treasure_heap.extract()
                i.update_load()

    



# a = StrawHatTreasury(3)
# a.add_treasure(treasure.Treasure(1,8,1))
# print([(x.id, x.completion_time) for x in a.get_completion_time()])
# a.add_treasure(treasure.Treasure(2,7,2))
# print([(x.id, x.completion_time) for x in a.get_completion_time()])
# a.add_treasure(treasure.Treasure(3,4,4))
# # a.add_treasure(treasure.Treasure(4,1,5))
# print([(x.id, x.completion_time) for x in a.get_completion_time()])
            
# to_add= [(4, 5, 1),
#          (3, 4, 4),
#          (5, 6, 4),
#          (6, 7, 4),
#          (8, 31, 4),
#          (7, 30, 5),
#          (9, 32, 6),
#          (2, 2, 7),
#          (1, 1, 8)]
        
# c = StrawHatTreasury(3)
# for i in to_add:
#     c.add_treasure(treasure.Treasure(i[0],i[1],i[2]))
#     print([(x.id, x.completion_time) for x in c.get_completion_time()])

# a = StrawHatTreasury(2)
# a.add_treasure(treasure.Treasure(1,10,0))
# # print([(x.id, x.completion_time) for x in a.get_completion_time()])
# a.add_treasure(treasure.Treasure(2,20,1))
# # print([(x.id, x.completion_time) for x in a.get_completion_time()])
# a.add_treasure(treasure.Treasure(3,10,35))
# a.add_treasure(treasure.Treasure(4,10,40))
# print([(x.id, x.completion_time) for x in a.get_completion_time()])


# if __name__ == "__main__":
#     to_add= [
#         (1, 1, 8),
#         (2, 2, 7),
#         (3, 4, 4),
#         (4, 5, 1),
#         (5, 6, 4),
#         (6, 7, 4),
#         (7, 30, 5),
#         (8, 31, 4),
#         (9, 32, 6)
#     ]

#     treasury = StrawHatTreasury(3)

#     for t in to_add:
#         treasury.add_treasure(treasure.Treasure(t[0], t[2], t[1]))
    
#     print([(t.id, t.arrival_time, t.completion_time) for t in treasury.get_completion_time()])
                


        

