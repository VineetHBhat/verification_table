import unittest
from verification_table import Verification_table


class Test_verification_table(unittest.TestCase):

    def setUp(self):

        self.tag_list = ['ID', 'DOE', 'inp1', 'inp2', 'out1', 'out2']

        self.extract_tag_value_regex = {
            'ID': r'(?<=<ID>).+(?=</ID>)',
            'DOE': r'(?<=<DOE>).+(?=</DOE>)',
            'inp1': r'(?<=<inp1>).+(?=</inp1>)',
            'inp2': r'(?<=<inp2>).+(?=</inp2>)',
            'out1': r'(?<=<out1>).+(?=</out1>)',
            'out2': r'(?<=<out2>).+(?=</out2>)'
        }

        self.xml_table_list = ['sample_vp_1.xml',
                               'sample_vp_2.xml',
                               'sample_vp_3.xml'
                               ]

        self.exp_string_list = [
            ('\ufeff<?xml version="1.0" encoding="UTF-8" ?>\n'
             '<root>\n'
             '<row-0>\n'
             '<ID>0</ID>\n'
             '<DOE>ULH</DOE>\n'
             '<inp1>1.2</inp1>\n'
             '<inp2>1.1</inp2>\n'
             '<out1>2.3</out1>\n'
             '<out2>1.32</out2>\n'
             '</row-0>\n<'),
            ('\ufeff<?xml version="1.0" encoding="UTF-8" ?>\n'
             '<root>\n'
             '<row-0>\n'
             '<ID>0</ID>\n'
             '<DOE>ULH</DOE>\n'
             '<inp1>1.2</inp1>\n'
             '<inp2>1.1</inp2>\n'
             '<out1>2.64</out1>\n'
             '<out2>0.792</out2>\n'
             '</row-0>'),
            ('\ufeff<?xml version="1.0" encoding="UTF-8" ?>\n'
             '<root>\n'
             '<row-0>\n'
             '<ID>0</ID>\n'
             '<DOE>ULH</DOE>\n'
             '<inp1>1.2</inp1>\n'
             '<inp2>1.1</inp2>\n'
             '<out1>2.86</out1>\n'
             '<out2>0.528</out2>\n'
             '</row-0>')
        ]

        self.generate_table = Verification_table(self.tag_list,
                                                 self.extract_tag_value_regex)

    def test_read_xml_table(self):

        self.act_string_table = self.generate_table.read_xml_table(
            self.xml_table_list[0])[:161]

        self.assertEqual(self.act_string_table, self.exp_string_list[0])

    def test_read_all_tables(self):

        self.act_string_list = self.generate_table.read_all_tables(
            self.xml_table_list)
        self.act_string_list = [new_str[:161] for new_str in
                                self.act_string_list]

        self.assertEqual(self.act_string_list, self.exp_string_list)

    def test_generate_regex_table(self):

        expected_regex_xml = 'expected_regex_table.xml'

        with open(expected_regex_xml, mode='r') as exp_res:
            self.expected_str = exp_res.read()

        self.actual_str = self.generate_table.generate_regex_table(
            self.xml_table_list)

        self.assertEqual(self.actual_str, self.expected_str)


if __name__ == '__main__':
    unittest.main()
