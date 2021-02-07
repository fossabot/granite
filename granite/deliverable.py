"""Deliverable handling library."""
# Include the logging module defining the functions and 
# classes that implement a flexible event logging system.
import logging
# Include the datetime module providing classes to manipulate dates and times.
import datetime
# OS module provides functions for interacting with the operating system
import os
from typing import Optional
from pathlib import Path

# Project includes
# IcdXmlAnalysis class needed for furthuer analysis
from granite.analysis.icd_xml import IcdXmlAnalysis

class DeliverableGenerator():
    """
    Generate the package
    """

    def __init__(
        self,
        project_config: dict,
        logger: Optional[str] = None,
        filename = None,
    ):
        """
        Initialize the object instance
        
        :param project_config: configuration of the project item
        :param logger: logger
        :param filename: not used
        """
        
        # self.logger = logger or logging.getLogger()
        # self.logger.name = __name__
        # self.logger.debug("Filename in constructor is {}".format(filename))

        # filename = "C:\\Users\\FARGES\\Documents\\TMP"
        # self.filename = Path(filename).resolve()
        # if self.filename.is_dir():
        #     self.filename.mkdir(exist_ok=True)
        #     self.logger.debug(
        #         "Given path is directory without filename, using default filename."
        #     )
        #     self.filename.joinpath("C:\\Users\\FARGES\\Documents\\TMP", ".md")

        # Initialize the instance configuration
        self._config            = project_config
        self._default_config    = _default_deliv_config
        # Get output folder tree
        self.output_folder_tree = self._get_output_path()
        # Make output directory
        self._make_output_dir()

        input_icd = Path(self._config['INPUT_DIR'], self._config['INPUT_XML_ICD_FILE'] ).resolve()

        output_dir = Path(self._config['OUTPUT_DIR'], self.output_folder_tree).resolve()

        # Make the output directory
        # os.makedirs(output_dir, exist_ok= True)

        IcdXmlAnalysis(input_icd, output_dir)

    def _get_output_path(self) -> str:
        """
        Retrieve the output path
        """

        # Construct a tree structure of output folders based on the information entered by the operator
        try:
            output_folder_tree = '\\'.join([self._config['PROJECT_NAME'], self._config['SW_VERSION']])
        except TypeError as err:
            output_folder_tree = _default_deliv_config["OUTPUT_DIR"]
            print("TypeError in {}: {}".format(__name__, err))

        # Return the output folder
        return output_folder_tree

    def _make_output_dir(self):
        """
        Make the output directory
        """
        # Log informational to the operator
        # logging.info('Creating the output directory...')
        # logging.warning('Creating the output directory...')
        
        try:
            # Retrieve the output directory path
            self.folder = self._config['OUTPUT_DIR']
            
            # Add backslash to construct be able to add additional information to the path
            self.folder = self.folder + "\\"
            
            # Add a custom directory depending on the information of the projet
            self.folder = self.folder + self.output_folder_tree

        except TypeError as err:
            # Retrieve the output directory path
            self.folder = self._default_config['OUTPUT_DIR']
            
            # Add backslash to construct be able to add additional information to the path
            self.folder = self.folder + "\\"
            
            # Add a custom directory depending on the information of the projet
            self.folder = self.folder + self.output_folder_tree
            print("TypeError in {}: {}".format(__name__, err))
            
        finally:
            # Make the output directory
            os.makedirs(self.folder, exist_ok= True)


_default_deliv_config = {

            'PROJECT_NAME':                 'DEFAULT_PROJET_NAME',
            'SW_VERSION':                   '0.0.0',
            'OUTPUT_DIR':                   ".\\examples\\output",
            'INPUT_DIR':                    ".\\examples\\input",
            'INPUT_XML_ICD_FILE':           'SW-ICD.xml',
            'NAME_OUTPUT_FILE':             'SW-ICD',
            'OUTPUT_HEADER_PROLOG':         'Autogenerated header file'

}
