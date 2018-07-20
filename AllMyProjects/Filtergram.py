from Filters import *

filename = "Flamigos.jpg"
filename2 = "Flamigos_filtered.jpg"

original = load_img(filename)

newImg = Kaylie(original)
save_img(newImg, filename2)
show_img(newImg)
