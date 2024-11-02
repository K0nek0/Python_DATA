from xmlschema import XMLSchema


def validate_xml(xml_file, xsd_file):
    schema = XMLSchema(xsd_file)
    if schema.is_valid(xml_file):
        print(f"Файл {xml_file} прошел валидацию.")
    else:
        print(f"Файл {xml_file} не прошел валидацию.")


if __name__ == '__main__':
    xsd_file = "ex_1.xsd"
    invalid_xml_file = "ex_1_invalid.xml"
    validate_xml(invalid_xml_file, xsd_file)
