import random
import math
def xor(a, b, n):
  
    ans = "" 
    for i in range(n):  
        if (a[i] == b[i]):  
            ans += "0"
        else:  
            ans += "1"
    return ans 

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    str=""
    for i in range(0,len(bits),8):
        y=chr(int(bits[i:i+8],2))
        str+=y
    return str

   


def DNA_coding_decrypt(a,cea_list):
    Com_strn=""
    KEY_COM=[]
    for i in range(0,len(cea_list),4):
        r=""
        r=cea_list[i:i+4]
        KEY_COM.append(r)
    decr_li=["AA","AT","AG","AC","TA","TT","TG","TC","GA","GT","GG","GC","CA","CT","CG","CC"]
    res = {} 
    for key in KEY_COM: 
        for value in decr_li: 
            res[key] = value 
            decr_li.remove(value) 
            break 
   
    for i in range(0,len(a),4):
        d=str(res.get((a[i:i+4])))
        
        Com_strn+=d

    DNA_code={
        "A":"00",
        "T":"01",
        "G":"10",
        "C":"11"    
        }
    DNA_decoded_strn=""
    for i in Com_strn:

        DNA_decoded_strn+=str(DNA_code.get(str(i)))
    
    return DNA_decoded_strn    
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def power(x,y,n):
    temp = 0
    if (y == 0):
        return 1
    temp = power(x, int(y / 2),n)
    if (y % 2 == 0):
        return ((temp%n)*(temp%n))%n;
    else:
        return ((x%n)*(temp%n)*(temp%n))%n;
def decimalToBinary(n):
    return '{0:08b}'.format(n)
def start_decrypt(Encrypted_strn):
    kee=Encrypted_strn.split('/')
    e=text_from_bits(kee[0])
    c=kee[1]
    c_1=kee[2]
    c_2=kee[3]
    
    Encrypted_strn=kee[4]
    p =35089
    q =49031
    n = p * q
    phi = (p-1) * (q-1)
  
       
    d = modInverse(int(e),phi)
    
    be=""
    d_1=power(int(text_from_bits(c)),d,n)%n
    d_2=power(int(text_from_bits(c_1)),d,n)%n
    d_3=power(int(text_from_bits(c_2)),d,n)%n
    if(len(str(d_1))==8):
        d_1='0'+str(d_1)
    if(len(str(d_1))==7):
        d_1='00'+str(d_1)
    if(len(str(d_2))==8):
        d_2='0'+str(d_2)    
    if(len(str(d_2))==7):
        d_2='0'+str(d_2)
    if(len(str(d_3))==8):
        d_3='0'+str(d_3)    
    if(len(str(d_3))==7):
        d_3='0'+str(d_3)
    
   
    be+=(str(d_1)+(str(d_2)+str(d_3))) 
    
    ans="" 
    for i in range(0,len(be),3):
        ans+=str(decimalToBinary(int(be[i:i+3])))
    
    cea_list=""
    cea_list=ans[0:64]
    key=""
    key=ans[64:72]
    mess=""
    mess=Encrypted_strn
    z=8
    y=0
    
    Decrypt_Binary=DNA_coding_decrypt(mess,cea_list)
    while z<=len(Decrypt_Binary):
        kb=Decrypt_Binary[y:z]
        xored=xor(key,kb,len(key))
        key+=xored
        y=z
        z+=len(key)
    
    ans=text_from_bits(key)
    ans=ans.split('%') 
    return ans[0]
