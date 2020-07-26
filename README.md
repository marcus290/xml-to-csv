# xml-to-csv

A simple XML to CSV converter. With an XML file having the given schema, outputs CSV files for each block of data.

Run with:
```
python src/convert_to_csv.py <input filepath>
```
The output CSV files are written to `output_files`.

If no filepath is given, the default `testfile.xml` will be parsed and converted instead.

If more than one version of python is installed, the script is run with `python3` instead of `python`.

Pytest is required to run the test suite, which can be installed by `pip install -U pytest`. The test suite is run with:
```
pytest
```

## What was done

## What wasn't done

## What would be done with more time