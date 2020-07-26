'''Convert XML to CSV data and output it to a CSV file.

Functions:
    convert(filename)
'''
import xml.dom.minidom
from line_code import LineCode
from write_to_csv import write_data_block_to_csv

def _get_text(nodelist):
    rc = []
    for node in nodelist:

        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
            
    return ''.join(rc)

def convert(filename):
    '''Takes the given file, parses the XML and writes 
    the CSVIntervalData element to CSV files.

    Parameters:
    filename (str): the path to the input XML file.
    '''
    with open(filename, 'r') as f:

        print("Parsing %s using xml.dom.minidom module..." % filename)
        dom = xml.dom.minidom.parse(f) 

        csvIntervalData_nodes = dom.getElementsByTagName("CSVIntervalData")

        for node in csvIntervalData_nodes:

            csvIntervalData_str = _get_text(node.childNodes)

            print("Parsing CSVIntervalData node...")
            csv_lines = csvIntervalData_str.splitlines()

            header_found = False
            header = ""
            TRAILER = "900"

            for i in range(len(csv_lines)):

                code = LineCode(csv_lines[i])
                if not code.is_valid():
                    continue

                if code == "100":
                    header_found = True
                    header = csv_lines[i]
                elif code == "200" and header_found:
                    # When a line starting with "200" is found nested between a 100 header  
                    # and 900 trailer, writes the data to an individual CSV file. 
                    write_data_block_to_csv(csv_lines[i:], header, TRAILER)
                elif code == "900":
                    header_found = False




