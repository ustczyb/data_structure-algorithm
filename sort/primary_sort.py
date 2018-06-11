# coding=utf-8
# 基本的排序算法 时间复杂度O(n^2) 空间复杂度O(1)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


# 选择排序 每次选出最小的放到第一个 复杂度O(n ^ 2)
def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if nums[min_i] > nums[j]:
                min_i = j
        swap(nums, i, min_i)


# 插入排序 将第i+1个插入到前i个的数组中使得前i+1个数有序
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[j + 1] < nums[j]:
                swap(nums, j + 1, j)


# 冒泡排序 从末尾向前相邻的两两比较，若逆序则交换顺序
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)


if __name__ == '__main__':
    nums = [6, 32, 1, 25, 47]
    bubble_sort(nums)
    print(nums)
