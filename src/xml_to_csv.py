import xml.dom.minidom
from line_code import LineCode

OUTPUT_FILES_PATH = "output_files/"

def _getText(nodelist):
    rc = []
    for node in nodelist:

        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
            
    return ''.join(rc)

def _writeDataBlockToCSV(remaining_lines, header, trailer):
    # Writes the 100 header, 200 line, all 300 lines 
    # (until another code is found) and 900 trailer
    outfilename = OUTPUT_FILES_PATH + remaining_lines[0].split(',')[1] + ".csv"

    with open(outfilename, 'w') as o:

        o.write(header)
        o.write(remaining_lines[0])

        for line in remaining_lines[1:]:

            code = LineCode(line)
            if code.is_valid() and code != "200" and code != "900":
                o.write(line)
            else:
                # Stop if the next line is anything other than a 300 line.
                break

        o.write(trailer)

        print("Finished writing %s" % outfilename)
    

def convert(filename):
    """Takes the given file, parses the xml and writes 
    the CSVIntervalData element to CSV files.

    Keyword arguments:
    filename -- the path to the xml file.
    """
    with open(filename, 'r') as f:

        print("Parsing %s using xml.dom.minidom module..." % filename)
        dom = xml.dom.minidom.parse(f) 

        csvIntervalData_nodes = dom.getElementsByTagName("CSVIntervalData")

        for node in csvIntervalData_nodes:

            csvIntervalData_str = _getText(node.childNodes)

            print("Parsing CSVIntervalData node...")
            csv_lines = csvIntervalData_str.splitlines(keepends=True)

            header_found = False
            header = ""
            TRAILER = "900\n"

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
                    _writeDataBlockToCSV(csv_lines[i:], header, TRAILER)
                elif code == "900":
                    header_found = False




