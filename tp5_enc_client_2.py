import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('5.5.5.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

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
    


# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
