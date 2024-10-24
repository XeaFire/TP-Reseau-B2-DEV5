import socket
import re
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('5.5.5.11', 13337))
s.send('Hello'.encode())
# On reçoit la string Hello
data = s.recv(1024)
valid = True

# Récupération d'une string utilisateur
while valid:
    msg = input("Calcul à envoyer: ")
    pattern = r'^\s*[\d.]+(?:\s*[\+\-\*\/]\s*[\d.]+)?\s*$'
    if re.match(pattern, msg):
        
        numbers = [int(word) for word in re.split(r'\D+', msg) if word]
        for numb in numbers:
            if numb > -1048575 or msg < 1048575:
                valid = False
            break
        else:
            print("Le nombre ou les nombres n'est / ne sont pas valide(s)")
    else:
        print("Votre input n'est pas valide")
        

encoded_msg = msg.encode('utf-8')
msglen = len(encoded_msg)
header = msglen.to_bytes(4, byteorder='big')
footer = "<clafin>"
payload = header + encoded_msg + footer.encode('utf-8')
    


# On envoie
s.send(payload)
print(payload)
# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
