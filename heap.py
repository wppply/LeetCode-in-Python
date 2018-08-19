class heap(object):
    def __init__(self, arr):
        self.arr = arr
        self.build_max_heap()

    def max_heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2

        if l < len(self.arr) and self.arr[l] < self.arr[i]:
            large_idx = i
        else:
            large_idx = l

        if r < len(self.arr) and self.arr[r] > self.arr[large_idx]:
            large_idx = r
        if large_idx != i and large_idx < len(self.arr):
            self.arr[i], self.arr[large_idx] = self.arr[large_idx], self.arr[i]
            self.max_heapify(large_idx)
        else:
            return

    def build_max_heap(self):
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.max_heapify(i)
            print('%d done' % i)


if __name__ == "__main__":
    arr = [2, 5, 1, 5, 7, 4, 8]
    h = heap(arr)
    print(h.arr)
