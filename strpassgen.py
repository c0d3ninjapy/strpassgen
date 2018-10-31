import random, string, hashlib, base64, time
from cryptography.fernet import Fernet

# The Fernet module implements an easy-to-use authentication scheme that uses a symmetric encryption algorithm.
# any message you encrypt with it cannot be manipulated or read without the key you define.
# You will need to install the cryptography package. (pip install cryptography)

# StrPassGen v1.0 by c0deNinja
# Python3

char = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase

lengthofpass = 16
length = int(lengthofpass)

password = ''

print ("Generating passwords, please give me 1 second..")
for i in range(1):
    print(str(1 - i) + " " + "Second remaining.........")
    time.sleep(1)
print("DONE!")

for x in range(length):
    password += random.choice(char)
print("Password: " + password)

password = password.encode()

hash_object = hashlib.sha1(password)
hex_dig = hash_object.hexdigest()
print("SHA1: " + hex_dig)

hash_object = hashlib.sha224(password)
hex_dig = hash_object.hexdigest()
print("SHA224: " + hex_dig)

hash_object = hashlib.sha256(password)
hex_dig = hash_object.hexdigest()
print("SHA256: " + hex_dig)

hash_object = hashlib.sha384(password)
hex_dig = hash_object.hexdigest()
print("SHA384: " + hex_dig)

hash_object = hashlib.sha512(password)
hex_dig = hash_object.hexdigest()
print("SHA512: " + hex_dig)

hash_object = hashlib.md5(password)
print("MD5: " + hash_object.hexdigest())

encode16 = base64.b16encode(password)
print ("Base16: " + str(encode16))

encode32 = base64.b32encode(password)
print ("Base32: " + str(encode32))

encode64 = base64.b64encode(password)
print ("Base64: " + str(encode64))

encodeb85 = base64.b85encode(password)
print ("Base85: " + str(encodeb85) + "\n")

ask = input("Do you want to encrypt your password with symmetric encryption algorithm? (Y/N): ")
if ask == "Y" or ask == "y":
    cipher_key = Fernet.generate_key()
    print ("Cipher Key: " + str(cipher_key))
    time.sleep(1)
    cipher = Fernet(cipher_key)
    encrypted_text = cipher.encrypt(password)
    print ("Encrypted Text: " + str(encrypted_text) + "\n")
elif ask == "N" or "n":
    print ("::::THANK YOU FOR USING StrPassGen V1.0 by c0deNinja!!::::")

# Decrypt your password: decrypted_text = cipher.decrypt(encrypted_text) print (decrypted_text)
