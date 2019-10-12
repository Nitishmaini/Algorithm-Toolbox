#python3
def max_pair(x):
    max1=max(x[0],x[1]) 
    secondmax=min(x[0],x[1])
    for b in range(2,len(x)):
        if(x[b]>max1):
            secondmax=max1
            max1=x[b] 
        else: 
            if x[b]>secondmax:
                secondmax=x[b]
    max_product=max1*secondmax
    print(max_product)

    

a=int(input())
x = [int(i) for i in input().split()]
max_pair(x)


# b=len(x)
  #  max_product=0
   # for y in range(b):
    # for z in range(y+1,b):
      #      max_product=max(max_product,x[y]*x[z])
   # print(max_product)
