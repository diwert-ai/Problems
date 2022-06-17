class Solution:
    def __init__(self):
        self.max_sum=0
        self.result=[]
        self.ops=0
        
    def add_variant(self,cur_sum,l):
        
        if len(l) == 2*self.max_sum:
            if cur_sum == 0:
                self.result.append(l)
            return

        self.ops+=1
        if cur_sum < self.max_sum:
            self.add_variant(cur_sum+1,l+'(')
        
        if cur_sum > 0:
            self.add_variant(cur_sum-1,l+')')
        
        return
        
            
    def generateParenthesis(self, n: int) -> list[str]:
        self.max_sum = n      
        self.add_variant(0,'')      
        return self.result


def next_step(cur_sum,max_sum, max_len,l):

    if len(l) == max_len:
        if cur_sum == 0:
            print(l,len(l),' ok!')      
        return

    if cur_sum<max_sum:
        next_step(cur_sum+1,max_sum,max_len,l+'(')

    if cur_sum>0:
        next_step(cur_sum-1,max_sum,max_len,l+')')

    return


if __name__ == '__main__':
    #next_step(0,2,4,'')
    l = []
    n=15
    for i in range(n):
        sol = Solution()
        sol.generateParenthesis(i)
        l.append(sol.ops)

    for i in range(1,n-1):
        print(l[i+1]/l[i])
        

