from cryptography.fernet import Fernet

print('Create a key')
key=Fernet.generate_key()
print(key)

f=Fernet(key)

msg=input('Enter the messege to Encrypt')
en=f.encrypt(msg.encode('utf-8'))
print(en)