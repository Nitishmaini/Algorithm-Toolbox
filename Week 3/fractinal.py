# Uses python3
# Python3 program to solve fractional  
# Knapsack Problem
import sys
class ItemValue: 
      
    """Item Value DataClass"""
    def __init__(self, wt, val, ind): 
        self.wt = wt 
        self.val = val 
        self.ind = ind 
        self.cost = val // wt 
  
    def __lt__(self, other): 
        return self.cost < other.cost 
  
# Greedy Approach 
class FractionalKnapSack: 
      
    """Time Complexity O(n log n)"""
    @staticmethod
    def getMaxValue(wt, val, capacity): 
          
        """function to get maximum value """
        iVal = [] 
        for i in range(len(wt)): 
            iVal.append(ItemValue(wt[i], val[i], i)) 
  
        # sorting items by value 
        iVal.sort(reverse = True) 
  
        totalValue = 0
        for i in iVal: 
            curWt = int(i.wt) 
            curVal = int(i.val) 
            if capacity - curWt >= 0: 
                capacity -= curWt 
                totalValue += curVal 
            else: 
                fraction = capacity / curWt 
                totalValue += curVal * fraction 
                capacity = int(capacity - (curWt * fraction)) 
                break
        return totalValue

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    val = data[2:(2 * n + 2):2]
    wt = data[3:(2 * n + 2):2]
    opt_value = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("{:.10f}".format(opt_value))
