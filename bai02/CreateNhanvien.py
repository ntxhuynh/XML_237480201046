from xml.dom import minidom

ds = [
    ("001", "Nguyễn Thế Anh", "Hành chính", "5.000.000"),
    ("002", "Nguyễn Thanh Bình", "Kỹ thuật", "7.000.000"),
    ("003", "Vương Thúy Phượng", "Tổ chức", "8.000.000"),
]

doc = minidom.Document()
danhsach = doc.createElement("danhsach")
doc.appendChild(danhsach)

for manv, hoten, donvi, luong in ds:
    nv = doc.createElement("nhanvien")
    for tag, value in (("manv", manv), ("hoten", hoten),
                       ("donvi", donvi), ("luong", luong)):
        e = doc.createElement(tag)
        e.appendChild(doc.createTextNode(value))
        nv.appendChild(e)
    danhsach.appendChild(nv)

with open("hoso.xml", "w", encoding="utf-8") as f:
    f.write(doc.toprettyxml(indent="    "))
print("Tạo hoso.xml thành công")
