import base64
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding

def MyDecrypt(ciphertext, key, IV):
    #Set the AES mode to Cipher Block Chaining (CBC).
    mode = AES.MODE_CBC
    #Create a new AES instance.
    decryptor = AES.new(key, mode, IV=IV)
    #Decrypt image (still a string).
    plaintext = decryptor.decrypt(ciphertext)
    
    return plaintext

def MyFileDecrypt(imageName, key, IV):
    #Open the image for reading in binary mode 'rb'.
    file = open(imageName, 'rb') 
    #Store contents in a variable.
    ciphertext = file.read()
    #Pass in ciphertext, key and IV and decrypted to padded plaintext.
    paddedPlaintext = MyDecrypt(ciphertext, key, IV)
    #Create a padder instance.
    unpadder = padding.PKCS7(256).unpadder()
    #Unpad the plaintext.
    unpaddedData = unpadder.update(paddedPlaintext)
    #Create a file to store decrypted message.
    image = open("decrypted.png", "wb")
    #Decode plaintext from a string to a image and write to file.
    image.write(base64.b64decode(unpaddedData))
    #Close the file.
    image.close()
    
    