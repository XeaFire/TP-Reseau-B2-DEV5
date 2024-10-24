import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('5.5.5.11', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        conn.send("Hello".encode())

        # On reçoit le calcul du client
        header = conn.recv(4)
        if not header:
            break

        # On lit la valeur
        msg_len = int.from_bytes(header[0:4], byteorder='big')

        print(f"Lecture des {msg_len} prochains octets")

        # Une liste qui va contenir les données reçues
        chunks = []

        bytes_received = 0
        while bytes_received < msg_len:
            # Si on reçoit + que la taille annoncée, on lit 1024 par 1024 octets
            chunk = conn.recv(min(msg_len - bytes_received,1024))
            if not chunk:
                raise RuntimeError('Invalid chunk received bro')

            # on ajoute le morceau de 1024 ou moins à notre liste
            chunks.append(chunk)

            # on ajoute la quantité d'octets reçus au compteur
            bytes_received += len(chunk)

        # ptit one-liner pas combliqué à comprendre pour assembler la liste en un seul message
        message_received = b"".join(chunks).decode('utf-8')
        print(f"Received from client {message_received}")
        
        
        # Evaluation et envoi du résultat
        res  = eval(message_received)
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
