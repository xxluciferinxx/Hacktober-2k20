n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        print("*", end=' ')
        j+=1
    print()
    i+=1

""" 
input : 5
output :
* * * * * 
* * * * 
* * * 
* * 
* 
"""