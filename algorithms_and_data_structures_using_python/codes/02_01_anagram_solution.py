# 简化问题为两个字符串的长度相同，只包含26个字母


# 解法1
def anagram_solution1(s1, s2):
    # 转为list的目的是，如果某个字符匹配过了，则擦除
    lst_s2 = list(s2)
    equal = True
    for i in s1:
        found = False
        j = 0
        while j < len(s2) and not found:
            if i == lst_s2[j]:
                lst_s2[j] = None
                found = True
            j += 1
        if not found:
            equal = False
            break
    return equal


def anagram_solution1_1(s1, s2):
    """
    教程的方法，list中已经对比成功的元素置为None,避免重复使用
    """
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1

    return still_ok

# 解法2

def anagram_solution2(s1, s2):
    lst1 = list(s1)
    lst2 = list(s2)
    
    lst1.sort()
    lst2.sort()

    print(lst1 == lst2)  # 返回Tue， 这个比较的复杂度是不是O(n)???
    
    matched = True
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            matched = False
    return matched


# 解法4：技术比较法
def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    for i in range(len(c1)):
         if c1[i] != c2[i]:
             return False

    return True


def anagram_solution4_2(s1, s2):
    d1 = {}
    d2 = {}
    
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
        
    print(d1, d2)
    print(d1 == d2)  # 这里的复杂度是多少？？？

    for k, v in d1.items():
        if k not in d2 or v != d2[k]:
            return False
        
    return True
    



if __name__ == '__main__':
    # print(anagram_solution1('heaat', 'heeat'))
    # print(anagram_solution2('heart', 'earth'))
    print(anagram_solution4_2('heart', 'earth'))
