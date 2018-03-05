import os
import base64
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding

def MyEncrypt(paddedImageString, key):
    #Generate a random Initialization Vector (IV).
    IV = os.urandom(16)
    #Set the AES mode to Cipher Block Chaining (CBC).
    mode = AES.MODE_CBC
    #Create a AES instance.
    encryptor = AES.new(key, mode, IV=IV)
    #Encrypt the message.
    ciphertext = encryptor.encrypt(paddedImageString)
        
    return ciphertext, IV, key
    
def MyFileEncrypt(imageName):
    #Generate a random key.
    key = os.urandom(32)
    #Open the image for reading in binary mode 'rb'.
    file = open(imageName, 'rb') 
    #Store contents in a variable using base64 to convert image to a string.
    imageString = base64.b64encode(file.read())
    #Create a padder instance
    padder = padding.PKCS7(256).padder()
    #Update padder with data you want to pad and store in a new variable.
    paddedImageString = padder.update(imageString)
    #Pad data.
    paddedImageString += padder.finalize()
    #Close file.
    file.close()
    
    
    #Encrypt using MyEncrypt method.
    ciphertext, IV, key = MyEncrypt(paddedImageString, key)
    
    #Create a file to store encrypted image.
    image = open("encrypted.jpg", "wb")
    #Write to file.
    image.write(ciphertext)
    #Close the file.
    image.close()
    
    #Needed to decrypt
    return key, IV
    