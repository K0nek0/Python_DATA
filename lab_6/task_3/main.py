import xml.etree.ElementTree as ET


def get_element():

    tree = ET.parse("ex_3.xml")
    root = tree.getroot()

    for item in root.findall("Документ/ТаблСчФакт/СведТов"):
        print(f"НАИМЕНОВАНИЕ ТОВАРА: {item.get("НаимТов")}; КОЛ-ВО ТОВАРА: {item.get("КолТов")}; ЦЕНА ТОВАРА: {item.get("ЦенаТов")}")


if __name__ == "__main__":
    get_element()
