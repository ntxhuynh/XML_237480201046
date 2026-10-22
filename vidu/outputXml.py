import xml.dom.minidom

doc = xml.dom.minidom.parse("Myxml.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)
