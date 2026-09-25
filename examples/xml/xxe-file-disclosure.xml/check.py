import xml.etree.ElementTree as ET

try:
    ET.parse("xxe-file-disclosure.xml")
    print("parsed")
except ET.ParseError as e:
    print("refused:", e)
