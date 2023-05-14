from hashlib import sha256

key = input (" input .txt key: ")
insert = input (" input .txt to encrypt: ")
output = input (" name of output .txt encrypt: ")

#clue = sha256(key.encode('utf-8').digest()) #hashage poss

with open(insert, 'rb') as insertt:
    
    with open(output, 'wb') as outputt:
        i = 0
        while insertt.peek():
            
            char = ord(insertt.read(1))
            modulo = i % len(key)
            b = bytes([char^ord(key[modulo])])
            outputt.write(b)
            i += 1