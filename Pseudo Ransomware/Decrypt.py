import json
import os
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

def MyFileDecrypt(filepath):
    #Split filename from extention.
    filename, ext = os.path.splitext(filepath)
    
    #Open the image for reading.
    file = open(filepath, 'r') 
    #Store contents in a variable.
    JsonDic = json.load(file)
    #Close file.
    file.close()
    
    #Contents where stored as strings so they now must be decoded to raw data
    #so that that they can be used.
    ciphertext = base64.b64decode(JsonDic['ciphertext'])
    key = base64.b64decode(JsonDic['key'])
    IV = base64.b64decode(JsonDic['IV'])
    ext = JsonDic['ext']
    
    #Pass in ciphertext, key and IV to be decrypted into raw padded plaintext data.
    paddedPlaintext = MyDecrypt(ciphertext, key, IV)
    #Create a padder instance.
    unpadder = padding.PKCS7(256).unpadder()
    #Unpad the plaintext.
    unpaddedData = unpadder.update(paddedPlaintext)
    
    #Create a file to store decrypted message.
    image = open(filename + ext, "wb")
    #Decode plaintext from a string to a image and write to file.
    image.write(unpaddedData)
    #Close the file.
    image.close()
    
    #Delete encrypted file.
    os.remove(filepath)
    
    
