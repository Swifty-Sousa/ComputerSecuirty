#!/usr/bin/python3

import sys
from collections import Counter
import statistics as stats
key1= "yz"
key2= "xyz"
key3= "wxyz"
key4= "vwxyz"
key5= "uvwxyz"
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
    k_len = len(k)
    k_int = [ord(i) for i in k]
    ct_int= [ord(i)for i in ct]
    pt=''
    for i in range(len(ct_int)):
        holder= (ct_int[i]- k_int[i% k_len])% 26
        pt= pt + chr(holder+ 65)
    return pt

def encrypt_varance(pt, key):
    cipher_text= encrypt(pt,key)
    ct_var= pop_var(cipher_text) 
    print("The variance with key ", key, "is", ct_var)
    print("")


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case

    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    #################################################################
    # first calculate the population variance in the given relitive frequenceies above
    erf= stats.variance(letter_freqs.values()) #English relitive frequncy 
    print("The population variance of the relitive english words is: ", erf)
    print("")

    #Sample plaintext:
    sample_plaintext= "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
    sample_plaintext= sample_plaintext.upper()
    
    # population variance of the sample plaintext
    sample_plaintext_variance= pop_var(sample_plaintext)
    print("The population variance of the relative words in the sample plaintext is: ",sample_plaintext_variance)

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
    