from rembg import remove
from PIL import Image
img = Image.open("D:\\20201118_0015399.png")
R = remove(img)
R.save("20201118_001539911.png")