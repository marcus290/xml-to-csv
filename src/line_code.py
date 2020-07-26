'''Convenience module for handling the first number (line code) of a CSVIntervalData line.

Classes:
    LineCode
'''
class LineCode:
    '''Convenience class for handling the first number of a CSVIntervalData line.

    Attributes
    ----------
        valid_codes (str[]): All valid codes for the line code.
        value (str): The code of a given line.

    Methods
    -------
        is_valid(): Returns a bool depending on whether the line code is a valid code.
    '''
    valid_codes = ["100", "200", "300", "900"]
    value = ""

    def __init__(self, line):
        '''Constructs the LineCode object and sets the value if it is valid.

        Parameters
        ----------
            line (str): The CSVIntervalData line.
        '''
        if len(line) >= 3 and line[:3] in self.valid_codes:
            self.value = line[:3]

    def is_valid(self):
        '''Returns a bool depending on whether the line code is a valid code.

        Returns
        -------
            bool
        '''
        return self.value in self.valid_codes
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
