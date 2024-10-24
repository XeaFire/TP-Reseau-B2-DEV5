# msg = input("Calcul à envoyer: ")

# encoded_msg = bin(int(msg))

# print(encoded_msg[2:len(encoded_msg)])

def bytes_to_bits_binary(byte_data):
    bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
    bits_data = bits_data.zfill(len(byte_data) * 8)
    return bits_data



int_i = 1048575
shifted_i = 1048575 << 20
int_f = 1
shifted_i = shifted_i | int_f
super_int_one_byte = shifted_i.to_bytes(5, byteorder='big')

print(bytes_to_bits_binary(super_int_one_byte))
i_bin = bytes_to_bits_binary(super_int_one_byte[0:5])[0:20]
f_bin = bytes_to_bits_binary(super_int_one_byte[0:5])[20:40]
print(i_bin)
print(f_bin)
print(int(i_bin, 2))

