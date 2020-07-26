class LineCode:
    valid_codes = ["100", "200", "300", "900"]
    value = ""

    def __init__(self, line):
        if len(line) >= 3 and line[:3] in self.valid_codes:
            self.value = line[:3]

    def is_valid(self):
        return self.value in self.valid_codes
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
