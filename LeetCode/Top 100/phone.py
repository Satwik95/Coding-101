def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits is None:
        return digits
    keypad = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    res = []

    def bfs(cur, index):
        if index == len(digits):
            res.append(cur)
            return
        temp = keypad[int(digits[index])]
        for i in range(len(temp)):
            bfs(cur + temp[i], index + 1)

    bfs("", 0)
    return res

print(letterCombinations("23"))