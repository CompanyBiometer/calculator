print("Дробь 1: a b/c")
a,b,c = map(int, input().split())
print("Действие")
run = input()
print("Дробь 2: a b/c")
a2,b2,c2 = map(int, input().split())
def okrug1(b,c):
    if c < b:
        for j in range(c):
            for i in range(c):
                if b % (i + 2) == 0 and c % (i + 2) == 0:
                    b = b / (i + 2)
                    c = c / (i + 2)
                    b = int(b)
                    c = int(c)

                    
    if b < c:
        for j in range(b):
            for i in range(b):
                if b % (i + 2) == 0 and c % (i + 2) == 0:
                    b = b / (i + 2)
                    c = c / (i + 2)
                    b = int(b)
                    c = int(c)
    print(b,"/",c)
    return (b,c)
                    
def okrug2(b,c):
    if b > c:
        
        a = int(b / c)
        b = int(b % c)
        print(a,b,"/",c)
    elif b == c:
        print("1")
    elif b < c:
        print(b,"/",c)





q1 = (a*c)+b
q2 = (a2*c2)+b2

print("")
print(q1,"/",c)
print(run)
print(q2,"/",c2)
print("Ответ:")
if(run == "/"):
    print(q1*c2,"/",q2*c)
    print((q1*c2)//(q2*c),"[",(q1*c2)-(((q1*c2)//(q2*c))*(q2*c)),"/",q2*c,"]")
    
if(run == "*"):
    b = q1
    b2 = q2
    print(b*b2,"/",c*c2)
    (b,c) = okrug1(b * b2,c * c2)
    print("Ответ:")
    okrug2(b,c)
if(run == "+"):
    obz = c*c2
    b = q1 * c2
    b2 = q2 * c
    print(b + b2,"/",obz)
    (b,c) = okrug1(b + b2,obz)
    print("Ответ:")
    okrug2(b,c)

    
if(run == "-"):
    obz = c*c2
    b = q1 * c2
    b2 = q2 * c
    print(b - b2,"/",obz)
    (b,c) = okrug1(b - b2,obz)
    print("Ответ:")
    okrug2(b,c)
    
    
    
