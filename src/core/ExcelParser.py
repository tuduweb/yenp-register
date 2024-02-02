import YenpRegCore

class ExcelParser(object):
    # need To be Change
    class ParserSettings(object):

        class ParserMapping(object):
            FieldMapping = {
                "name": 3,
                "range": 4,
                "defaultVal": 5,
                "fieldType": 6,
                "description": 7,
            }
            fieldMappingMaxIndex = 7

            RegItemMapping = {
                "name": 0,
                "addr": 1
            }
            pass

        pass

    def ParseRegField(self, fieldItem) -> dict:
        parsedItem = {}
        for _name, _index in self.ParserSettings.ParserMapping.FieldMapping.items():
            if _index >= len(fieldItem):
                continue
            # print(_name, _index, fieldItem[_index])
            parsedItem[_name] = fieldItem[_index]
        
        print(parsedItem)
        return parsedItem

    def ParseRegItem(self, itemData) -> dict:
        parsedItem = {}
        for _name, _index in self.ParserSettings.ParserMapping.RegItemMapping.items():
            if _index >= len(fieldItem):
                continue

            parsedItem[_name] = fieldItem[_index]
        print(parsedItem)
        return parsedItem


if __name__ == "__main__":

    field1 = YenpRegCore.YenpRegField("field1", 1, 0, 0, "desc")
    field2 = YenpRegCore.YenpRegField("field2", 1, 0, 0, "desc")
    reg_item1 = YenpRegCore.YenpRegItem("reg1", 0)
    reg_item1.AddFeilds([field1, field2])

    parser = ExcelParser()
    parser.ParseRegField(('dfx_reg1', '0x000', 'DFXjicunqi', 'reserved', '31:2', "30'h0", 'RW', 'baoliu', 1, 1))