class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def f_w(num):
            mask = 1
            w = 0

            while num:
                if num& mask:
                    w += 1
                    num^=mask
                mask<<= 1
            return w
        arr.sort(key = lambda num: (f_w(num),num))
        return arr