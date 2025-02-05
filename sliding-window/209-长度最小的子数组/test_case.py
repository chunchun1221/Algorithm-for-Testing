import pytest
from solution import min_subarray_len  # 替换为实际模块路径

def test_standard_case():
    """常规测试：存在满足条件的子数组"""
    # Case 1: 明确存在最短子数组
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2  # [4,3]
    # Case 2: 多个可能子数组，取最短
    assert min_subarray_len(15, [5, 1, 3, 5, 10]) == 2   # [5,10]

def test_no_valid_subarray():
    """无满足条件的子数组"""
    # Case 1: 数组总和不足
    assert min_subarray_len(100, [1, 2, 3]) == 0
    # Case 2: 空数组
    assert min_subarray_len(1, []) == 0

def test_single_element():
    """单个元素满足条件"""
    # Case 1: 元素直接等于target
    assert min_subarray_len(4, [1, 4, 4]) == 1  # [4]
    # Case 2: 元素大于target
    assert min_subarray_len(3, [1, 5, 2]) == 1  # [5]

def test_minimal_window():
    """最小窗口为整个数组"""
    # Case: 整个数组和恰好等于target
    assert min_subarray_len(10, [1, 2, 3, 4]) == 4  # [1,2,3,4]
    # Case: 整个数组和刚好超过target
    assert min_subarray_len(9, [2, 3, 4, 1]) == 3   # [3,4,1]

def test_boundary_conditions():
    """边界条件测试"""
    # Case 1: target为0（非法输入，但函数应返回0）
    assert min_subarray_len(0, [1, 2, 3]) == 0
    # Case 2: 数组包含负数（根据题意应为正整数数组，但测试容错性）
    with pytest.raises(ValueError):  # 若函数有输入校验
        min_subarray_len(5, [2, -1, 3])



if __name__=="__main__":
    pytest.main()
