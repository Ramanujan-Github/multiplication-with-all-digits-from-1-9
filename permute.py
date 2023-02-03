from itertools import permutations

a=permutations([1,2,3,4,5,6,7,8,9],9)
c=list(a)
for i in range(len(c)):
    b=list(c[i])
    for j in range(len(b)):
        x=int(str(b[0])+str(b[1]))
        y=int(str(b[2])+str(b[3])+str(b[4]))
        z=int(str(b[5])+str(b[6])+str(b[7])+str(b[8]))
        w=int(str(b[0]))
        v=int(str(b[1])+str(b[2])+str(b[3])+str(b[4]))
        t=int(str(b[5])+str(b[6])+str(b[7])+str(b[8]))
        if x*y==z:
            print(b)
        elif w*v==t:
            print(b)


