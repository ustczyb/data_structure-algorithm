# coding=utf-8
# 高级排序算法 复杂度O(nlogn) 希尔排序 快速排序 归并排序 堆排序





# 快速排序
from data_structure.heap import MaxHeap
from sort.primary_sort import swap


def quick_sort(nums, begin, end):
    if begin >= end:
        return
    mid = partation(nums, begin, end)
    quick_sort(nums, begin, mid - 1)
    quick_sort(nums, mid + 1, end)


# 快速排序的partation操作
def partation(nums, begin, end):
    a = nums[begin]
    index = begin + 1
    for i in range(begin, end + 1):
        if nums[i] < a:
            swap(nums, i, index)
            index += 1
    swap(nums, begin, index - 1)
    return index - 1


# 希尔排序
def shell_sort(nums):
    n = len(nums)
    h = n / 3
    while h > 0:
        for i in range(h, n):
            for k in range(i - h, -1, -h):
                if nums[k] > nums[k + h]:
                    swap(nums, k, k + h)
                else:
                    break
        h = (h + 1) / 3


# 堆排序
def heap_sort(nums):
    heap = MaxHeap(nums, len(nums))
    heap.build_heap()
    for i in range(len(nums) - 1, -1, -1):
        swap(nums, 0, i)
        heap.max_heapify(0, i)


# 归并排序
class MergeSort:
    def __init__(self, nums):
        self.nums = nums
        self.nums_copy = nums[:]

    # 归并排序，对[begin, end)范围内的数据进行排序
    def merge_sort(self, begin=0, end=-1):
        if end == -1:
            end = len(self.nums)
        if begin >= end - 1:
            return
        mid = int((begin + end) / 2)
        self.merge_sort(begin, mid)
        self.merge_sort(mid, end)
        self.merge(begin, mid, end)

    # 合并操作，[lo, mid)和[mid, high)均为排序后的数组，合并这两个数组使其有序
    def merge(self, lo, mid, high):
        for i in range(lo, mid):
            self.nums_copy[i] = nums[i]
        i = k = lo
        j = mid
        while i < mid and j < high:
            if self.nums_copy[i] > nums[j]:
                nums[k] = nums[j]
                k += 1
                j += 1
            else:
                nums[k] = self.nums_copy[i]
                k += 1
                i += 1
        if j == high:
            nums[k: high] = self.nums_copy[i: mid]


if __name__ == '__main__':
    nums = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    mergeSort = MergeSort(nums)
    mergeSort.merge_sort()
    # heap_sort(nums)
    print(nums)
