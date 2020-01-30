text = """
{
    "parent": "item/generated",
    "textures": {
        "layer0": "%s:item/%s"
    }
}
""" % ( input("What is your modid? "), input("What is the resourcelocation of your item? ") )

with open( input("What file? "), "w" ) as f:
	f.write(text)
