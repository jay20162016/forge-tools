#!/Users/jayjay/anaconda3/bin/python
from PIL import Image


def stdImage(rgba, img, file, preview=False):
    image = Image.open(img).convert("RGBA")
    content = image.load()
    imy, imx = image.size

    for x in range(imx):
        for y in range(imy):
            pixel = content[y, x]
            if pixel[0] == pixel[1] == pixel[2]:
                content[y, x] = (int(pixel[0] * rgba[0] / 255), int(pixel[1] * rgba[1] / 255),
                                 int(pixel[2] * rgba[2] / 255), int(pixel[3] * rgba[3] / 255))

    if preview:
        image.show()
        if input("Do you want to save? ").lower().startswith("y"):
            image.save(file)
    else:
        image.save(file)


if __name__ == '__main__':
    stdImage(eval(input("What is your desired RGBA? ")), input("What image do you want to use? "),
             input("What file to save to? "), preview=True)
