class YenpBasicNumber(object):
    numberString = ""

    def str_coverter(self, input_str: str):
        pass
    pass

def StrCoverter(input_str : str) -> tuple:
    num_str = input_str
    num_result = 0
    num_type = "d"
    num_valid = True

    if num_str.startswith("'"):
        num_str = num_str[1:]
        if num_str.startswith("h"):
            num_type = "h"
            num_str = num_str[1:]
    elif num_str.startswith("h"):
        num_type = "h"
        num_str = num_str[1:]
    elif num_str.startswith("0x"):
        num_type = "h"
        num_str = num_str[2:]
    else:
        # regex
        pass
    # print(num_str)

    try:
        if num_type == "h":
            num_result = int(num_str, 16)
        elif num_type == "d":
            num_result = int(num_str, 10)
    except:
        num_valid = False
        pass
    return num_valid, num_result

if __name__ == "__main__":
    testStrings = [
        "h00",
        "'h33",
        "0x03",
        "h1_0",
        "h1__0"
    ]

    for idx, testItem in enumerate(testStrings):
        print(idx, testItem, StrCoverter(testItem))