#!/usr/bin/python3

import sys
from collections import Counter
import statistics as stats
import math
key1= "yz"
key2= "xyz"
key3= "wxyz"
key4= "vwxyz"
key5= "AAAAA"
#taken from Wikipedia
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


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

#this function used for the test exersies in the assignment
#this fuction based of off thise encryptor https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4
def encrypt(pt, k):
    k=k.upper()
    k_len = len(k)
    k_int = [ord(i) for i in k]
    pt_int= [ord(i) for i in pt]
    ct= ''
    for i in range(len(pt)):
        holder= (pt_int[i] + k_int[i % k_len])%26
        ct = ct + chr(holder + 65)
    return ct


#this function used for the test exersies in the assignment
#this fuction based of off thise encryptor https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4
def decrypt(ct, k):
    k= k.upper()
    k_len = len(k)
    k_int = [ord(i) for i in k]
    ct_int= [ord(i)for i in ct]
    pt=''
    for i in range(len(ct_int)):
        holder= (ct_int[i]- k_int[i% k_len])% 26
        pt= pt + chr(holder+ 65)
    return pt

def encrypt_varance(pt, key):
    key=key.upper()
    cipher_text= encrypt(pt,key)
    ct_var= pop_var(cipher_text) 
    print("The variance with key ", key, "is", ct_var)
    print("")

def find_len(ct):
    variances=[]
    for i in range(2,14):
        variances.append(find_len_helper(ct,i)) 
    #print(*variances, sep='\n')
    for i in variances:
            if i>=0.001:
                #we add two because the list starts with a key lenth of two, therefore a key of length 6 will have index 4 in the list
                return (variances.index(i)+2)

def find_len_helper(ct, leng):
    holder=[]
    for i in range(0, leng-1):
        new_cipher=ct[i::leng]
        new_cipher_var=pop_var(new_cipher) 
        holder.append(new_cipher_var)
    return(stats.mean(holder))

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
        array.append((c_counts-e_counts)**2/e_counts)
    return(sum(array))
        
def solve(ct):
    key_len=find_len(ct)
    slices=[ct]
    plaintext=[]
    cesars=[]
    cesars_val=[]
    for i in range(0, key_len-1):
        slices.append(ct[i::key_len-1])
    for k in slices:
        for i in alphabet:
            holder=cesar(k, i)
            cesars_val.append(chi_sqr(holder))
        letter_holder= cesars_val.index(min(cesars_val))
        #print(letter_holder)
        plaintext.append(alphabet[letter_holder])
        cesars_val=[]
        hold=""
    print(hold.join(plaintext))

def solve_1(ct):
    keylen=find_len(ct)
    print("key length: ", keylen)
    #test= [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
    #firsts= test[::2]
    #print(firsts)
    #break into bits of length of key
    first= ct[::2]
    second= ct[1::2]
    cesars=[]
    for i in alphabet:
        cesars.append(cesar(first, i))
    #print(cesars, sep='\n')
    values=[]
    al=[]
    for k in cesars:
        values.append(chi_sqr(k))    
    key_letter= values.index(min(values))
    a= ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    test=[]
    for i in range(0, 25):
        test.append(a[i])
    print(test)
    print(*test, sep= '\n')
    #print(key_letter)
    #print(*values, sep='\n')
    #print("")
    #print(values[2])
    #print(alphabet[-2])


    







        


    


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    sample_plaintext= "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
    sample_plaintext= sample_plaintext.upper()
    #cipher= encrypt(sample_plaintext, key5)
    #key_len= find_len(cipher)
    #print(decrypt(cipher,"temblor"))
    #print("the key length is: ", key_len)
    #test= "aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila"
    #test= test.upper()
    #print(chi_sqr(test))
    #cipher=encrypt(sample_plaintext,key1)
    solve(cipher)

    #################################################################
    # first calculate the population variance in the given relitive frequenceies above
    erf= stats.variance(letter_freqs.values()) #English relitive frequncy 
    #print("The population variance of the relitive english words is: ", erf)
    #print("")

    #Sample plaintext:

    
    # population variance of the sample plaintext
    #sample_plaintext_variance= pop_var(sample_plaintext)
    #print("The population variance of the relative words in the sample plaintext is: ",sample_plaintext_variance)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #testing the encryptor and decryptor:
    #test_cipher= encrypt(sample_plaintext, "ABC")
    #print("The cipher is: ", test_cipher)
    #test_cipher= decrypt(test_cipher, "ABC")
    #print("The plaintext of the cipher is: ", test_cipher)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Part 3 
    #encrypt_varance(sample_plaintext, key1)
    #encrypt_varance(sample_plaintext, key2)
    #encrypt_varance(sample_plaintext, key3)
    #encrypt_varance(sample_plaintext, key4)
    #encrypt_varance(sample_plaintext, key5)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Part4
    #cipher_text= encrypt(sample_plaintext, key5)
    #cipher_text_even= cipher_text[0::2]
    #cipher_text_odd= cipher_text[1::2]
    #cipher_text_three= cipher_text[::3]
    #three_var=pop_var(cipher_text_three)
    #even_var= pop_var(cipher_text_even)
    #odd_var= pop_var(cipher_text_odd)
    #print("the even variance with key yz is: ", even_var)
    #print("the odd variance with key yz is: ", odd_var)
    #print("the mean of these two values is: ", stats.mean([even_var,odd_var]))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #part5 
    #cipher= encrypt(sample_plaintext, key5)
    #test= find_len2(cipher, 6)
    #print(test)
    #two=find_len(cipher,2)
    #three=find_len(cipher,3)
    #four=find_len(cipher,4)
    #five=find_len(cipher,5)
    #six= find_len(cipher,6)
    #seven= find_len(cipher,7)
    #eight= find_len(cipher,8)
    #nine= find_len(cipher,9)
    #ten= find_len(cipher,10)
    #eleven= find_len(cipher,11)
    #twelve= find_len(cipher,12)
    #print(stats.mean([two,three,four,five, six, seven, eight, nine, ten, eleven, twelve]))
    #test= [1,2,3,4,5,6,7,8,9,10,11,12,13]
    #print(test[0::3])
    #print(test[::3])
    #print(test[1::3])
    #print(test[2::3])
    #print('2 ', find_len2(cipher,2))
    #print('3 ', find_len2(cipher,3))
    #print('4 ', find_len2(cipher,4))
    #print('5 ', find_len2(cipher,5))
    #print('6 ', find_len2(cipher,6))
    #print('7 ', find_len2(cipher,7))
    #print('8 ', find_len2(cipher,8))
    #print('9 ', find_len2(cipher,9))
    #print('10', find_len2(cipher,10))
    #print('11', find_len2(cipher,11))
    #print('12', find_len2(cipher,12))
    #print('13', find_len2(cipher,13))
    #find_len2 became find_len_helper
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #apply the same concept but in a loop and find the variance that is closest to the true value.
    #print(find_len(cipher))

    

