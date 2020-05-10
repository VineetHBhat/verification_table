import re


class Verification_table:
    '''
    This class provides methods for reading multiple tables in xml format and
    generating a single xml verification table with regular expression in
    cells. This verification table can be used to generate a baseline for table
    comparision in scenarios where cell values vary with changing versions.
    '''

    def __init__(self, tag_list, tag_value_regex):
        '''
        Initializes various instance variables used by other methods of the
        class.
        '''

        self.column_names = tag_list
        self.column_regex_dict = tag_value_regex
        self.generated_regex = {}

        for column in self.column_names:
            self.generated_regex[column] = []

    def read_xml_table(self, xml_table):
        '''
        Reads a single xml file and return the contents in the form of
        a string.
        '''

        with open(xml_table, mode='r') as xtab:
            str_table = xtab.read()

        return str_table

    def read_all_tables(self, xml_tables):
        '''
        Reads all passed xml files and returns the contents in the form of
        a list of string. Each element of the list represents the contents of
        one xml file. This uses read_xml_table() method of this class.
        '''

        string_table_list = []

        for xml_table in xml_tables:
            string_table = self.read_xml_table(xml_table)
            string_table_list.append(string_table)

        return string_table_list

    def return_matches(self, tag_name, string_table):
        '''
        This generator reads values of tag_name in string_table and yields
        the values one by one.
        '''

        pattern = re.compile(self.column_regex_dict[tag_name])
        matches = pattern.finditer(string_table)

        for match in matches:
            yield match.group()

    def format_generated_xml(self):
        '''
        Produces the final formatted string. The format defined here is hard
        coded. This needs to be modified as per the expected format of the
        output xml. This method does not return anything.
        '''

        self.regex_string_table = ('<?xml version="1.0" encoding="UTF-8" ?>\n'
                                   '<root>')
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

    def generate_regex_table(self, xml_tables):
        '''
        This methods uses read_all_tables(), return_matches() &
        format_generated_xml() methods to generate the desired xml string.
        This string is then returned.
        '''

        string_table_list = self.read_all_tables(xml_tables)

        for col_tag in self.column_names:
            get_tag_generators = []

            for index in range(len(xml_tables)):
                tag_generator = self.return_matches(col_tag,
                                                    string_table_list[index])
                get_tag_generators.append(tag_generator)

            for vals in zip(*get_tag_generators):
                try:
                    assemble_string = f'(?:{vals[0]}'
                except Exception as expn:
                    print(f'An exception has occured.\nDetails:\n{expn}')
                else:
                    for i in range(1, len(vals)):
                        assemble_string += f'|{vals[i]}'
                    assemble_string += ')'
                    self.generated_regex[col_tag].append(assemble_string)

        self.format_generated_xml()

        return self.regex_string_table

    def generate_output_xml(self, xml_tables, output_xml_filename):
        '''
        This methods generates the desired output in the form of a
        verification xml file.
        '''

        xml_content = self.generate_regex_table(xml_tables)

        with open(output_xml_filename, mode='w') as xfile:
            xfile.write(xml_content)
