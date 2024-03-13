from PIL import Image



im = Image.open('Turt(16).png') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(im.getpixel((8,8)))
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png



'''with open('Turt.png', 'rb') as f:
    filebytes = f.read()
    print('[')
    print(filebytes)
    print(']')

    print('{')
    print(filebytes.decode('utf-8'))
    print('}')'''

'''with open(image, 'rb') as f: # open the file in read binary mode
    data = f.read() # read the bytes from the file to a variable

pos = data.find(bytes(8)) # locate the 8 null bytes
message = data[pos + 8:].decode('utf-8')  # decode the message'''