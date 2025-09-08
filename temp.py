from sys import argv

with open(argv[1], "rb") as f:
    data = f.read(int(argv[2]))
    bits = ''.join(f'{byte:08b}' for byte in data)
    print(bits)
