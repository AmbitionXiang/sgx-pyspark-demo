import sys, os, pyaes, binascii

#Encrypt input data
def encrypt_file(i_file_name, o_file_name):
    f = open(i_file_name, 'rb')
    f1 = open(o_file_name, 'wb')
    key = "Scontain-Germany"
    aes = pyaes.AESModeOfOperationCTR(key)
    for mess in f.read().split('\n'):
        e_mess = aes.encrypt(mess)
        l = list(ord(c) for c in e_mess)
        e_mess = b''.join(chr(b) for b in l)
        hexlified = binascii.hexlify(e_mess)
        f1.write(hexlified)
        f1.write('\n')

    f1.close()

if __name__ == "__main__":
    # wordcount
    # encrypt_file('sensitive-input.txt', 'encrypted-sensitive-input.txt')

    # logistic regression
    encrypt_file('lr_opaque_1062.txt', 'enc-lr_opaque_1062.txt')

    # matrix multiplication
    # encrypt_file('mm_opaque_a_100.txt', 'enc-mm_opaque_a_100.txt')
    # encrypt_file('mm_opaque_b_100.txt', 'enc-mm_opaque_b_100.txt')

    # pearson correlation
    # encrypt_file('pe_opaque_a_105.txt', 'enc-pe_opaque_a_105.txt')
    # encrypt_file('pe_opaque_b_105.txt', 'enc-pe_opaque_b_105.txt')

    # kmeans
    # encrypt_file('km_opaque_50000_5.txt', 'enc-km_opaque_50000_5.txt')
    
    # dijkstra
    # encrypt_file('dij_opaque_1.txt', 'enc-dij_opaque_1.txt')

    # page rank
    # encrypt_file('pr_opaque.txt', 'enc-pr_opaque.txt')

    # transitive closure
    # encrypt_file('tc_opaque_2.txt', 'enc-tc_opaque_2.txt')

    # triangle counting
    # encrypt_file('tc_opaque_7.txt', 'enc-tc_opaque_7.txt')
