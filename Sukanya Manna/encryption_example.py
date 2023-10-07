import encrypt

encryptor=encrypt.Encryptor()

mykey=encryptor.key_create()

encryptor.key_write(mykey, 'mykey.key')

loaded_key=encryptor.key_load('mykey.key')

encryptor.file_encrypt(loaded_key, 'file.txt', 'enc_file.txt')

encryptor.file_decrypt(loaded_key, 'enc_file.txt', 'file.txt')