from PIL import Image

rgba = eval(input("Please input your desired RGBA in tuple format: "))
image = Image.open(input("Please input your desired image: ")).convert("RGBA")
content = image.load()
imy , imx = image.size

for x in range(imx):
	for y in range(imy):
		pixel = content[y, x]
		if pixel[0] == pixel[1] == pixel[2]:
			content[y, x] = (int(pixel[0] * rgba[0] / 255), int(pixel[1] * rgba[1] / 255), int(pixel[2] * rgba[2] /255), int(pixel[3] * rgba[3] / 255))

image.show()
if input("Do you want to save? ").lower().startswith("y"):
	image.save(input("What file do you want to save to? "))
