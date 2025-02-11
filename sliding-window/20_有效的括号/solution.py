def isVail(s:str)->bool:
    stack=[]#用堆栈来判断是否是有效括号
    kuohao_map={')':'(','}':'{',']':'['}#用哈希表来搞映射

    for cha in s:
        if cha in kuohao_map:
            if stack and stack[-1]!=kuohao_map[cha]:
                return False
            stack.pop()
        else:
            stack.append(cha)

    return not stack


