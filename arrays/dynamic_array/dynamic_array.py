import ctypes
class DynamicArray(object):
    """ Dynamic array implmentation using ctypes """
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __get_item__(self, k):
        if not 0 <= k:
            return IndexError('k is out of bounds')
        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity is not enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
