import random
import math
xored_str=""
key=""
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
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'   

def DNA_coding_encrypt(a,key,e,n1):
    
    
    DNA_code={
    "00": "A",
    "01": "T",
    "10": "G",
    "11": "C"
      }
    n=len(a)
    DNA_CODED_STR=""
    for i in range(0,int(n),2):
        c=""
        c=str(a[i:i+2])
        DNA_CODED_STR+=str(DNA_code.get(str(c)))
      
    KEY_COM={
        "AA": 0,
        "AT": 1,
        "AG": 2,
        "AC": 3,
        "TA": 4,
        "TT": 5,
        "TG": 6,
        "TC": 7,
        "GA": 8,
        "GT": 9,
        "GG": 10,
        "GC": 11,
        "CA": 12,
        "CT": 13,
        "CG": 14,
        "CC": 15
        }
    ceasar_list=["0101","0011","0001","0010","0110","1111","0111","1001","1010","0100","1000","1100","1110","1011","0000","1101"]
    random.shuffle(ceasar_list)
    
    key_1=""
    for i in ceasar_list:
        key_1+=i

    key=key_1+key
    

    a1=key[0:24]
    b1=key[24:48]
    c1=key[48:72]
    k1=""
    k2=""
    k3=""
    for i in range(0,len(a1),8):
        y1=str(int(a1[i:i+8],2))
        if(len(y1)==1):
            k1+='00'+y1
        if(len(y1)==2):
            k1+='0'+y1
        if(len(y1)==3):
            k1+=y1
          
    for i in range(0,len(b1),8):
        y1=str(int(b1[i:i+8],2))
        if(len(y1)==1):
            k2+='00'+y1
        if(len(y1)==2):
            k2+='0'+y1
        if(len(y1)==3):
            k2+=y1
    for i in range(0,len(c1),8):
        y1=str(int(c1[i:i+8],2))
        if(len(y1)==1):
            k3+='00'+y1
        if(len(y1)==2):
            k3+='0'+y1
        if(len(y1)==3):
            k3+=y1
    


    

    c=(power(int(k1),e,n1)%n1)
    c_1=(power(int(k2),e,n1)%n1)
    c_2=(power(int(k3),e,n1)%n1)
    
    

    
   
    key=text_to_bits(str(e))+'/'+text_to_bits(str(c))+'/'+text_to_bits(str(c_1))+'/'+text_to_bits(str(c_2))+'/'
    
    

    EXP_STR=""
   
    for i in range(0,int(n/2),2):
        d=KEY_COM.get((DNA_CODED_STR[i:i+2]))
       
        EXP_STR+=str(ceasar_list[d])
     
    return key+EXP_STR    
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

def power(x,y,n):
    temp = 0
    if (y == 0):
        return 1
    temp = power(x, int(y / 2),n)
    if (y % 2 == 0):
        return ((temp%n)*(temp%n))%n;
    else:
        return ((x%n)*(temp%n)*(temp%n))%n; 


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def start_encrypt(str1):
    n=len(text_to_bits(str1))
    wq=math.ceil( float(math.log(n)/math.log(2)))
    y=int((math.pow(2,wq)-n)/8)
    for i in range(0,y,1):
        str1+="%"
    res=text_to_bits(str1)

    p =35089
    q =49031

    

    n = p * q
    phi = (p-1) * (q-1)
    e = 1505750551
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
       
    d = modInverse(e,phi)
    
    z=8
    
    key=res[0:z]
   
    xored_str=""
    cr=math.pow(2,wq)
    while z<cr:
        ka=res[0:z]
        kb=res[z:2*z]
        xored=xor(ka,kb,z)
        xored_str+=xored
        z+=z
    
    Encrypted_strn=DNA_coding_encrypt(xored_str,key,e,n)
    
    
    return (Encrypted_strn)
