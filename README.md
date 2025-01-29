# convert_to_ascii
# Quick conversion of pictures to ASCII text images

## First of all, install Pillow
```
pip install pillow
```

## This block of code exists for resizing: 
```python
# change size of pic, for better perception
width, height = img.size
aspect_ratio = height / width
new_width = 300 # u can replace this num with num u want, for big pics bigger num
new_height = int(new_width * aspect_ratio * 0.5)
img = img.resize((new_width, new_height))
```

[My TG](https://t.me/ov4rlxrd)
[My X](https://x.com/DDenicah)

