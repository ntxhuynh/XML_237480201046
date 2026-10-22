import xml.dom.minidom

def lay_text(node, tag):
    return node.getElementsByTagName(tag)[0].firstChild.data.strip()

doc = xml.dom.minidom.parse("danhsach.xml")
students = doc.getElementsByTagName("student")

stt = 1
for sv in students:
    name = lay_text(sv, "name")
    date = lay_text(sv, "date")
    city = lay_text(sv, "city")
    print("%d. %-15s %s %s" % (stt, name, date, city))
    stt += 1
