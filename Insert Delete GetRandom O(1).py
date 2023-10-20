class RandomizedSet:

    def __init__(self):
        self.val_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False

        self.val_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        
        curr_index = self.val_index[val]
        last_val = self.vals[-1]
        #swap the last elemnt with val
        self.vals[curr_index] = last_val
        self.val_index[last_val] = curr_index
        self.vals.pop()

        del self.val_index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
