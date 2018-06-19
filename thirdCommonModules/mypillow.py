from PIL import Image
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('../data/test.jpg')
# 获得图像尺寸:
w, h = im.size

print('Original image size: %sx%s' % (w, h))
im.thumbnail(w/2,h/2)
print('Resize image to: %sx%s' % (w/2, h/2))
im.save('../data/thumbnail.jpg', 'jpeg')