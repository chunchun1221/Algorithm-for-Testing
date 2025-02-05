"""解题思路：
    1、维护一个窗口，窗口是可变窗口
    2、如果"""

def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    209. 长度最小的子数组 - 滑动窗口解法
    :param target: 目标和
    :param nums: 正整数数组
    :return: 最小子数组长度
    """
    if target ==0:
        return 0

    if any(num<0 for num in nums):
        raise ValueError('数组包含负数，无法处理')
    left=0
    min_len=float('inf')#假设为无穷大，那么比较大小的时候就可以用了
    current_sum=0

    for right in range(len(nums)):
        #先往窗口里面去扩展
        current_sum+=nums[right]

        #然后用循环
        while current_sum>=target:
            min_len=min(min_len,right-left+1)
            current_sum-=nums[left]
            left+=1

    return min_len if min_len != float('inf') else 0
