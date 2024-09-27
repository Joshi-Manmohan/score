class solution :
    def maxRegions(self,n):
        M = 1000000007
        num = ((n*(n+1))//2)+1
        return num % M
    
if __name__ == '__main__':
    n= int(input())
    ob= solution()
    ans = ob.maxRegions(n)
    print(ans)
