import numpy as np

initial_permutation = [[58,50,42,34,26,18,10,2],
                      [60,52,44,36,28,20,12,4],
                      [62,54,46,38,30,22,14,6],
                      [64,56,48,40,32,24,16,8],
                      [57,49,41,33,25,17,9,1],
                      [59,51,43,35,27,19,11,3],
                      [61,53,45,37,29,21,13,5],
                      [63,55,47,39,31,23,15,7]]

final_permutation=  [[8, 40, 16, 48, 24, 56, 32, 64],
                        [7, 39, 15, 47, 23, 55, 31, 63],
                        [6, 38, 14, 46, 22, 54, 30, 62],
                        [5, 37, 13, 45, 21, 53, 29, 61],
                        [4, 36, 12, 44, 20, 52, 28, 60],
                        [3, 35, 11, 43, 19, 51, 27, 59],
                        [2, 34, 10, 42, 18, 50, 26, 58],
                        [1, 33, 9,  41, 17, 49, 25, 57]]

rev_final_permutation= [[57, 49, 41, 33, 25, 17, 9, 1],
                       [59, 51, 43, 35, 27, 19, 11, 3],
                       [61, 53, 45, 37, 29, 21, 13, 5],
                       [63, 55, 47, 39, 31, 23, 15, 7],
                       [58, 50, 42, 34, 26, 18, 10, 2],
                       [60, 52, 44, 36, 28, 20, 12, 4],
                       [62, 54, 46, 38, 30, 22, 14, 6],
                       [64, 56, 48, 40, 32, 24, 16, 8]]

rev_initial_permutation = [[40,8,48,16,56,24,64,32],
                    [39,7,47,15,55,23,63,31],
                    [38,6,46,14,54,22,62,30],
                    [37,5,45,13,53,21,61,29],
                    [36,4,44,12,52,20,60,28],
                    [35,3,43,11,51,19,59,27],
                    [34,2,42,10,50,18,58,26],
                    [33,1,41,9,49,17,57,25]]

inv_sbox_per = [ 9,17,23,31,
                    13,28,2,18,
                    24,16,30,6,
                    26,20,10,1,
                    8,14,25,3,
                    4,29,11,19,
                    32,12,22,7,
                    5,27,15,21]

S={
            1:[ [14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],
                [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13 ]],
    
            2:[ [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9]],
    
            3:[[ 10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],
               [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
               [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],
               [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
            4:[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
               [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
               [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],
               [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    
            5:[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
               [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
               [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
               [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    
            6:[[12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],
               [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
               [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
               [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    
            7:[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
               [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
               [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
               [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
            8:[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7],
               [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
               [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
               [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
         }

expansion = [   32,1,2,3,4,5,
                4,5,6,7,8,9,
                8,9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32,1]

permutation = [ 16,7,20,21,
                29,12,28,17,
                1,15,23,26,
                5,18,31,10,
                2,8,24,14,
                32,27,3,9,
                19,13,30,6,
                22,11,4,25]

PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,
                        63,55,47,39,31,23, 15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,
                         52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

def hex_to_bin(input_str):
    input_str = input_str.replace(" ","")
    result = ""
    for c in input_str:
        if c.isalpha():
            c = ord(c.lower())-87
        result += "{:0>4b}".format(int(c))
    return result

def bin_to_str(input_str):
    result = ""
    for i in range(0,len(input_str),4):
        result += chr( ord('f') + int(input_str[i:i+4],2) )
    return result

def apply_permutation(input_str):
    input_str = input_str.replace(" ", "")
    result = ""
    for i,c in enumerate(input_str):
        result += input_str[permutation[i] - 1]
    return result

def apply_permut(input_str, which_permut):
    input_str = input_str.replace(" ","")
    if len(input_str)==16:
        input_str = hex_to_bin(input_str)
    result = ""
    for i,c in enumerate(input_str):
        result += input_str[which_permut[i//8][i%8]-1]
    return result

def apply_expansion(input_str):
    input_str = input_str.replace(" ","")
    result = ""
    if len(input_str) == 8:
        input_str = hex_to_bin(input_str)
        
    if len(input_str) == 32:
        for i in range(48):
            result += input_str[expansion[i]-1]
    return result

def str_to_bin(input_str):
    result = ""
    for i in input_str:
        result += "{:0>4b}".format(ord(i) - 102) 
    return result

def apply_inv_sbox_per(input_str):
    result = ""
    for i,c in enumerate(input_str):
        result += input_str[inv_sbox_per[i] - 1]
    return result

def bitwise_xor(a,b, length):
    result =""
    for i in range(length):
        result += str( int(a[i]) ^ int(b[i]))
    return result

def apply_sbox(input_str, box_no):
    result=""
    row = int(input_str[0]+input_str[5],2)
    col = int(input_str[1:5],2)
    result +=  "{0:0>4b}".format(S[box_no][row][col])
    return result

def find_k6_of_sboxes(input_sbox_xor, inv_perm, expansion_out, sboxes):
    keys = np.zeros((8,64),dtype=int)
    for i in range(len(inv_perm)):  
        for box in range(0,8):
            t_s_in_xor = input_sbox_xor[i][box*6:box*6+6]
            t_s_out_xor = inv_perm[i][box*4:box*4+4]
            t_ex_out1 = expansion_out[2*i][box*6:box*6+6]

            for a in range(0,64):
                a1 = "{:0>6b}".format(a)                                   
                a2 = bitwise_xor(a1,t_s_in_xor,6)
                s_a1_xor_a2 = bitwise_xor( apply_sbox(a1,box+1), apply_sbox(a2,box+1),4)

                if s_a1_xor_a2 == t_s_out_xor:
                    key = bitwise_xor(t_ex_out1,a1,6)
                    keys[box][int(key,2)]+=1
                     
    k6_sbox = dict()
    freq= dict()
    for i in sboxes:
        k6_sbox["Sbox-"+str(i)] =  "{:0>6b}".format(np.where(keys[i-1] == keys[i-1].max())[0][0])
        freq["Sbox-"+str(i)] = keys[i-1].max()
    return (k6_sbox,freq)

def left_shift_key(input_list, num_shifts):
    if type(input_list) == list:
        while(num_shifts > 0):
            input_list.append(input_list.pop(0))
            num_shifts -=1
        return input_list

def key_scheduling(rounds):
    k=PC1.copy()
    round_keys = dict()
    for r in range(1,rounds+1):
        left = k[0:28]
        right = k[28:]
        left = left_shift_key(left, shifts[r-1])
        right = left_shift_key(right, shifts[r-1])
        k = left + right
        t=['#']*48
        for j in range(0,48):
            t[j] = k[PC2[j]-1]
        round_keys[r]=t
    return round_keys

def encrypt(n,key56,rounds):
    n = apply_permut(n, initial_permutation)
    k=[x for x in key56]
    for r in range(1,rounds+1):
        R = n[32:]
        L = n[:32]
        
        R1 = apply_expansion(R)
        
        left = k[0:28]
        right = k[28:]
        left = left_shift_key(left, shifts[r-1])
        right = left_shift_key(right, shifts[r-1])
        k = left + right
        t=""
        for j in range(0,48):
            t += k[PC2[j]-1]
        key48 = "".join(t)
        
        s_in = bitwise_xor(R1,key48,48)
        s_out = ""
        for i in range(0,48,6):
            s_out += apply_sbox(s_in[i:i+6],i//6+1)
        
        p_out = apply_permutation(s_out)
        n = R + bitwise_xor(p_out,L,32) 
        
    n= apply_permut(n, final_permutation)
    return n

def decryption(p,round_keys,rounds):
    p = apply_permut(p, rev_final_permutation)
    R = {6:p[32:]}
    L = {6:p[:32]}
    for r in range(rounds,0,-1):
        R[r-1] =L[r]  
        expansion_out = apply_expansion(R[r-1])
        s_in = bitwise_xor(round_keys[r],expansion_out,48)
        s_out = ""
        for box in range(8):
            s_out += apply_sbox(s_in[box*6:box*6+6], box+1)
        p_out = apply_permutation(s_out)
        L[r-1] = bitwise_xor(p_out,R[r],32)
    return apply_permut(L[0]+R[0], rev_initial_permutation)

def generate_round_keys(key56):
    round_keys={}
    k = [x for x in key56]
    for r in range(1,6+1):        
        left = k[0:28]
        right = k[28:]
        left = left_shift_key(left, shifts[r-1])
        right = left_shift_key(right, shifts[r-1])
        k = left + right
        t=""
        for j in range(0,48):
            t += k[PC2[j]-1]
        
        round_keys[r]="".join(t)
    return round_keys

def brute_force(partial_key56,plaintext,ciphertext ):
    unk_bits =[]
    for i,c in enumerate(partial_key56):
        if c == '#':
            unk_bits.append(i)
        
    final_key = ""
    l = len(unk_bits)
    for i in range(2**l):
        b = "{:0>14b}".format(i)
        temp_k = partial_key56.copy()
        for j in range(l):
            temp_k[unk_bits[j]] = b[j]
        temp_k = "".join(temp_k)
        inp = str_to_bin(plaintext)

        if bin_to_str(encrypt(inp, temp_k,6 )) == ciphertext:
            final_key =temp_k
            return final_key
    return False 

filein1 = open("sbox_in_xor1.txt","r")
filein2 = open("sbox_in_xor2.txt","r")

input_sbox_xor1 = []
out = filein1.readlines()
for x in out:
    input_sbox_xor1.append(x[:-1])

input_sbox_xor2 = []
out = filein2.readlines()
for x in out:
    input_sbox_xor2.append(x[:-1])



filein1 = open("fiout1.txt","r")
filein2 = open("fiout2.txt","r")

fout1 = []
out = filein1.readlines()
for x in out:
    fout1.append(x[:-1])

fout2 = []
out = filein2.readlines()
for x in out:
    fout2.append(x[:-1])

inv_per1 = [apply_inv_sbox_per(x) for x in fout1] 
inv_per2 = [apply_inv_sbox_per(x) for x in fout2]


filein1 = open("expansion1.txt","r")
filein2 = open("expansion2.txt","r")

expanded1 = []
out = filein1.readlines()
for x in out:
    expanded1.append(x[:-1])

expanded2 = []
out = filein2.readlines()
for x in out:
    expanded2.append(x[:-1])



filein1 = open("plaintext1.txt","r")
filein2 = open("plaintext2.txt","r")

input_list1 = []
out = filein1.readlines()
for x in out:
    input_list1.append(x[:-1])

input_list2 = []
out = filein2.readlines()
for x in out:
    input_list2.append(x[:-1])

filein1 = open("ciphertext1.txt","r")
filein2 = open("ciphertext2.txt","r")

output_list1 = []
out = filein1.readlines()
for x in out:
    output_list1.append(x[:-1])

output_list2 = []
out = filein2.readlines()
for x in out:
    output_list2.append(x[:-1])

k6 , freq_k6 = find_k6_of_sboxes(input_sbox_xor1, inv_per1, expanded1, sboxes= [2,5,6,7,8])
k6_1, freq_k6_1 = find_k6_of_sboxes(input_sbox_xor2, inv_per2, expanded2, sboxes= [1,2,4,5,6])

if k6["Sbox-2"] != k6_1["Sbox-2"] or k6["Sbox-5"] != k6_1["Sbox-5"] or k6["Sbox-6"] != k6_1["Sbox-6"]:
    print("Number of input pairs didn't yield a key!, increasing it in trail.cpp file")
else:
    partial_key_sixth = [k6_1["Sbox-1"], k6_1["Sbox-2"],"######", k6_1["Sbox-4"],k6_1["Sbox-5"],k6_1["Sbox-6"],k6["Sbox-7"],k6["Sbox-8"]]
    partial_key_sixth = "".join(partial_key_sixth)
    
    partial_key56 = ["#"] * 56
    partial_key64 = ["#"] * 64
    round_keys = key_scheduling(rounds=6)
    for i,b in enumerate(round_keys[6]):
        partial_key64[b-1] = partial_key_sixth[i]
    for i in range(56):
        partial_key56[i] = partial_key64[PC1[i]-1]

    final_key = brute_force(partial_key56, input_list1[0], output_list1[0])
    if final_key==False:
        print("Can't find the final key! Increment the number of input pairs in trail.cpp")
    
    print("\nFinal 56-bit key : ",final_key)
    final_round_keys = generate_round_keys(final_key) 
    encrypted_password = "kgrrhjhlnuqiqtjiumjnmiupjjpljhqf"
    d= decryption(str_to_bin(encrypted_password[:16]),final_round_keys,6) + decryption(str_to_bin(encrypted_password[16:]),final_round_keys,6)
    print("\n\nPassword in binary : ", d)
    print("\n\nhehe: ",bin_to_str(d))
    ans=""
    for i in range(0,len(d),8):
        s =d[i:i+8]
        ans += chr(int(s,2))
    print("\nDecrypted password: ",ans)