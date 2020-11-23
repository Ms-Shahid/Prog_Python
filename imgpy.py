from PIL import Image

img = Image.open('/home/ms/Pictures/Wallpapers/ubuntu.jpg')

contobw = img.convert("L")
contobw.save('new_img.jpg')
contobw.show()