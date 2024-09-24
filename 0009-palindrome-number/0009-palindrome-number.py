class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        string = str(x)
        pointerStart = 0
        pointerEnd = len(string) - 1
        while (pointerStart <= pointerEnd):
            if(string[pointerStart] !=  string[pointerEnd]):
                return False
            else:
                pointerStart += 1
                pointerEnd -= 1
        return 1
