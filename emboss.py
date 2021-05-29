
from PIL import Image
from PIL import ImageFilter

Image = Image.open("artificial.jpg")
edgeEnahnced = Image.filter(ImageFilter.EDGE_ENHANCE)
imageEdge = Image.filter(ImageFilter.CONTOUR())

Image.show() 
imageEdge.show()