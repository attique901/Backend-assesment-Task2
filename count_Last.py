count=0
fo = open("/home/attique/Desktop/names.txt","r")
content = fo.read()
print (content)
count=content.count(" Siddique")
print('-----')
print (count)