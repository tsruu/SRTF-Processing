'''
Python Code to implement a heap with general comparison function
'''
def comparator_load(a, b):
    return a.load < b.load

def comparator_priority(a,b):
    if a.priority() == b.priority():
        return a.id < b.id
    return a.priority() < b.priority()

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comaparator = comparison_function
        self.heap = []
        if init_array:
            self.heap = init_array[:]
            n = len(self.heap)
            for i in reversed(range(n//2)):
                self._heapify_down(i)
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        top_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return top_element
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.heap:
            return self.heap[0]
        else:
            return None
        pass
    
    # You can add more functions if you want to
    def _heapify_down(self, idx):
        """
        Maintain the heap property by bubbling down from index `idx`.
        """
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        if left < len(self.heap) and self.comaparator(self.heap[left], self.heap[smallest]):
            smallest = left
        
        if right < len(self.heap) and self.comaparator(self.heap[right], self.heap[smallest]):
            smallest = right
        
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify_down(smallest)
    
    def _heapify_up(self, idx):
        """
        Maintain the heap property by bubbling up from index `idx`.
        """
        parent = (idx - 1) // 2
        if idx > 0 and self.comaparator(self.heap[idx], self.heap[parent]):
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)

