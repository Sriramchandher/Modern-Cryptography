from pyfinite import ffield

Field = ffield.FField(7)

powr = {}

dict = {0:'f',
        1:'g',
        2:'h',
        3:'i',
        4:'j',
        5:'k',
        6:'l',
        7:'m',
        8:'n',
        9:'o',
        10:'p',
        11:'q',
        12:'r',
        13:'s',
        14:'t',
        15:'u',}

for x in range(0,128):
    powr[x] = {}

def byte_str(k):
    res = ""
    res += dict[int(k/16)]
    n = k%16
    res += dict[n]
    return res

def str_block(ch):
    res = 16*(ord(ch[0])-ord('f')) + 1*(ord(ch[1])-ord('f'))
    return res

def cal_powr(base, n):
    if base in powr:
        if n in powr[base]:
            return powr[base][n]
        
    if base == 1:
        return 1
    
    result = 0
    if n == 0:
        result = 1
    elif n == 1:
        result = base
    elif n%2 == 0:
        base_root = cal_powr(base, n>>1)
        result = Field.Multiply(base_root, base_root)
    else:
        base_root = cal_powr(base, n>>1)
        result = Field.Multiply(base_root, base_root)
        result = Field.Multiply(base, result)

    powr[base][n] = result
    return result

def possible_diagonal(plain, cipher, possiAd, possiE, index):

    redu_possiAd = []
    redu_possiE = []

    for A in possiAd:
        for E in possiE:
            ispossible = True
            for i,p in enumerate(plain):
                k = cal_powr( Field.Multiply( cal_powr( Field.Multiply( cal_powr(plain[i][index], E), A), E), A), E)
                if cipher[i][index] != k:
                    ispossible = False
            if ispossible:
                redu_possiAd.append(A)
                redu_possiE.append(E)

    return redu_possiAd, redu_possiE

def break_ties(plain, cipher, possiAd, possiE, index):

    for a in range(0, 128):
        x = 0
        while (len(possiE[index+1])>x):
            y = 0
            while (len(possiE[index])>y):
                flag = True
                for i in range(0, len(plain)):
                    if cipher[i][index+1] != cal_powr(Field.Multiply(cal_powr(Field.Multiply(cal_powr(plain[i][index], possiE[index][y]), possiAd[index][y]), possiE[index][y]), a) ^ Field.Multiply(cal_powr(Field.Multiply(cal_powr(plain[i][index], possiE[index][y]), a), possiE[index+1][x]), possiAd[index+1][x]), possiE[index+1][x]):
                        flag = False
                        break
                if flag:
                    possiE[index+1] = [possiE[index+1][x]]
                    possiAd[index+1] = [possiAd[index+1][x]]
                    possiE[index] = [possiE[index][y]]
                    possiAd[index] = [possiAd[index][y], a]
                y = y+1
            x = x+1

    return possiAd, possiE

def vector_addition(v1, v2):
    res = []
    for i in range(0, len(v1)):
        res.append(v1[i] ^ v2[i])

    return res

def scalar_vector_multi(v1, k):
    res = []
    for i in range(0, len(v1)):
        res.append(Field.Multiply(v1[i], k))

    return res

def applyA(A, v):
    res = [0]*8
    for r, e in zip(A, v):
        res = vector_addition(scalar_vector_multi(r, e), res)

    return res

def applyEAEAE(plain, A, E):
    res = [0]*8
    for i in range(0, len(plain)):
        res[i] = cal_powr(plain[i], E[i])
    
    res = applyA(A, res)

    for i in range(0, len(res)):
        res[i] = cal_powr(res[i], E[i])

    res = applyA(A, res)

    for i in range(0, len(res)):
        res[i] = cal_powr(res[i], E[i])

    return res 

def complete_matrix(plain, cipher, A, E, index):

    for idx in range(0,6):
        offset = idx + 2

        exp = [x[0] for x in E]
        Ad = [[0 for i in range(0,8) ] for j in range(0,8)]

        for i in range(0,8):
            for j in range(0,8):
                Ad[i][j] = 0 if len(A[i][j]) == 0 else A[i][j][0]

        for index in range(0,8):
            if index + offset > 7:
                continue

            plain1 = plain[index*15: (index+1)*15]
            cipher1 = cipher[index*15: (index+1)*15]

            for i in range(0, 128):
                Ad[index][index+offset] = i
                flag = True
                for j,p in enumerate(plain1):
                    if cipher1[j][index+offset] != applyEAEAE(p, Ad, exp)[index+offset]:
                        flag = False
                        break
                if flag:
                    A[index][index+offset] = [i]

    comp_A = [[0 for i in range(0,8)] for j in range(0,8)]

    for i in range(8):
        for j in range(8):
            comp_A[i][j] = 0 if len(A[i][j]) == 0 else A[i][j][0]

    exp = [x[0] for x in E]

    return comp_A, exp

plain = open("plaintext.txt",'r')
cipher = open("ciphertext.txt", 'r')

plain_list = plain.readlines()
cipher_list = cipher.readlines()

plain_list = [x[:-1] for x in plain_list]
cipher_list = [x[:-1] for x in cipher_list]

byte_plain = []
byte_cipher = []

for p in plain_list:
    x = []
    for i in range(0, len(p), 2):
        x.append(str_block(p[i:i+2]))
    byte_plain.append(x)

for c in cipher_list:
    x = []
    for i in range(0, len(c), 2):
        x.append(str_block(c[i:i+2]))
    byte_cipher.append(x)

possiAii = []
possiEi = []

for i in range(0,8):

    possiAd = [ x for x in range(0,128) ]
    possiE = [ x for x in range(0,128) ]

    possiAd, possiE = possible_diagonal(byte_plain[i*15: (i+1)*15], byte_cipher[i*15: (i+1)*15], possiAd, possiE, i)

    possiAii.append(possiAd)
    possiEi.append(possiE)

# print(possiAii)
# print(possiEi)

for i in range(0,7):

    possiAii, possiEi = break_ties(byte_plain[i*15: (i+1)*15], byte_cipher[i*15: (i+1)*15], possiAii, possiEi, i)

# print(possiAii)
# print(possiEi)

A = [ [ [] for x in range(0,8) ] for y in range(0,8) ]
E = [ x[0] for x in possiEi ]

for i in range(0,8):
    for j in range(0,8):
        if i == j:
            A[i][j] = [possiAii[i][0]]
        if i == j-1:
            A[i][j] = [possiAii[i][1]]

comp_A, E = complete_matrix(byte_plain, byte_cipher, A, possiEi, i)

print(comp_A)
print(E)

def Decrypt(password):
    byte_password = []

    for i in range(0, len(password), 2):
        byte_password.append(str_block(password[i:i+2]))

    decrypted_password = ""
    byte_dp = []

    for i in range(0, len(byte_password)):
        for j in range(0, 128):
            check = decrypted_password + byte_str(j) + (16-len(decrypted_password)-2)*'f'
            byte_check = []
            for a in range(0, len(check), 2):
                byte_check.append(str_block(check[a:a+2]))
            if byte_password[i] == applyEAEAE(byte_check, comp_A, E)[i]:
                decrypted_password += byte_str(j)
                byte_dp.append(j)
                break

    return byte_dp

password1 = "msltfplimqhimsim"
password2 = "ltmhlplminksjiir"

byte_dp1 = Decrypt(password1)
byte_dp2 = Decrypt(password2)

print(byte_dp1)
print(byte_dp2)

pass1 = ""
for x in byte_dp1:
    pass1 += chr(x)

pass2 = ""
for x in byte_dp2:
    pass2 += chr(x)

print(pass1+pass2)