#Denary to Binary Conversion Algorithm - www.101computing.net/denary-to-binary-conversion-algorithm

encoder = (128, 64, 32, 16, 8, 4, 2, 1)

def convertToBinary(denary):
    binary = ''
    for val in encoder:
        if denary >= val:
            binary = binary + '1'
            denary = denary - val
        else:
            binary = binary + '0'
    return binary

def convertToDenary(binary):
    denary = 0
    for i, bit in enumerate(binary):
        if bit == '1':
            denary += encoder[i]
    return denary

while True:
    try:
        den_num = int(input("Enter a number between 0 and 255:\n"))
    except ValueError:
        print("Invalid input. Try again.\n")
    else:
        if 0 <= den_num <= 255:
            break
        else:
            print("Input out of range. Try again.\n")

print(convertToBinary(den_num), '\n')

while True:
    try:
        bin_num = input("Enter a byte of any value (1 byte = 8 bits):\n")
    except ValueError:
        print("Invalid input. Try again.\n")
    else:
        if len(bin_num) == 8 and all(bit in ('0', '1') for bit in bin_num):
            break
        else:
            print("Byte must be 8 digits consisting of 0s or 1s. Try again.\n")

print(convertToDenary(bin_num))