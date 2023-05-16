import hashlib 

def Crypt_Password(password):
    encode_password = password.encode()
    password_sha3 = hashlib.sha3_256(encode_password)
    return password_sha3.hexdigest()
