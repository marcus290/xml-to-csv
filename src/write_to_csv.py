from line_code import LineCode

def write_data_block_to_csv(remaining_lines, header, trailer):
    """Writes the 100 header, 200 line, all 300 lines 
    (until another code is found) and 900 trailer

    Keyword parameters:
    remaining_lines -- Remaining lines in CSVIntervalData to check for data in this block
    header -- The 100 header
    trailer -- The 900 trailer
    """
    outfilename = "output_files/" + remaining_lines[0].split(',')[1] + ".csv"

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