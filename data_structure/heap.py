# coding=utf-8
# 最大堆
from sort.primary_sort import swap


class MaxHeap:
    # nums[]为堆的数组 size为堆大小
    def __init__(self, nums, size):
        self.nums = nums
        self.size = size

    # 左子树下标
    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) / 2

    # 建堆操作
    def build_heap(self):
        for i in range(int(self.size / 2), -1, -1):
            self.max_heapify(i, self.size)

    # 假定i的左右子树均为最大堆，调整使得i为根的子树也为最大堆
    def max_heapify(self, i, size):
        # 叶子节点无需操作
        if self.left(i) >= size:
            return
        # 仅有左节点
        if self.left(i) == size - 1:
            if self.nums[i] >= self.nums[self.left(i)]:
                return
            else:
                swap(self.nums, i, self.left(i))
                return
        # 左右节点均存在
        maxi = self.left(i) if self.nums[self.left(i)] > self.nums[self.right(i)] else self.right(i)
        if self.nums[i] >= self.nums[maxi]:
            return
        else:
            swap(self.nums, i, maxi)
            self.max_heapify(maxi, size)


if __name__ == '__main__':
    nums = [6, 32, 1, 25, 47, 28, 15]
    heap = MaxHeap(nums, len(nums))
    heap.build_heap()
    print(heap.nums)
    for i in range(len(nums) - 1, -1, -1):
        swap(nums, 0, i)
        heap.max_heapify(0, i)
    print(nums)