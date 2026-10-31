class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(0, len(nums), nums)
        return nums

    def quickSort(self, begin, end, arr) -> None:
        if(begin > end):
            return

        mid = self.partition(begin, end, arr)
        if(mid == -1):
            return
        self.quickSort(begin, mid, arr)
        self.quickSort(mid+1, end, arr)

    def partition(self, begin, end, arr) -> int:
        if(end - begin < 8):
            self.insertionSort(begin, end, arr)
            return -1

        mid = (end+begin)//2

        if(arr[begin] > arr[end-1]):
            self.swap(begin, end-1, arr)
        if(arr[begin] > arr[mid]):
            self.swap(begin, mid, arr)
        if(arr[mid] > arr[end-1]):
            self.swap(mid, end-1, arr)

        pivot = arr[mid]
        self.swap(mid, end-2, arr)

        left = begin
        right = end-3

        while(left < right):
            while(left < end-3 and arr[left] <= pivot):
                left += 1
            
            while(right > begin and arr[right] >= pivot):
                right -= 1
            
            if(left < right):
                self.swap(left, right, arr)
        
        self.swap(left, end-2, arr)
        return left

    def swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def insertionSort(self, begin, end, arr) -> None:
        for i in range(begin, end-1):
            for j in range(i + 1, 0, -1):
                if(arr[j] < arr[j - 1]):
                    self.swap(j, j - 1, arr)
                else:
                    break

    