import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.dic = {}
        self.size = 0
        

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.append(val)
            self.dic[val] = self.size
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            idx = self.dic[val]
            last = self.data[-1]
            self.data[idx] = last
            self.dic[last] = idx

            self.data.pop()
            del self.dic[val]
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()