#!/usr/bin/env python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)

        print(f"Dictionary serialized to {filename}.")
    except Exception as e:
        print(f"Error serializing dictionary to XML: {e}")


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}

        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except FileNotFoundError:
        print(f"Error deserializing XML from {filename}: File not found.")
        return None
    except ET.ParseError:
        print(f"Error deserializing XML from {filename}: Invalid XML.")
        return None
    except Exception as e:
        print(f"Error deserializing XML from {filename}: {e}")
        return None
