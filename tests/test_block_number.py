import xml_to_csv
import shutil
import os

OUTPUT_PATH = "output_files"

def test_no200():
    filepath = "tests/test_files/input/no200.xml"
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    
    xml_to_csv.convert(filepath)

    assert len(os.listdir(OUTPUT_PATH)) == 0

def test_10blocks():
    filepath = "tests/test_files/input/10blocks.xml"
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    
    xml_to_csv.convert(filepath)

    assert len(os.listdir(OUTPUT_PATH)) == 10

def test_1000blocks():
    filepath = "tests/test_files/input/1000blocks.xml"
    shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    
    xml_to_csv.convert(filepath)

    assert len(os.listdir(OUTPUT_PATH)) == 1000

