from PIL import Image

def Image_Encrypt(Img_Path,key):

    img = Image.open(Img_Path)
    img = img.convert("RGB")
    pixels = img.load()
    width , height = img.size

    for i in range(width):
        for j in range(height):
            red, green , blue = pixels[i, j]

            red  = (red + key) % 256
            green = (green + key) % 256
            blue = (blue + key) % 256

            pixels[i, j] = (red, green, blue)
    
    Encrypted_Img = "encrypted_img.png"
    img.save(Encrypted_Img)
    print("Encrypted image saved as ",Encrypted_Img)

def Image_Decrypt(Img_Path, key):

    img = Image.open(Img_Path)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            red, green, blue = pixels[i,j]

            red = (red - key) % 256
            green = (green - key) % 256
            blue = (blue - key) % 256

            pixels[i, j] = (red, green, blue)
    
    Decrypted_Img = "decrypted_img.png"
    img.save(Decrypted_Img)
    print("Decryption image saved as ",Decrypted_Img)


print("---- WELCOME..! IMAGE ENCYRPTION TOOL ----")
Img_Path = input("Enter Image path : ")
key = int(input("Enter Encryption(Secret) key : "))
Image_Encrypt(Img_Path, key)
Image_Decrypt("encrypted_img.png", key)

