class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, o = len(s1), len(s2), len(s3)
        if n + m != o:
            return False
        
        s = set([(n,m)])
        while s:
            ns = set()
            for (i,j) in s:
                if (i,j) == (0,0):
                    return True
                if 0 <= i-1 < n and s3[i + j - 1] == s1[i - 1]:
                    ns.add((i-1, j))
                if 0 <= j -1 < m and s3[i + j - 1] == s2[j -1]:
                    ns.add((i,j - 1))
            s = ns
        return False