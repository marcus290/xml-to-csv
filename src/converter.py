import xml_to_csv
import sys

filepath = sys.argv[1] if len(sys.argv) > 1 else "tests/test_files/input/testfile.xml"

xml_to_csv.convert(filepath)