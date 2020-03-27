#!/Users/jayjay/anaconda3/bin/python
def blockJSON(modid, resourcelocation, file):
    text = """
    {
        "parent": "block/cube_all",
        "textures": {
            "all": "%s:block/%s"
        }
    }
    """ % (modid, resourcelocation)

    with open(file, "w") as f:
        f.write(text)


if __name__ == '__main__':
    blockJSON(input("What is your modid? "), input("What is the resourcelocation of your item? "),
              input("What file? "))
