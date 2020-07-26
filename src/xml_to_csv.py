import xml.dom.minidom

OUTPUT_FILES_PATH = "output_files/"

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def writeDataBlockToCSV(remaining_lines, header, trailer):
    outfilename = OUTPUT_FILES_PATH + remaining_lines[0].split(',')[1] + ".csv"

    with open(outfilename, 'w') as o:
        o.write(header)
        o.write(remaining_lines[0])

        for line in remaining_lines[1:]:
            if len(line) < 3:
                continue
            
            code = line[:3]
            if code == "300":
                o.write(line)
            else:
                break

        o.write(trailer)
    

def convert(filename):
    with open(filename, 'r') as f:
        print("Parsing %s using xml.dom.minidom module..." % filename)
        dom = xml.dom.minidom.parse(f) 

        csvIntervalData_nodes = dom.getElementsByTagName("CSVIntervalData")

        csvIntervalData_str = getText(csvIntervalData_nodes[0].childNodes)

        print("Parsing CSVIntervalData...")
        csv_lines = csvIntervalData_str.splitlines(keepends=True)

        header_found = False
        data_block_found = False
        header = ""
        TRAILER = "900\n"
        code = ""

        for i in range(len(csv_lines)):
            if len(csv_lines[i]) < 3:
                continue
            
            code = csv_lines[i][:3]

            if code == "100":
                header_found = True
                header = csv_lines[i]
            elif code == "200" and header_found:
                data_block_found = True
                writeDataBlockToCSV(csv_lines[i:], header, TRAILER)
            elif code == "900":
                header_found = False


