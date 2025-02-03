def check_inclusion(s1: str, s2: str) -> bool:
    """
    567. 字符串的排列 - 滑动窗口解法
    - 测试场景映射：检测日志中是否存在连续N次相同错误码
    - 时间复杂度：O(n)，适合实时监控场景
    """
    from collections import defaultdict
    need = defaultdict(int)
    for c in s1:
        need[c] += 1

    left = 0
    window = defaultdict(int)
    valid = 0  # 满足条件的字符数

    for right in range(len(s2)):
        c = s2[right]
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 窗口收缩条件：窗口长度≥s1长度
        while right - left + 1 >= len(s1):
            if valid == len(need):
                return True
            left_c = s2[left]
            if left_c in need:
                if window[left_c] == need[left_c]:
                    valid -= 1
                window[left_c] -= 1
            left += 1

    return False