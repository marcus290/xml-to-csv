# xml-to-csv

A simple XML to CSV converter. Accepts an XML file having the given schema and outputs CSV files in the required format for each block of data.

To run:
```
python src/converter.py <input filepath>
```
The output CSV files are written to `output_files`.

If no filepath is given, the default `testfile.xml` will be parsed and converted instead.

If more than one version of python is installed, the script is run with `python3` instead of `python`.

## Automated testing
Pytest is required to run the test suite, which can be installed by `pip install -U pytest`. To run the test suite:
```
pytest
```

## What was done
- Design of the file structure
- Investigate xml parser package in Python
- Write test scenarios/cases
(30 mins)

- Implement solution and testing on testfile.xml, fulfilling the requirements:
  - Create a CSV for each block of data that starts with 200
  - Each CSV will have the 100 row as a header, and the 900 row as the trailer
  - Each CSV will be named from the second field in the 200 row
  - Remove leading and trailing white spaces, newlines, tabs, etc. (from CSVIntervalData text value only, not individual CSV values)
(60 mins)

- Refactoring for better structure, more maintainable and readable code.
(60 mins)

- Test infrastrucure and fixes to code based on tests (as needed)
(120 mins)


## What wasn't done
- Removing leading and trailing white spaces, newlines, tabs, etc. from individual CSV values (none were found in `testfile.xml`)
- More understanding on possible valid input xml files: 
  - Can there be more than one CSVIntervalData element? 
  - Can we assume the individual CSV values are valid and don't need validation?
  - Can a CSV line start with any number other than 100/200/300/900? 
  - In a block of data (after 200) can there be any lines not beginning with 300?

## What would be done with more time
- More understanding of valid input xml files and valid CSVIntervalData elements.
- More validators on input xml files and CSVIntervalData elements.
- More test cases.
- Better separation of functional and unit tests
