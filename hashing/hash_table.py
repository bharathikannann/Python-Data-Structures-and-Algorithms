# Hash table
# Here collisions are handles by sepearte chaining
class HashTable:
    def __init__(self, size = 100):
        self.size = size   # Size initialization
        self.arr = [[] for _ in range(self.size)]   
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)   # Ord returns the ASCII value of character
        return hash % self.size # Mod of total hash vs size is the final hash
    # ------------------------------------------------------------------------------------------
    # https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    # By using __setitem__, __delitem__, __getitem__ we can easily work with hash objects
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False   
        for idx, element in enumerate(self.arr[h]):   # For updating the already present key
            if element[0] == key:
                self.arr[h][idx] = (key, val)         # Update existing key value pairs
                found = True
        if not found:                                 # If not found append at last
            self.arr[h].append((key, val))
    # ------------------------------------------------------------------------------------------
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):   # Find the position in sepearte chains and delete at that position
            if element[0] == key:
                del self.arr[h][idx]
    # ------------------------------------------------------------------------------------------            
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:   # If element found
                return element[1]
        return "Not present"        # If element not found

if __name__ == '__main__':
    h = HashTable(10)
    h['1'] = 1
    h['2'] = 2
    h['3'] = 3
    print(h.arr)
    del h['1']
    print(h.arr)
    print(h['1'])
    print(h['2'])
    '''
    Output
    [[('2', 2)], [('3', 3)], [], [], [], [], [], [], [], [('1', 1)]]
    [[('2', 2)], [('3', 3)], [], [], [], [], [], [], [], []]
    Not present
    2
    '''