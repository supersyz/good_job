##第一种做法搞成暴力求解了
##说明没有理解什么是滑动窗
##首先，暴力求解是两层循环，但是滑动窗只要一层循环
#滑动窗口的核心是思考如果只扫描一遍就能得到结果

###滑动窗口思路：
##fast为条件，扫描一遍，那么需要思考的是：每次fast移动后，slow该怎么定位到新的位置？
##思考： fast超前走肯定是要走到满足字符处，此时字典中对应字符会+1
##那么，slow的移动？ 可以想到是每移动到对应字符就-1

##最开始想的是减到没有，但是不对，应该是减到跟目标字符转化字典相同为止。

##第二种思路应该是对的，但是对边界条件处理一坨屎，应该是时间比较长的原因。

##滑动窗口总结：
##fast移动，扫描一遍截止， 随着fast走动思考slow该怎么以不暴力搜索的方式移动
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        import copy
        s_ls = list(s)
        t_ls = list(t)
        len_s_ls = len(s_ls)
        len_t_ls = len(t_ls)
       # s_dic = Counter(s)
        t_dic = Counter(t)
        temp_t_dic = copy.deepcopy(t_dic)
        #print(s_dic,t_dic)
        ans = []
        final_ans = []
        len_ans = len(s_ls) + 1

        if len_s_ls < len_t_ls:
            return ''
        
        fast,slow = 0,0


        while slow < len_s_ls:
            count = 0
            flag = False
            if s_ls[slow] in t_dic:
                fast = slow
 
                while fast < len_s_ls:

                    ans.append(s_ls[fast])
                    if s_ls[fast] in temp_t_dic:
                        count += 1
                        if count == 2:
                            slow = fast
                            flag = True
                    if s_ls[fast] in t_dic:
                        t_dic[s_ls[fast]] -= 1
                        if t_dic[s_ls[fast]] == 0:
                            t_dic.pop(s_ls[fast])
                    if len(t_dic) == 0:
                        break
                    fast += 1

                if len(t_dic) == 0:
                    if len(ans)<len_ans:
                        len_ans = len(ans)
                        final_ans = ans

                t_dic = copy.deepcopy(temp_t_dic)
                ans = []
            if not flag:
                slow += 1
        if len_ans == len(s_ls) + 1:
            final_ans = []
        final_ans = ''.join(final_ans)
        return final_ans
    
    
    


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        import copy
        s_ls = list(s)
        t_ls = list(t)
        len_s_ls = len(s_ls)
        len_t_ls = len(t_ls)
       # s_dic = Counter(s)
        t_dic = Counter(t)
        temp_t_dic = copy.deepcopy(t_dic)
        #print(s_dic,t_dic)
        ans = []
        lenth = len_s_ls + 1
        s,f = 0,0
        len_ans = len(s_ls) + 1

        if len_s_ls < len_t_ls:
            return ''
        fast,slow = 0,0
        count = 0
        ans_counter = Counter()
        while fast < len_s_ls:
            ans.append(s_ls[fast])
            if s_ls[fast] in temp_t_dic:
                ans_counter[s_ls[fast]] += 1
                count += 1
                if count == 1:
                    slow = fast
            if s_ls[fast] in t_dic:
                t_dic[s_ls[fast]] -= 1
                
                if t_dic[s_ls[fast]] == 0:
                    t_dic.pop(s_ls[fast])
            fast += 1
            if len(t_dic) == 0:
                break
            
        
        if len(t_dic) != 0:
            return ''

        len_ans_counter = len(ans_counter)
        s,f = slow,fast
        lenth = f - s 


        while (slow < fast):
            if s_ls[slow] in ans_counter:
                if ans_counter[s_ls[slow]] == temp_t_dic[s_ls[slow]]:
                    break
                else:
                    ans_counter[s_ls[slow]] -= 1
            slow += 1
        
        if (fast - slow ) <lenth:
            f = fast 
            s = slow
            lenth = fast - slow 


        while fast < len_s_ls:
            if s_ls[fast] in ans_counter:
                ans_counter[s_ls[fast]] += 1
                while (slow <= fast):
                    if s_ls[slow] in ans_counter:
                        if ans_counter[s_ls[slow]] == temp_t_dic[s_ls[slow]]:
                            break
                        else:
                            ans_counter[s_ls[slow]] -= 1
                    slow += 1

            fast += 1
            if (fast - slow ) <lenth:
                f = fast
                s = slow
                lenth = fast - slow 
                    

        if lenth == len(s_ls) + 1:
            final_ans = []
        else:
            final_ans = s_ls[s:f]
        final_ans = ''.join(final_ans)
        return final_ans
    
    



#官方思路：先向右滑动快指针，再收缩左边慢指针
 class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return '' 

        from collections import Counter
        dic_t = Counter(t)
        cnt = len(t)
        

        slow,fast = 0,0
        ans = len(s) + 1
        f_s,f_f = 0,len(s)+1
        while fast < len(s):
            if s[fast] in t:
                dic_t[s[fast]] -= 1
                if dic_t[s[fast]] >= 0:
                    cnt -= 1

            while cnt == 0:
                if s[slow] in t:
                    dic_t[s[slow]] += 1
                    if dic_t[s[slow]] > 0:
                        cnt += 1
                
                if fast - slow + 1 < ans:


                    f_s,f_f = slow,fast
                    ans = fast - slow + 1
                


                slow += 1 


            fast += 1
        if f_f == len(s)+1:
            return ''
        return s[f_s:f_f+1]