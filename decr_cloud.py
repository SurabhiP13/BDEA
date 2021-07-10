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
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'   

   


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




def start_decrypt(Encrypted_strn):
    cea_list=""
    cea_list=Encrypted_strn[0:64]
    key=""
    key=Encrypted_strn[64:72]
    mess=""
    mess=Encrypted_strn[72:]
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
    sd=len(ans)-1
    for i in range(len(ans)-1,0,-1):
        if ans[i]=='%':
            sd=sd-1
        else :
            break    
    return ans[:sd]

enc_text=open('encr.txt','r',encoding='utf-8')
ori_text=open('decr.txt','w',encoding='utf-8')
ori_text.write(start_decrypt(enc_text.read()))
