"""
**Name:** Caesar
**Author:** Christoffer Thorske Johnsen
**Created:** 10.01.2019
"""
from itertools import cycle


Low_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

upper_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']

key = int()

print('Do you want to Encode or Decode with Caesar Cipher: ')
encode_decode = input('E to encode and D to decode: ')

while True:
    if encode_decode == 'E':
        key = int(input('Key to use: '))
        break

    if encode_decode == 'D':
        key_ne = input('Key to use: ')
        key = int('-' + key_ne)
        break


word = input('Word to encrypt or decrypt: ')
crypt_word = []



for j in word:
    if j.islower():
        finn_numb = Low_letter.index(j)
        loop = cycle(Low_letter)
        for i in range(finn_numb + key):
            next(loop)
        krypto_letter = (next(loop))
        crypt_word.append(krypto_letter)

    if j.isupper():
        finn_numb = upper_letter.index(j)
        loop = cycle(upper_letter)
        for i in range(finn_numb + key):
            next(loop)
        upper_krypto_letter = (next(loop))
        crypt_word.append(upper_krypto_letter)

    elif not j.islower() or j.isupper():
        print(j)
        crypt_word.append(j)
print(*crypt_word, sep='')


