import encryption_level
import getpass

encryption_level.generateKeys()
privateKey, publicKey =encryption_level.loadKeys()
print("For encryption")
message = getpass.getpass()
ciphertext = encryption_level.encrypt(message, publicKey)

signature = encryption_level.sign(message, privateKey)

#text = encryption_level.decrypt(ciphertext, privateKey)
print("For verifying")
text = getpass.getpass()

if encryption_level.verify(text, signature, publicKey):
    print('Successfully verified password')
else:
    print('The password could not be verified')