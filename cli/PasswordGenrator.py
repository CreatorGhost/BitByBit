
def cipher_encode(string,n):
    new=""
    for char in string:
        ascii=ord(char)
        new=new+chr(ascii+n)
    return new


def cipher_decode(string,n):
    new=""
    for char in string:
        ascii=ord(char)
        new=new+chr(ascii-n)
    return new




encoded=cipher_encode(a,n)
decoded=cipher_decode(encoded,n)

print(encoded)
print(decoded)
