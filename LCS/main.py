def LCSRecursive(s1, s2, m, n, lcs) -> int:
    if m == 0 or n == 0:
        return 0

    if lcs[m][n]:
        return lcs[m][n]

    if s1[m - 1] == s2[n - 1]:
        lcs[m][n] = 1 + LCSRecursive(s1, s2, m - 1, n - 1, lcs)
    else:
        lcs[m][n] = max(LCSRecursive(s1, s2, m - 1, n, lcs), LCSRecursive(s1, s2, m, n - 1, lcs))

    return lcs[m][n]


def LCSIterative(s1, s2, lcs) -> int:
    m = len(s1)
    n = len(s2)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[m][n]


def findLCS(s1, s2, lcs) -> str:
    m = len(s1)
    n = len(s2)

    lcs_chars = [""] * lcs[m][n]
    idx = lcs[m][n]

    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars[idx - 1] = s1[i - 1]

            i -= 1
            j -= 1
            idx -= 1
        else:
            if lcs[i - 1][j] >= lcs[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return "".join(lcs_chars)


def findAllLCS(s1, s2, m, n, lcs) -> set:
    s = set()

    if m == 0 or n == 0:
        s.add("")
        return s

    if s1[m - 1] == s2[n - 1]:
        tmp = findAllLCS(s1, s2, m - 1, n - 1, lcs)

        for string in tmp:
            s.add(string + s1[m - 1])
    else:
        if lcs[m - 1][n] >= lcs[m][n - 1]:
            s = findAllLCS(s1, s2, m - 1, n, lcs)

        if lcs[m][n - 1] >= lcs[m - 1][n]:
            tmp = findAllLCS(s1, s2, m, n - 1, lcs)

            for string in tmp:
                s.add(string)

    return s


def LCSOptimizedInSpace(s1, s2, lcs) -> int:
    m = len(s1)
    n = len(s2)

    bi = bool

    for i in range(m + 1):
        bi = i & 1
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[bi][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                lcs[bi][j] = 1 + lcs[1 - bi][j - 1]
            else:
                lcs[bi][j] = max(lcs[1 - bi][j], lcs[bi][j - 1])

    return lcs[bi][n]


def LCSOptimizedInSpaceWithOneArray(s1, s2):
    m = len(s1)
    n = len(s2)

    lcs = [0] * (n + 1)

    for i in range(m + 1):
        prev = lcs[0]
        for j in range(n + 1):
            backup = lcs[j]
            if i == 0 or j == 0:
                lcs[j] = 0
            else:
                if s1[i - 1] == s2[j - 1]:
                    lcs[j] = prev + 1
                else:
                    lcs[j] = max(lcs[j], lcs[j - 1])

            prev = backup

    return lcs[n]


def main():
    s1 = "ABCD"
    s2 = "ACBAD"

    if len(s2) > len(s1):
        s1, s2 = s2, s1

    print("LCS with Recursive Method")
    lcs = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    print("LCS Length: {}".format(LCSRecursive(s1, s2, len(s1), len(s2), lcs)))
    print("LCS: {}".format(findLCS(s1, s2, lcs)))
    print("ALL LCS: {}".format(findAllLCS(s1, s2, len(s1), len(s2), lcs)))

    print("\n")

    print("LCS with Iterative Method")
    lcs = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    print("LCS Length: {}".format(LCSIterative(s1, s2, lcs)))
    print("LCS: {}".format(findLCS(s1, s2, lcs)))
    print("ALL LCS: {}".format(findAllLCS(s1, s2, len(s1), len(s2), lcs)))
    for i in range(len(s1) + 1):
        print(lcs[i])

    print("\n")

    print("LCS: Space Optimized Version")
    lcs = [[0 for _ in range(len(s2) + 1)] for _ in range(2)]
    print("LCS Length: {}".format(LCSOptimizedInSpace(s1, s2, lcs)))

    print("\n")

    print("LCS: Space Optimized Version with One Array")
    print("LCS Length: {}".format(LCSOptimizedInSpaceWithOneArray(s1, s2)))


if __name__ == '__main__':
    main()
