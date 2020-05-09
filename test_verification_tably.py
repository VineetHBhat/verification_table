import unittest
from verification_table import Verification_table


class Test_verification_table(unittest.TestCase):

    def setUp(self):

        self.xml_table_list = ['sample_vp_1.xml',
                               'sample_vp_2.xml',
                               'sample_vp_3.xml'
                               ]

        self.generate_table = Verification_table()

    def test_read_xml_table(self):
        self.exp_string_table = ('\ufeff<?xml version="1.0" '
                                 'encoding="UTF-8" ?>\n'
                                 '<root>\n'
                                 '<row-0>\n'
                                 '<ID>0</ID>\n'
                                 '<DOE>ULH</DOE>\n'
                                 '<inp1>1.2</inp1>\n'
                                 '<inp2>1.1</inp2>\n'
                                 '<out1>2.3</out1>\n'
                                 '<out2>1.32</out2>\n'
                                 '</row-0>')

        self.act_string_table = self.generate_table.read_xml_table(
            self.xml_table_list[0])[:159]

        self.assertEqual(self.act_string_table, self.exp_string_table)

    def test_read_all_tables(self):
        self.exp_string_list = [
            ('\ufeff<?xml version="1.0" '
             'encoding="UTF-8" ?>\n'
             '<root>\n'
             '<row-0>\n'
             '<ID>0</ID>\n'
             '<DOE>ULH</DOE>\n'
             '<inp1>1.2</inp1>\n'
             '<inp2>1.1</inp2>\n'
             '<out1>2.3</out1>\n'
             '<out2>1.32</out2>\n'
             '</row-0>\n<'),
            ('\ufeff<?xml version="1.0" '
             'encoding="UTF-8" ?>\n'
             '<root>\n'
             '<row-0>\n'
             '<ID>0</ID>\n'
             '<DOE>ULH</DOE>\n'
             '<inp1>1.2</inp1>\n'
             '<inp2>1.1</inp2>\n'
             '<out1>2.64</out1>\n'
             '<out2>0.792</out2>\n'
             '</row-0>'),
            ('\ufeff<?xml version="1.0" '
             'encoding="UTF-8" ?>\n'
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

        self.act_string_list = self.generate_table.read_all_tables(
            self.xml_table_list)

        self.act_string_list = [new_str[:161] for new_str in
                                self.act_string_list]

        self.assertEqual(self.act_string_list, self.exp_string_list)


if __name__ == '__main__':
    unittest.main()
