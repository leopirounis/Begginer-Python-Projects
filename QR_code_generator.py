import qrcode

text_URL = input("Enter the text or URL: ")
img = qrcode.make(text_URL)
type(img)
file_name = input("Enter the file name: ") #for right image set as: your_file_name.jpg
img.save(file_name)
print(f"QR code is saved as {file_name}")