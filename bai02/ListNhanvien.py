import xml.dom.minidom

doc = xml.dom.minidom.parse("hoso.xml")
for nv in doc.getElementsByTagName("nhanvien"):
    for tag in ("manv", "hoten", "donvi", "luong"):
        value = nv.getElementsByTagName(tag)[0].firstChild.data.strip()
        print("%s: %s" % (tag, value))
    print()
