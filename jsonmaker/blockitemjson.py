#!/Users/jayjay/anaconda3/bin/python
text = """
{
    "parent": "%s:block/%s"
}
""" % ( input("What is your modid? "), input("What is the resourcelocation of your block? ") )
with open( input("What file? "), "w" ) as f:
	f.write(text)
