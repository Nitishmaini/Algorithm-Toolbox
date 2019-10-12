# python3
import sys


def countRefill(N, K, M, compulsory): 
    count = 0
    i = 0
    distCovered = 0
  
    # While we complete the whole journey. 
    while (distCovered < N): 
          
        # If must visited petrol pump lie 
        # between distCovered and distCovered+K. 
        if (i < M and compulsory[i] <= (distCovered + K)): 
              
            # make last mustVisited as distCovered 
            distCovered = compulsory[i] 
  
            # increment the index of  
            # compulsory visited. 
            i += 1
  
        # if no such must visited pump is 
        # there then increment distCovered by K. 
        else: 
            distCovered += K 
  
        # Counting the number of refill. 
        if (distCovered < N): 
            count += 1
  
    return count


if __name__ == '__main__':
    N=int(input())
    K=int(input())
    M=int(input())
    compulsory=list(map(int,input().split()))
    print(countRefill(N, K, M, compulsory))

