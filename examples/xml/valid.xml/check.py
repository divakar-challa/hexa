import xml.etree.ElementTree as ET

try:
    ET.parse("valid.xml")
    print("parsed")
except ET.ParseError as e:
    print("refused:", e)
