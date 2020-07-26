import xml_to_csv
import shutil
import os
import filecmp

OUTPUT_PATH = "output_files"
FILEPATH = "tests/test_files/input/testfile.xml"

EXPECTED_OUTPUT = [
    "tests/test_files/example/12345678901.csv",
    "tests/test_files/example/98765432109.csv"]

ACTUAL_OUTPUT = [
    "output_files/12345678901.csv",
    "output_files/98765432109.csv"]

def test_testfile_xml():
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    
    xml_to_csv.convert(FILEPATH)

    for i in range(len(EXPECTED_OUTPUT)):
        assert filecmp.cmp(EXPECTED_OUTPUT[i], ACTUAL_OUTPUT[i])

