# External includes
# OS module provides functions for interacting with the operating system
import os
import markdown_generator as mg
from typing import Optional

# Project includes
from granite.generator.output_file_wrapper import OutputFileWrapper

class MarkDownFileWrapper(OutputFileWrapper):
    """
    ...
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the object instance
        """

        # Call the parent class constructor
        super().__init__(filename, ".MD")

        self.md_writer = mg.Writer(self.document)

    def __del__(self) -> None:
        """
        Redefine the class destructor to call its parent's destructor

        """
        super().__del__()

    def write_heading(
        self,
        string: str,
        level: int = 1
    ) -> None:
        """
        Method for initializing a section of source code in Markdown

        :param language: source code language to get synthax coloration
        """
        self.md_writer.write_heading(string, level)
        
    def write(self, string: str) -> None:
        """
        Method for writing a string a section of source code

        :param language: source code language to get synthax coloration
        """
        self.md_writer.write(string)
        
    def _write_hrule(self) -> None:
        """
        Method for writing a horizontal ruler tag to the Markdown file

        """
        self.md_writer.write_hrule()

    def init_code(self, language: str = "c") -> None:
        """
        Method to initialize a source code section

        :param language: source code language to obtain synthetic coloring
        """
        self.code = mg.Code(language)
        
    def append_code(self, string: str) -> None:
        """
        Method to add the string to the code

        :param dict_field: value of the structure fields

        """
        self.code.append(string)

    def _write_code(self) -> None:
        """
        Method for writing the instance of the code object in the markdown file

        """
        self.md_writer.write(self.code)

    def writeline(
        self,
        string: Optional[str] = None
    ) -> None:
        """
        Method for writing a line in the markdown file

        :param string: optional string
        """
        self.md_writer.writeline(string)

    def write_header_table(
        self,
        dict_header: dict
    ) -> None:
        """
        Method for writing the table header to the markdown file

        """
        self.table = mg.Table()
        # For each items in the dictionary
        for key, value in dict_header.items():
            # add the items into the table
            self.table.add_column(key, value)

    def write_table(self) -> None:
        """
        Method of writing the table to the markdown file

        """

        self.write(self.table)

    def append_table(
        self,
        dict_field: dict
    ) -> None:
        """
        Method for appending the input dicionary to the object instance table

        :param dict_field: value of the structure fields
        """

        self.table.append(*['{}'.format(j) for j in dict_field.values()])

    def write_source_code(
        self,
        tc_name: str,
        c_structure: str
    ) -> None:
        """
        Method of writing the source code section in the mardown file

        :param tc_name: telecommand name
        :param c_structure: C strucuture of the telecommand
        """

        self._write_hrule()
        self.init_code("c")
        self.append_code("/* Autogenerated C implementation of the '{}' structure */".format(tc_name))
        self.append_code(c_structure)
        self._write_code()
        self._write_hrule()