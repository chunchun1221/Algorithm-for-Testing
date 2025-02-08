from collections import Counter


def fin_anagrams(s: str, p: str)-> list[int]:
    """
    438. 找到字符串中所有字母异位词
    :param s: 字符串
    :param p: 字符串
    :return: 字符串中每个字母异位词的起始索引
    """
    if len(s) < len(p):
        return []

    p_count=Counter(p)
    window_count=Counter()
    left=0
    reslut=[]

    for right in range(len(s)):
        window_count[s[right]]+=1

        if right-left+1>len(p):
            window_count[s[left]]-=1
            if window_count[s[left]]==0:
                del window_count[s[left]]
            left+=1
        if right-left+1==len(p) and window_count==p_count:
            reslut.append(left)
    return reslut

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(fin_anagrams(s, p))