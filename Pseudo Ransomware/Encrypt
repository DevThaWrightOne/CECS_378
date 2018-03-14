import os
import base64
import json
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding

KEY_SIZE = 32
IV_SIZE = 16
AES_BLOCK_SIZE = 256

def MyEncrypt(paddedFileData, key):
    #Generate a random Initialization Vector (IV).
    IV = os.urandom(IV_SIZE)
    #Set the AES mode to Cipher Block Chaining (CBC).
    mode = AES.MODE_CBC
    #Create a AES instance.
    encryptor = AES.new(key, mode, IV=IV)
    #Encrypt the message.
    ciphertext = encryptor.encrypt(paddedFileData)
        
    return ciphertext, IV, key
    
def MyFileEncrypt(filepath):
    #Extract filename and extention.
    filename, ext = os.path.splitext(filepath)
    #Generate a random key.
    key = os.urandom(KEY_SIZE)
    #Open the file for reading in binary mode 'rb'.
    file = open(filepath, 'rb') 
    #Store raw data contents in a variable.
    fileData = file.read()
    #Create a padder instance
    padder = padding.PKCS7(AES_BLOCK_SIZE).padder()
    #Update padder with data you want to pad and store in a new variable.
    paddedFileData = padder.update(fileData)
    #Pad data.
    paddedFileData += padder.finalize()
    #Close file.
    file.close()
    
    #Encrypt using MyEncrypt method.
    ciphertext, IV, key = MyEncrypt(paddedFileData, key)
    
    #JSON does not take in bytes so key, IV and ciphertext are encoded to str.
    key = base64.b64encode(key).decode('utf-8')
    IV = base64.b64encode(IV).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    
    #Store variables in a python dict.
    dic = {"key": key, "IV": IV, "ext": ext, "ciphertext": ciphertext}
    #Convert dict to JSON.
    JsonDic = json.dumps(dic)    
    #Create a file to store JSON data.
    image = open(filename + ".devluz", "w")
    #Write to file.
    image.write(JsonDic)
    #Close the file.
    image.close()
    
    #Delete oringal file
    os.remove(filepath)
