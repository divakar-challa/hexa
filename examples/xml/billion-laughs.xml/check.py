import xml.etree.ElementTree as ET

try:
    ET.parse("billion-laughs.xml")
    print("parsed")
except ET.ParseError as e:
    print("refused:", e)
