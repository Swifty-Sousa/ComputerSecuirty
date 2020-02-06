import math 

letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def cesar(pt, k):
    k=k.upper()
    k_len = len(k)
    k_int = [ord(i) for i in k]
    pt_int= [ord(i) for i in pt]
    ct= ''
    for i in range(len(pt)):
        holder= (pt_int[i] + k_int[i % k_len])%26
        ct = ct + chr(holder + 65)
    return ct

def chi_sqr(letters):
    array=[]
    for i in alphabet:
        c_counts= letters.count(i)
        e_counts= letter_freqs[i]* len(letters)
        array.append(((c_counts-e_counts)**2)/e_counts)
    return(sum(array))
test="aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohilaaoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohilaaoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila"
test= test.upper()
cesar_vals=[]
for i in alphabet:
    holder=cesar(test, i)
    cesar_vals.append(chi_sqr(holder))

print(cesar_vals.index(min(cesar_vals)))

test= "aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila"
test= test.upper()
test2= "AAA"