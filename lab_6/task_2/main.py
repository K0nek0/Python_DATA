import xml.etree.ElementTree as ET


def add_new_element():
    
    tree = ET.parse("ex_2.xml")
    root = tree.getroot()

    new_item = ET.Element("Item")
    ET.SubElement(new_item, "ArtName").text = "Сыр Гауда"
    ET.SubElement(new_item, "Barcode").text = "2000000000228"
    ET.SubElement(new_item, "QNT").text = "228,1"
    ET.SubElement(new_item, "QNTPack").text = "228,1"
    ET.SubElement(new_item, "Unit").text = "шт"
    ET.SubElement(new_item, "SN1").text = "00000008"
    ET.SubElement(new_item, "SN2").text = "02.11.2024"
    ET.SubElement(new_item, "QNTRows").text = "14"

    root.find("Detail").append(new_item)
    ET.indent(tree, '    ')

    summ, summ_rows = 0, 0

    for item in root.findall("Detail/Item"):
        val_1 = item.find("QNT").text.replace(",", ".")
        val_2 = item.find("QNTRows").text

        summ += float(val_1)
        summ_rows += int(val_2)

    root.find("Summary/Summ").text = str(summ).replace(".", ",")
    root.find("Summary/SummRows").text = str(summ_rows)

    tree.write("new_ex_2.xml", encoding="UTF-8", xml_declaration=True)


if __name__ == "__main__":
    add_new_element()
