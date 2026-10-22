from xml.dom import minidom

root = minidom.Document()

data = root.createElement('data')
root.appendChild(data)

item1 = root.createElement('item')
item1.setAttribute('name', 'item1')
item1.appendChild(root.createTextNode('item1abc'))
data.appendChild(item1)

item2 = root.createElement('item')
item2.setAttribute('name', 'item2')
item2.appendChild(root.createTextNode('item2abc'))
data.appendChild(item2)

with open("data.xml", "w", encoding="utf-8") as f:
    f.write(root.toprettyxml(indent="    "))
print("Tạo file thành công")
