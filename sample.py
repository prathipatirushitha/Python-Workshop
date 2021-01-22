"'this is sample of creating module'"
def Is_prime(n):
    if n==1:
        return False
    cnt=0
    for i in range(2,n):
        if n%i==0:
           cnt+=1
           break
    if cnt==0:
        return True
    else:
        return False


def Prime_gen(s,e):
    for i in range(s,e+1):
        if Is_prime(i):
            print(i)



def Is_Perfect(n):
    fc=0
    for i in range(1,n):
        if(n%i==0):
            fc+=i
    if(fc==n):
        return True
    else:
        return False
    
    
def Is_even(n):
    if n%2==0:
        return True
    else:
        return False




