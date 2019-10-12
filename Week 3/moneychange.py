# Uses python3
import sys
def get_change(m):
    deno = [1,5,10] 
    n = len(deno) 
      
    # Initialize Result 
    ans = [] 
  
    # Traverse through all denomination 
    i = n - 1
    while(i >= 0): 
          
        # Find denominations 
        while (m >= deno[i]): 
            m -= deno[i] 
            ans.append(deno[i]) 
  
        i -= 1
  
   
    print(len(ans))

if __name__ == '__main__':
    m = int(sys.stdin.read())
    get_change(m)
#def min_coins(coin_value,n,amount):
#while loop is needed since one coin can be used multiple times
