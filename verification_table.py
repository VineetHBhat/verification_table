import re


class Verification_table:

    def __init__(self):
        pass

    def read_xml_table(self, xml_table):

        with open(xml_table, mode='r') as xtab:
            self.str_table = xtab.read()

        return self.str_table
