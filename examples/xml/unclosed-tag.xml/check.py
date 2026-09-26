import xml.etree.ElementTree as ET

try:
    ET.parse("unclosed-tag.xml")
    print("parsed")
except ET.ParseError as e:
    print("refused:", e)
