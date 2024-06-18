import random

class RandomizedSet:
    
    def __init__(self):
        self.mySet = set()
        self.arr = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if (val not in self.mySet):
            self.mySet.add(val)
            self.arr.append(val)
            self.size += 1
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if (val in self.mySet):
            self.mySet.remove(val)
            for i in range(self.size):
                if (self.arr[i] == val):
                    temp = self.arr[i]
                    self.arr[i] = self.arr[self.size-1]
                    self.arr[self.size-1] = temp
                    break
            self.arr.pop()
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.size-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()