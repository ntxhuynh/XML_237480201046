import xml.dom.minidom

doc = xml.dom.minidom.parse("hoso.xml")
ds_the = []
for e in doc.getElementsByTagName("*"):
    if e.tagName not in ds_the:
        ds_the.append(e.tagName)

for ten in ds_the:
    print(ten)
