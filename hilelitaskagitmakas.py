import random

def hileli_pc_secimuret(user_secim):
    if user_secim == 'tas':
        return 'makas'
    elif user_secim == 'kagit':
        return 'tas'
    else:
        return 'kagit'

skor_user = 0
skor_pc = 0

while True:
    user_secim =  input('tas,kagit,makas?: ')
    pc_secim = hileli_pc_secimuret(user_secim)
    print('Bilgisayar:',pc_secim)

    if pc_secim == user_secim:
        print('---Berabere---')
    elif pc_secim == 'tas' and user_secim == 'kagit':
        skor_user +=1
    elif pc_secim == 'kagit' and user_secim == 'makas':
        skor_user +=1
    elif pc_secim == 'makas' and user_secim == 'tas':
        skor_user +=1
    else:
        skor_pc +=1
    
    print('siz:', skor_user, 'VS bilgisayar:', skor_pc )

    if skor_user == 3 or skor_pc == 3:
        break

if skor_pc > skor_user:
    print('----KAYBETTINIZ----')
else:
    print('+++KAZANDINIZZ+++')