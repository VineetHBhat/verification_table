# Generate Verification Table
This module provides methods to output an xml file of tabular data. The xml file is created after reading a list of input xml files of tabular data. The idea is to capture all values for a *tag* in all the input files and then create a
*non-capturing regex group* with all those values separated by **OR** (`|`) operator. So, if we consider the table that those xml files represent, the *regex* is generated for each cell of the table.

This output table can be used as a baseline or reference when comparing with output at runtime.
