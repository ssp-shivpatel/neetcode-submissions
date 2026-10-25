class MyHashSet:

    def __init__(self):
        self.arr = [None] * 10
        self.size = 0
        
    def add(self, key: int) -> None:
        if(self.size > len(self.arr) / 2):
           self._increaseCapacity()

        index = key % len(self.arr)

        while(self.arr[index] != key and self.arr[index] != None):
            index += 1;
            if(index == len(self.arr)):
                index = 0

        self.arr[index] = key
        self.size += 1
        
    
    def remove(self, key: int) -> None:
        index = key % len(self.arr)
        cluster = []

        while(self.arr[index] != None):
            if(self.arr[index] != key):
                cluster.append(self.arr[index])

            self.arr[index] = None
            index += 1
            if(index == len(self.arr)):
                index = 0
        
        for i in range(len(cluster)):
            self.add(cluster[i])

    def contains(self, key: int) -> bool:
        index = key % len(self.arr)

        while(self.arr[index] != key):
            if(self.arr[index] == None):
                return False

            index += 1
            if(index == len(self.arr)):
                index = 0
        
        return True

    def _increaseCapacity(self) -> None:
        oldArr = self.arr
        newArr = [None] * len(self.arr) * 2
        self.arr = newArr
        self.size = 0

        for i in range(len(oldArr)):
            if(oldArr[i] != None):
                self.add(oldArr[i])

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)