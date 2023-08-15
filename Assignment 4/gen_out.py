import subprocess
import sys

def generate_ciphertext_via_ssh(input_list):
    intxt = ['hardwired', 'hardwired', '4','read', 'password ', 'c']
    
    for s in input_list:
        intxt.extend([s,'c'])
    intxt.extend(['back','exit'])
    file = open("input_ssh.txt","w")
    for i in intxt:
        file.write(i)
        file.write("\n")
    file.close()
    
    process = subprocess.Popen('./extract.sh')
    process.wait()
    search_line = 'Slowly, a new text starts appearing on the screen. It reads ...\n'
    file = open("extracted.txt", "r")
    out = file.readlines()

    x=out.index(search_line)
    out = out[x:]
    output_list = [] 
    for i,s in enumerate(out):
        if s==search_line:
            output_list.append(out[i+1][2:-1])
    return output_list



if sys.argv[1] == "1":
    file_in = open("plaintext1.txt","r")
    file_out = open("ciphertext1.txt","w")
elif sys.argv[1] == "2":
    file_in = open("plaintext2.txt","r")
    file_out = open("ciphertext2.txt","w")

inpu = []

out = file_in.readlines()
for x in out:
    inpu.append(x[:-1])

out_list = generate_ciphertext_via_ssh(inpu)
password = out_list.pop(0)
for i in out_list:
    file_out.write(i)
    file_out.write("\n")
file_out.close()