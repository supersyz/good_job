##注意：不重复，考虑用set数据格式

#divmod函数返回（a // b，a % b)

class Solution:
    def isHappy(self, n: int) -> bool:
        from collections import Counter,defaultdict
        if n == 1:
            return True 

        temps = set()

        while True:

            new_n = sum([int(i)**2 for i in str(n)])

            if new_n in temps:
                return False
            if new_n == 1:
                return True

            n = new_n
            temps.add(new_n)



class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
