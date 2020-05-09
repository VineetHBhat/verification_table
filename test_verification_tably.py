import unittest
from verification_table import Verification_table


class Test_verification_table(unittest.TestCase):

    def setUp(self):

        self.xml_table = 'sample_vp_1.xml'
        self.xml_table_list = ['sample_vp_1.xml',
                               'sample_vp_1.xml',
                               'sample_vp_1.xml'
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
            self.xml_table)[:159]

        self.assertEqual(self.act_string_table, self.exp_string_table)


if __name__ == '__main__':
    unittest.main()
