import re


class Verification_table:

    def __init__(self):
        pass

    def read_xml_table(self, xml_table):

        with open(xml_table, mode='r') as xtab:
            self.str_table = xtab.read()

        return self.str_table

    def read_all_tables(self, xml_tables):

        self.string_table_list = []

        for xml_table in xml_tables:
            string_table = self.read_xml_table(xml_table)
            self.string_table_list.append(string_table)

        return self.string_table_list
