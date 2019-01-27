A=0 #sum of odds
B=0 #sum of evens
C=0 #odd count:
D=0 #even count:
E=0 #total positive int count

while E!=-1:
    E+=1
    integer_choice=input("Input an integer (0 terminates): ")
    integer_choice=int(integer_choice)
    if integer_choice==0:
        E-=1
        break
    elif integer_choice %2 ==0 and integer_choice>0 == 0:
        A+=0
        B+=integer_choice
        C+=0
        D+=1
    elif integer_choice < 0 and integer_choice %2 == 0:
        print("Sorry, no negative values please!")
        A+=0
        B+=0
        C+=0
        D+=0
        E-=1
    elif integer_choice <0 and integer_choice%1 == 0:
        print("Sorry, no negative values please!")
        A+=0
        B+=0
        C+=0
        D+=0
        E-=1
    else:
        A+=integer_choice
        B+=0
        C+=1
        D+=0

print("sum of odds:",A)
print("sum of evens:",B)
print("odd count:",C)
print("even count:",D)
print("total positive int count:",E)
