def compund_interest(p,t,r,n):
    a=p*((1+r/n))**(n*t)
    return round(a,2)

print(compund_interest(10000,10,0.06,12))
print(compund_interest(100,1,0.05,12))
print(compund_interest(3500,15,0.1,4))
print(compund_interest(100000,20,0.15,365))