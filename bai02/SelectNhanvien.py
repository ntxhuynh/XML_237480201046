import xml.dom.minidom

doc = xml.dom.minidom.parse("hoso.xml")
nhanvien = doc.getElementsByTagName("nhanvien")

print("Danh sách nhân viên:")
for nv in nhanvien:
    manv = nv.getElementsByTagName("manv")[0].firstChild.data.strip()
    hoten = nv.getElementsByTagName("hoten")[0].firstChild.data.strip()
    print(manv, "-", hoten)

print()
print("Nhân viên có manv = 002:")
for nv in nhanvien:
    if nv.getElementsByTagName("manv")[0].firstChild.data.strip() == "002":
        for tag in ("manv", "hoten", "donvi", "luong"):
            value = nv.getElementsByTagName(tag)[0].firstChild.data.strip()
            print("%s: %s" % (tag, value))
