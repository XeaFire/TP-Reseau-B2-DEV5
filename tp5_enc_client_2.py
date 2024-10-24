import socket
import re
import utils
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('5.5.5.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

valid = True

while valid:
    index = 1
    msg = input("Calcul à envoyer: ")
    pattern = r'^\s*[\d.]+(?:\s*[\+\-\*\/]\s*[\d.]+)?\s*$'
    if re.match(pattern, msg):
        
        numbers = [int(word) for word in re.split(r'\D+', msg) if word]
        valid = False
        for numb in numbers:
            if numb > -1048575 or msg < 1048575:
                continue
            else:
                valid =  True
                print("Le nombre ou les nombres n'est / ne sont pas valide(s)")
                break
            
    else:
        print("Votre input n'est pas valide")
    
# Encodage à la Tristan Diarhée là

numb1 = numbers[0]
numb2 = numbers[0]
shifted_i = numb1 << 20
numbs = shifted_i | numb2
numbs_bytes = numbs.to_bytes(5, byteorder='big')

print(utils.bytes_to_bits_binary(numbs_bytes))
# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
