import math


def zin_find_K(K_o, q, n):
    K_n = K_o * (1+q/100)**n
    return round(K_n,2)

def zin_find_n(K_o, q, K_n):
    K = K_n / K_o
    q = 1+q/100
    n = math.log(K,10) / math.log(q,10)
    return round(n,2)

def zin_find_init_K(K_n, q, n):
    K_o = K_n / (1+q/100)**n
    return round(K_o,2)

def zin_find_rate(K_o, n, K_n):
    q = (K_n / K_o)**(1/n)
    return round(q,2)


def rent(K_o, r, q, n, o1, o2, o3):
    '''Input: K_o (=owned Kapital); r (=rente); q (=rate); t (=time); o1(=if vorschüssiger or nachschüssiger); o2 (= if a Kaptial already own); o3 (=if merhung or mindrung))'''
    q = (1+q/100)
    if o1 == True: # if True => vor
        if o2 == True: # if K_o
            if o3 == True: # if mehrung oder minderung
                K_n = K_o * q**n + (r * q * ((q**n - 1) / (q - 1)))
            else: 
                K_n = K_o * q**n - (r * q * ((q**n - 1) / (q - 1)))
        else: K_n = r * q * ((q**n -1) / (q-1))
        return round(K_n,2)

    if o1 == False: # if False => nach
        if o2 == True: # if K_o
            if o3 == True: # if mehrung or minderung
                K_n = K_o * q**n + (r * ((q**n - 1) / (q - 1)))
            else: 
                K_n = K_o * q**n - (r * ((q**n - 1) / (q - 1)))
        else: K_n = r * ((q**n -1) / (q-1))
        return round(K_n,2)



x = rent(0,50,2.25,3, True, False, True)
print(x)



