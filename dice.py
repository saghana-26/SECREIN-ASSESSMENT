A=[1,2,3,4,5,6]
B=[1,2,3,4,5,6]
n=len(A)
m=len(B)
com=n*m
print("the total number of combinations possible are: ",com)
for i in A:
    for j in B:
        print("(",i,",",j,") ",end='')
    print("\n")

sums=dict()
for i in A:
    for j in B:
        res=i+j
        if res in sums:
            sums[res] +=1
        else: 
           sums[res]=1
        


for i in sums:
    prob=format(sums[i]/com ,".3f")
    output="P(Sum = {})=  {}/{} = {} "
    print(output.format(i,sums[i],com,prob))
    

def undoom_dice(A,B):
    A[0]=1
    A[1]=2
    A[2]=2
    A[3]=3
    A[4]=3
    A[5]=4
    B[0]=1
    B[1]=3
    B[2]=4
    B[3]=5
    B[4]=6
    B[5]=8


undoom_dice(A,B)
print("\nthe new Die A:",A)
print("the new Die B:",B)
undoom_sums=dict()
for i in A:
    for j in B:
        res=i+j
        if res in undoom_sums:
            undoom_sums[res] +=1
        else: 
           undoom_sums[res]=1
        
print("\nThe values of probability of sums after undoomed dice: \n")
l=[*range(2,13)]
for i in l:
    prob=format(undoom_sums[i]/com ,".3f")
    output="P(Sum = {})=  {}/{} = {} "
    print(output.format(i,undoom_sums[i],com,prob))
