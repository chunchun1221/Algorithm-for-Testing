def inPalindrome(s: str) -> bool:
    """
    判断一个字符串是否为回文串
    """
    #字符过滤
    sgood=''.join(cha.lower() for cha in s if cha.isalnum())
     #双指针处理
    left,right=0,len(sgood)-1
    while left<right:
        if sgood[left]!=sgood[right]:
            return False
        left+=1
        right-=1
    return True

if __name__=='__main__':
    print(inPalindrome('A man, a plan, a canal: Panama'))
