from Crypto.Cipher import DES3
from hashlib import md5
while True:
    print('Zgjidh njërin nga operacionet e mëposhtme:\n\t1- Enkriptim\n\t2- Dekriptim')
    operation = input('Zgjedhja juaj: ')
    if operation not in ['1','2']:
        break
    file_path = input('File path: ')
    key = input ('TDes key: ')

    key_hash = md5(key.encode('ascii')).digest()

    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_CBC, nonce=b'0')

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()

        if operation == '1':
            #Enkripto
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            #Dekripto
            new_file_bytes = cipher.decrypt(file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
