#1
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))

#2
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))

#3
def reverse3(nums):
    return nums[::-1]

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))

#4
def middle_way(a, b):
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))

#5
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))

#6
def sum3(nums):
    return sum(nums)

print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))

#7
def max_end3(nums):
    max_num = max(nums[0], nums[-1])
    return [max_num] * 3

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

#8
def make_ends(nums):
    return [nums[0], nums[-1]]

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))

#9
def make_pi():
    return [3, 1, 4]

print(make_pi())

#10
def rotate_left3(nums):
    return nums[1:] + nums[:1]

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))

#11
def sum2(nums):
    return sum(nums[:2])

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))

#12
def has23(nums):
    return 2 in nums or 3 in nums

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))
