#mở rộng
import xml.etree.ElementTree as ET

tree = ET.parse("hoso.xml")
for nv in tree.getroot().findall("nhanvien"):
    if nv.find("manv").text.strip() == "001":
        nv.find("luong").text = "6.000.000"

tree.write("hoso.xml", encoding="utf-8", xml_declaration=True)
print("Sửa thành công")