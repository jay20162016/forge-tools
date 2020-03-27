#!/Users/jayjay/anaconda3/bin/python
from PIL import Image


def oreImage(rgba, file, preview=False):
    image = Image.open(
        "/Users/jayjay/programming/project/Minecraft/forge-tools/texturemaker/textures/blocks/diamond_ore.png").convert(
        "LA").convert("RGBA")
    content = image.load()

    li = [(1, 8), (2, 8), (3, 13), (4, 2), (4, 6), (4, 10), (4, 13), (5, 6), (6, 5), (6, 6), (7, 3), (7, 6), (7, 9),
          (8, 3), (8, 9), (8, 12), (9, 8), (9, 9), (9, 13), (10, 6), (10, 9), (10, 12), (10, 13), (11, 5), (11, 6),
          (11, 11), (11, 12), (12, 2), (12, 11), (12, 12), (13, 2), (13, 12), (10, 5), (5, 5), (3, 6), (8, 8), (9, 12)]

    for y, x in li:
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
    oreImage(eval(input("What is your desired RGBA? ")), input("What file to save to? "), preview=True)
