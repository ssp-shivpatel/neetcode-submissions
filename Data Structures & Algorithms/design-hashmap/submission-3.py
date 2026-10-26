class MyHashMap:

    class _HashNode:
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.next = None


    def __init__(self):
        self.buckets = [None] * 10
        self.size = 0


    def put(self, key: int, value: int) -> None:
        if(self.size > len(self.buckets)):
            self._expandCapacity()
        
        hashIndex = key % len(self.buckets)

        if(self.buckets[hashIndex] == None):
            self.buckets[hashIndex] = self._HashNode(key, value)
        elif(self.buckets[hashIndex].key == key):
            self.buckets[hashIndex].value = value
        else:
            curr = self.buckets[hashIndex]
            while(curr.next != None):
                curr = curr.next
                if(curr.key == key):
                    curr.value = value
                    return

            curr.next = self._HashNode(key, value)
        
    def get(self, key: int) -> int:
        hashIndex = key % len(self.buckets)

        if(self.buckets[hashIndex] == None):
            return -1
        elif(self.buckets[hashIndex].key == key):
            return self.buckets[hashIndex].value
        else:
            curr = self.buckets[hashIndex]
            while(curr.next != None):
                curr = curr.next
                if(curr.key == key):
                    return curr.value

            return -1
        

    def remove(self, key: int) -> None:
        hashIndex = key % len(self.buckets)

        if(self.buckets[hashIndex] == None):
            return
        elif(self.buckets[hashIndex].key == key):
            self.buckets[hashIndex] = self.buckets[hashIndex].next
        else:
            curr = self.buckets[hashIndex]
            while(curr.next != None):
                if(curr.next.key == key):
                    curr.next = curr.next.next
                    return
                curr = curr.next

    def _expandCapacity():
        oldBuckets = self.buckets
        newBuckets = [None] * len(self.buckets) * 2
        self.buckets = newBuckets

        for i in range(len(oldBuckets)):
            curr = oldBuckets[i]
            if(curr != None):
                self.put(curr.key, curr.value)
                curr = curr.next
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)