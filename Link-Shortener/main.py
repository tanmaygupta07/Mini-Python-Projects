import pyshorteners

link = input("\nEnter the link: ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nShorted link is : " +x)