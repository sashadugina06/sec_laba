a=float(input())
b=float(input())
c=float(input())
disc=b**2-4*a*c
if disc<0:
    print('no')
elif disc>0:
    print('x1=',(-b +(disc**0.5))/(2*a), 'x2=',(-b - (disc**0.5))/(2*a))
elif disc==0:
    print('x1=',(-b)/(2*a) )