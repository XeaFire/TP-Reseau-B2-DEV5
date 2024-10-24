import socket
import utils

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
        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(6)
        data_bin = utils.bytes_to_bits_binary(data)

        operateur_bin = data_bin[0:1]

        if operateur_bin == 1:
            operateur = '+'
        elif operateur_bin == 2:
            operateur = '-'
        elif operateur_bin == 3:
            operateur = '*'
        elif operateur_bin == 4:
            operateur = '/'

        numb1_bin = data_bin[9:28]
        numb2_bin = data_bin[28:48]

        print(int(numb1_bin, 2))
        print(int(numb2_bin, 2))
        # Evaluation et envoi du résultat
        # res  = eval(data.decode())
        # conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
