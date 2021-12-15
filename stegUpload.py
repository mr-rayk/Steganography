#Referensi:
#https://pythonrepo.com/repo/Damgaard-PyImgur-python-third-party-apis-wrappers
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
#https://www.youtube.com/watch?v=lvky-tmoTvg
#https://www.geeksforgeeks.org/image-based-steganography-using-python/

import pyimgur
import base64
import requests
import json
from stegano import lsb

#Melakukan Encode Message ke dalam Base 64
msg = input("Message to encode with UTF-8: ")
msg_utf8 = msg.encode("utf-8")
msg_b64encoded = base64.b64encode(msg_utf8)

print(f"Encoded string to Base64: " + msg_b64encoded.decode("utf-8"))

msg_b64decoded = msg_b64encoded.decode("utf-8")

#memasukan message kedalam file PNG.
image = lsb.hide("banana.png", msg_b64decoded) #image source
image.save("bananaSTEG.png") #image yang sudah di inject dengan message dunamakan bananaSTEG.png
image_decode = lsb.reveal("bananaSTEG.png")
print(image_decode) 
print("\nMessage succesfully injected")

#deklarasi API Key Imgur dan file PNG yang sudah diinject dengan message
CLIENT_ID = "APIKEY"
PATH = "bananaSTEG.png"

#upload file PNG ke Imgur
imageUpload = pyimgur.Imgur(CLIENT_ID)
uploaded_image = imageUpload.upload_image(PATH, title="Stegano")

#print link imgur dari file PNG
print(uploaded_image.link)
