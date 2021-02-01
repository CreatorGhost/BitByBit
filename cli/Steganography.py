# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
from PIL import Image
import stepic

choice = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))



if choice==1:
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
    data = input("Enter data to be encoded : ")
    data=bytes(data, 'utf-8') 
    new_img_name = input("Enter the name of new image(without extension) : ")+'.png'
    im1 = stepic.encode(image,data)
    im1.save(new_img_name, 'PNG')
    print('Encoded')

if choice==2:
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
    stegoImage = stepic.decode(image)
    print(stegoImage)