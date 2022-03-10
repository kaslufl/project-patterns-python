import xml.etree.ElementTree as et

from .serializer import Serializer


class XmlSerializer(Serializer):
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):

        self._element = et.Element(object_name, attrib={'id': str(object_id)})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')
