import math
import re

def zins(st):
    '''
    Input: zins(K_n = K_o * p^n) == zins(K_n;K_o;p;n)
    Note: if you use the 1st instance make sure to have space between operators
    '''
    ls = re.split(";| = | \* |\^",st)
    if ls[0] == "K_n":
        #parsing input
        #fK_n = float(ls[0])= missing 
        K_o = float(ls[1])
        p = float(ls[2])
        n = float(ls[3])
        K_n = K_o * (1+p/100)**n
        return round(K_n,2)

    if ls[1] == "K_o":
        #parsing input
        K_n = float(ls[0])
        #K_o = float(ls[1]) = missing
        p = float(ls[2])
        n = float(ls[3])
        #calc
        K_o = K_n / (1+p/100)**n
        return round(K_o,2)

    if ls[2] == "p":
        #parsing input
        K_n = float(ls[0])
        K_o = float(ls[1])
        #p = float(ls[2]) = missing
        n = float(ls[3])
        #calc
        q = (K_n / K_o)**(1/n)
        p = (q-1) *100
        return round(p,2)

    if ls[3] == "n":
        #parsing input
        K_n = float(ls[0])
        K_o = float(ls[1])
        p = float(ls[2])
        #n = float(ls[3]) missing
        #calc
        K = K_n / K_o
        q = 1+q/100
        n = math.log(K,10) / math.log(q,10)
        return round(n,2)



def rent(K_o, r, q, n, o1=True, o2=False, o3=True):
    '''
    Input: K_o (=owned Capital >> 0 if not); r (=rent); q (=rate); t (=time)
    Option: o1(=if in advance or afterwords); o2 (= if a Capital already own); o3 (=if increase or decrease)
    '''
    q = (1+q/100)
    if o1 == True: # if True => in advance
        if o2 == True: # if K_o owned
            if o3 == True: # if increase or decrease
                K_n = K_o * q**n + (r * q * ((q**n - 1) / (q - 1)))
            else: 
                K_n = K_o * q**n - (r * q * ((q**n - 1) / (q - 1)))
        else: K_n = r * q * ((q**n -1) / (q-1))
        return round(K_n,2)

    if o1 == False: # if False => afterword
        if o2 == True: # if K_o owned
            if o3 == True: # if increase or decrease
                K_n = K_o * q**n + (r * ((q**n - 1) / (q - 1)))
            else: 
                K_n = K_o * q**n - (r * ((q**n - 1) / (q - 1)))
        else: K_n = r * ((q**n -1) / (q-1))
        return round(K_n,2)



print(zins.__doc__)
x = zins("8000 = 6700 * p^12") # or "zins(8000;6700;p;12)" work as well
print(x)

print(rent.__doc__)
x = rent(0,50,2.25,3)
print(x)




# def zin_find_K(K_o, q, n):
#     K_n = K_o * (1+q/100)**n
#     return round(K_n,2)

# def zin_find_n(K_o, q, K_n):
#     K = K_n / K_o
#     q = 1+q/100
#     n = math.log(K,10) / math.log(q,10)
#     return round(n,2)

# def zin_find_init_K(K_n, q, n):
#     K_o = K_n / (1+q/100)**n
#     return round(K_o,2)

# def zin_find_rate(K_o, n, K_n):
#     q = (K_n / K_o)**(1/n)
#     return round(q,2)

