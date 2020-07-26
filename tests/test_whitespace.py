import xml_to_csv
import shutil
import os
import filecmp

OUTPUT_PATH = "output_files"
FILEPATH = "tests/test_files/input/whitespace.xml"
OUTPUT_FILEPATH = OUTPUT_PATH + "/12345678901.csv"

def test_whitespace():
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    
    xml_to_csv.convert(FILEPATH)

    with open(OUTPUT_FILEPATH, 'r') as f:
        lines = f.readlines()

        # Check the first line is the 100 header
        assert len(lines[0]) >= 3 and "100," in lines[0] 

        # Check whitespaces and tabs have been stripped 
        # from the beginning and end of all lines
        for line in lines:
            assert ' ' not in line
            assert '\t' not in line

        # Check the last line is the 900 trailer
        assert len(lines[-1]) >= 3 and lines[-1] == "900\n" 

        

