#!/Users/jayjay/anaconda3/bin/python
def itemJSON(modid, resourcelocation, file):
    text = """
                {
                    "parent": "item/generated",
                    "textures": {
                        "layer0": "%s:item/%s"
                    }
                }
                """ % (modid, resourcelocation)

    with open(file, "w") as f:
        f.write(text)


if __name__ == '__main__':
    itemJSON(input("What is your modid? "), input("What is the resourcelocation of your item? "),
             input("What file? "))
