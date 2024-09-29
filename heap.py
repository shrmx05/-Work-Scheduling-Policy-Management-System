'''
Python Code to implement a heap with general comparison function
'''

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
        self.comparator=comparison_function
        self.size=len(init_array)
        self.heap=init_array
        self.build_heap()

        # Write your code here
        pass
    def build_heap(self):
        """ Bottom-up heap construction """
        n = len(self.heap)
        for i in range((n - 2) // 2, -1, -1):
            self.downheap(i)
    def downheap(self, i):
        """ Sifts the element at index i downwards to maintain heap property """
        n = len(self.heap)
        while 2 * i + 1 < n:  # While i has at least one child
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            min_child = left_child

            if right_child < n and self.comparator(self.heap[right_child],self.heap[left_child]):
                min_child = right_child

            if self.comparator(self.heap[i],self.heap[min_child]):
                break

            # Swap and continue sifting down
            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child        

    def upheap(self, i):
        """ Sifts the element at index i upwards to maintain heap property """
        while i > 0:
            parent = (i - 1) // 2
            if self.comparator(self.heap[parent],self.heap[i]):
                break

            # Swap and continue sifting up
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent    
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
        self.heap.append(value)
        self.upheap(len(self.heap) - 1)
        
        # Write your code here
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
        top_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.downheap(0)

        return top_value
        
        # Write your code here
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
        x=self.heap
        return x[0]
        # Write your code here
        pass
    
    # You can add more functions if you want to