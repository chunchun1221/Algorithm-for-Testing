def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    :param intervals:
    :return:
    """
    #先定义一个列表来存储内容
    merge=[]
    #排序
    intervals.sort(key=lambda x:x[0])

    for interval in intervals:
        #r如果内容为空，或者最右边的元素比这个最左边的元素小的话，就是没有交集，就加入到结果里面
        if not merge or merge[-1][1]<interval[0]:
            merge.append(interval)
        else:
            merge[-1][1]=max(merge[-1][1],interval[1])
    return merge


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(intervals))