class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        last = 0
        next_merge = 0
        dont_merge = 1

        for d in s:
            can_merge = 10 <= 10 * last + int(d) <= 26

            if d == '0':
                next_dont_merge = 0
            else:
                next_merge = dont_merge
                next_dont_merge = dont_merge
            
            if can_merge:
                next_dont_merge += merge

            merge = next_merge
            dont_merge = next_dont_merge
            last = int(d)
        return dont_merge
