# xml-to-csv

A simple XML to CSV converter. Accepts an XML file having the given schema and outputs CSV files in the required format for each block of data.

To run:
```
python src/converter.py <input filepath>
```
The output CSV files are written to `output_files`.

If no filepath is given, the default `testfile.xml` will be parsed and converted instead.

If more than one version of python is installed, the script is run with `python3` instead of `python`.

Pytest is required to run the test suite, which can be installed by `pip install -U pytest`. To run the test suite:
```
pytest
```

## What was done
- Design of the file structure
- Investigate xml parser package in Python
- Write test scenarios/cases
(30 mins)

- Implement solution and testing on testfile.xml
(60 mins)

- Refactoring for better structure, more maintainable and readable code.
(60 mins)

- Test infrastrucure and fixes to code based on tests (as needed)
(90 mins)


## What wasn't done
- More understanding on valid input xml files. 
  - Can there be more than one CSVIntervalData element? 
  - Can a CSV line start with any other number other than those in the example? 
  - In a block of data (after 200) can there be any lines not beginning with 300?

## What would be done with more time
- More understanding of valid input xml files and valid CSVIntervalData elements.
- More validators on input xml files and CSVIntervalData elements.
- More test cases.
- Better separation of functional and unit tests
