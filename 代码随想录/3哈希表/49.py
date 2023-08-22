#笨办法：
##2.排序，满足条件的字符串排序后一致
#3.仅包含小写字母或者大写字母的话，要想到可以用
# a-z的ascii码， 因为记不住a的开头，所以用 ord(ch) - ord('a')来表示一个字符串

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        #from collections import
        ans = []
        dic_ans = []
    
        ans.append([strs[0]])
        dic_ans.append(dict(Counter(strs[0])))
        if len(strs) <= 1:
            return [strs]
        for st in strs[1:]:
            dic_st = dict(Counter(st))
            if dic_st in dic_ans:
                for dic_an in range(len(dic_ans)):
                    if dic_st == dic_ans[dic_an]:
                        ans[dic_an].append(st)
                        
            else:
                dic_ans.append(dic_st)
                ans.append([st])
        return ans
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        #from collections import
        ans = defaultdict(list)
        for st in strs:
            ans[''.join(sorted(st))].append(st)
        return list(ans.values())
        