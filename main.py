import re
import xml.etree.ElementTree as ET

def parse_xml(xml_filename):
  tree = ET.parse(xml_filename)
  root = tree.getroot()
  return {
    seg.attrib.get('id'): [
      _seg.strip()
      for _seg in re.sub('\s+|\-+', ' ', seg.text).strip().split('. ')
      if _seg != ''
    ]
    for seg in root.iter('seg')
  }

spanish = parse_xml('Spanish.xml')
quechua = parse_xml('Quichua-NT.xml')


success = open("qui_sp.txt", "w+")
error = open("error.txt", "w+")

for key in spanish.keys():
	if key in spanish and key in quechua:
		len_sp = len(spanish[key])
		len_qu = len(quechua[key])
		if len_sp != len_qu:
			error.write(f'{spanish[key]}\t{quechua[key]}\t\t{key}\n')
		else:
			for i in range(len_sp):
				success.write(f'{quechua[key][i]}\t{spanish[key][i]}\t\t{key}\n')

success.close() 
error.close() 
