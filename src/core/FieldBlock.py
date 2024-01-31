class FieldBlock(object):
    pass

class FieldItem(object):
    fieldName: str = ""
    fieldRange: tuple = (0, 0)
    defaultVal: int
    fieldType: str = "RW"
    fieldDesc: str = ""

    def __init__(self) -> None:
        self.fieldName = ""