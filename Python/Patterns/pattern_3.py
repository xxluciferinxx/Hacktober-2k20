n=int(input())
i=1
while i<=n:
    space=1
    while space<=i-1:
        print(" ", end="")
        space+=1
        
    num=i
    while num<=n:
        print(num, end="")
        num+=1
    print()
    i+=1
i=n-1
while i>=1:
    space=i
    while space>=2:
        print(" ", end="")
        space-=1   
    num=i
    while num<=n:
        print(num, end="")
        num+=1
    print()
    i-=1


    """
    input : 6
    output : 
    123456
     23456
      3456
       456
        56
         6
        56
       456
      3456
     23456
    123456

    """