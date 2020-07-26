from line_code import LineCode

LINES = [
    "100,xyz\n", 
    "200,xyz\n",
    "300,xyz\n",
    "900,xyz\n",
    "xyz900\n",
    "invalid line code 99999",
    "\n"
]

EXPECTED_CODES = [
    "100",
    "200",
    "300",
    "900",
    "",
    "",
    ""
]

def test_line_code_value():
    codes = []

    for line in LINES:
        codes.append(LineCode(line))

    for i in range(len(codes)):
        assert codes[i].value == EXPECTED_CODES[i]

def test_valid_code():
    codes = []

    for line in LINES:
        codes.append(LineCode(line))

    for i in range(len(codes)):
        assert codes[i].is_valid() == (True if EXPECTED_CODES[i] else False)

def test_code_eq():
    codes = []

    for line in LINES:
        codes.append(LineCode(line))

    for i in range(len(codes)):
        assert codes[i] == EXPECTED_CODES[i]
        assert not codes[i] == "000"
        