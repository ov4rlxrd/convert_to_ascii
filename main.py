from PIL import Image # pip install pillow
import numpy as np

# path to file with pic
image_path = "ippyheader1.png"

img = Image.open(image_path).convert("L")  # convert("L") converting pic to gray

# change size of pic, for better perception
width, height = img.size
aspect_ratio = height / width
new_width = 300 # u can replace this num with num u want, for big pics bigger num
new_height = int(new_width * aspect_ratio * 0.5)
img = img.resize((new_width, new_height))

# ASCII symbols for use, u can use what u want for example '@%#..' and etc
ascii_chars = "█▓▒░=-:. "

# convert pixels to ascii
pixels = np.array(img)
ascii_image = "\n".join("".join(ascii_chars[pixel // 32] for pixel in row) for row in pixels)


print(ascii_image)

