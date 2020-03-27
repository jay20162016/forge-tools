#!/Users/jayjay/anaconda3/bin/python
def blockStateJSON(modid, resourcelocation, file):
    text = """
        {
            "variants": {
                "": { "model": "%s:block/%s" }
            }
        }
        """ % (modid, resourcelocation)

    with open(file, "w") as f:
        f.write(text)


if __name__ == '__main__':
    blockStateJSON(input("What is your modid? "), input("What is the resourcelocation of your item? "),
                   input("What file? "))
