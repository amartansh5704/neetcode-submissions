class Solution:
    def checkValidString(self, s: str) -> bool:
        score = bp = grey = 0
        for c in s:
            if c == '(':
                score += 1
            elif c == ')':
                if score > 0:
                    score -= 1
                elif grey:
                    grey -= 1
                    bp += 1
                elif bp:
                    bp -= 1
                else:
                    return False
            else:
                if score > 0:
                    score -= 1
                    grey += 1
                else:
                    bp += 1
        return score == 0