import re


class Verification_table:

    column_regex_dict = {
        'ID': r'(?<=<ID>).+(?=</ID>)',
        'DOE': r'(?<=<DOE>).+(?=</DOE>)',
        'inp1': r'(?<=<inp1>).+(?=</inp1>)',
        'inp2': r'(?<=<inp2>).+(?=</inp2>)',
        'out1': r'(?<=<out1>).+(?=</out1>)',
        'out2': r'(?<=<out2>).+(?=</out2>)'
    }

    def __init__(self):
        self.column_names = ['ID', 'DOE', 'inp1', 'inp2', 'out1', 'out2']
        self.generated_regex = {
            'ID': [],
            'DOE': [],
            'inp1': [],
            'inp2': [],
            'out1': [],
            'out2': []
        }

    def read_xml_table(self, xml_table):

        with open(xml_table, mode='r') as xtab:
            str_table = xtab.read()

        return str_table

    def read_all_tables(self, xml_tables):

        string_table_list = []

        for xml_table in xml_tables:
            string_table = self.read_xml_table(xml_table)
            string_table_list.append(string_table)

        return string_table_list

    def generate_regex_table(self, xml_tables):

        self.regex_string_table = ('<?xml version="1.0" encoding="UTF-8" ?>\n'
                                   '<root>')
        string_table_list = self.read_all_tables(xml_tables)

        for col_tag in self.column_names:
            get_tag_generators = []

            for index in range(len(xml_tables)):
                tag_generator = Verification_table.return_matches(
                    col_tag, string_table_list[index])
                get_tag_generators.append(tag_generator)

            for (e1, e2, e3) in zip(*get_tag_generators):
                self.generated_regex[col_tag].append(f'(?:{e1}|{e2}|{e3})')

        self.format_generated_xml()

        return self.regex_string_table

    @classmethod
    def return_matches(cls, tag_name, string_table):

        pattern = re.compile(cls.column_regex_dict[tag_name])
        matches = pattern.finditer(string_table)

        for match in matches:
            yield match.group()

    def format_generated_xml(self):
        for num in range(len(self.generated_regex[self.column_names[0]])):
            self.regex_string_table += '\n'
            self.regex_string_table += (
                f'<row-{num}>\n'
                f'<ID>{self.generated_regex["ID"][num]}'
                f'</ID>\n'
                f'<DOE>{self.generated_regex["DOE"][num]}'
                f'</DOE>\n'
                f'<inp1>{self.generated_regex["inp1"][num]}'
                f'</inp1>\n'
                f'<inp2>{self.generated_regex["inp2"][num]}'
                f'</inp2>\n'
                f'<out1>{self.generated_regex["out1"][num]}'
                f'</out1>\n'
                f'<out2>{self.generated_regex["out2"][num]}'
                f'</out2>\n'
                f'</row-{num}>'
            )
        self.regex_string_table += '\n</root>\n'
