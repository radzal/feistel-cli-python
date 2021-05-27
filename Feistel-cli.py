# Feistel Cipher Structure
# Code presents structure implementation
# Aims to prove that the same block of code is used
# for encryption and decryption.
# 2020
  
import binascii 
import random 

keyList = []
# ---- Random bits key generation ----
def rand_key(p): 
    key = "" 
    for i in range(p): 
        key += str(random.randint(0,1)) 
    return(key) 

# ---- Bit xor ----
def exor(a,b): 
    xor_ed = ""  
    for i in range(n):
        if (a[i] == b[i]): 
            xor_ed += "0"              
        else:  
            xor_ed += "1"
    return xor_ed

# ---- rounding block function ----
def rounds(L, R, K):            # encode function
    R_new = exor(exor(R,K),L)   # xor right with key, xor xored with left
    L_new = R                   # swap sides
    return L_new, R_new         # return values
  
# ==== PRE-PROCESSING ====
# Text input and print out 
plain = input('Input text: ')
nrOfRnds = int(input('Input rounds number: '))
print("Plain Text is:\t", plain)
print("Round number:\t", rounds)

# Text to ASCII 
plain2ascii = [ord(x) for x in plain] 
  
# ASCII to # 8-bit binary 
ascii2bin = "".join([format(b,'08b') for b in plain2ascii]) 
  
n = int(len(ascii2bin)//2)  # two halves
Left, Right = ascii2bin[0:n], ascii2bin[n::]  

# ---- end of pre-processing ----  

# ==== Generating list with keys ===
for i in range(nrOfRnds):                   # appending keys to list
    keyList.append(rand_key(len(Right)))    # for key lenth used half's lenth 
    
# ==== ENCRYPTION ====
# ---- Encoding rounds ----
for i in range(nrOfRnds):
    Left, Right = rounds(Left, Right, keyList[i])
# ---- end of encryption ----

# ==== POST-ENCRYPTION PROCESSING ====
# text converting
bin_data = Left + Right #joining two halves
str_data =' '
  
for i in range(0, len(bin_data), 7):    
    str_data += chr(int(bin_data[i:i + 7], 2) )
print("\nCipher Text: ->>" + str_data + "<<-")
# ---- end of Post-Encryption Processing

# ==== DECRYPTION ====
keyList.reverse()   # Reverse keyList order for decryption

# ---- Decoding round -----
# Decryption: Loop each time swaps Left and Right before use encription function
# round function is used for both processes (encryption and decryption)
for i in range(nrOfRnds):
    Left, Right = Right, Left
    Right, Left = rounds(Left, Right, keyList[i])
# ---- end of encryption ----
    
# ========= POST-ENCRYPTION PROCESSING =======
# Jojning halves, grouping to integers, converting hexadecimal string to binary
# decode in UTF-8
print(binascii.unhexlify( '%x'% int(Left+Right, 2)).decode("utf-8"))
# ---- end of program ----
