from cryptography.fernet import Fernet

key=input('Enter key').encode('utf-8')

msg=input('Enter message').encode('utf-8')

f=Fernet(key)

print(f.decrypt(msg).decode('utf-8'))

'''
BmUp_Odc_5Z6vjwXPI1GaVgIWXUht7MniUMHKLuchvI=
gAAAAABfCeETUMef27f_nKDgAeQ7cCc60ypa1KOylEjBUecAOvhl2dEvKH2wuEh0-B2cbvQ61hN8w3Jdch5dz4fEdR2OkP9JGUr7MblBUNEcGnBiY2Ut5ts=
'''