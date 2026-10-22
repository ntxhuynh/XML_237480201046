#mở rộng
import xml.dom.minidom

doc = xml.dom.minidom.parse("hoso.xml")
for nv in doc.getElementsByTagName("nhanvien"):
    donvi = nv.getElementsByTagName("donvi")[0].firstChild.data.strip()
    if donvi == "Kỹ thuật":
        print(nv.getElementsByTagName("hoten")[0].firstChild.data.strip())