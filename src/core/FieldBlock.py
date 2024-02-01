from enum import Enum

class YenpNodeItem(object):
    class NodeType(Enum):
        NODE_TYPE_BLOCK = 1
        NODE_TYPE_REG = 2
        NODE_TYPE_FIELD = 3
    
    _create_count: int = 0

    idx: int
    name: str
    addr: int
    description: str
    nodeType: NodeType

    parent: object
    childs: list

    def __init__(self, name, addr, description, nodeType, parent = None, childs = []) -> None:

        self.name = name
        self.addr = YenpNodeItem.AddrNumberAdapter(addr)
        self.description = description
        self.nodeType = nodeType

        self.parent = parent
        self.childs = childs

        # please make unique number
        self.idx = YenpNodeItem._create_count
        YenpNodeItem._create_count = YenpNodeItem._create_count + 1
        pass

    # TODO: maybe need to move util tools package
    @staticmethod
    def AddrNumberAdapter(addr: (str, int)) -> int:
        addr_int = 0
        if isinstance(addr, str):
            # cover to int
            addr_int = int(addr)
        elif isinstance(addr, int):
            addr_int = addr
        else:
            # fatal
            pass
        return addr_int

class YenpRegBlock(YenpNodeItem):
    pass

class YenpRegItem(YenpNodeItem):
    def __init__(self, name, offset_addr, description = "") -> None:
        super().__init__(name, offset_addr, description, YenpNodeItem.NodeType.NODE_TYPE_REG)

    def AddFeild(self, yenpFieldItem: object):
        if not isinstance(yenpFieldItem, YenpRegField):
            pass
        
        yenpFieldItem.parent = self
        self.childs.append(yenpFieldItem)

    def AddFeilds(self, yenpFieldItems: list):
        for item in yenpFieldItems:
            self.AddFeild(item)

# data.configure 的 9 个parameter: parent, size, lsb_pos, access, volatile, reset value, has_reset, is_rand, individually accessible

# 参数一，是此域的父辈，也就是此域位于哪个寄存器中，即是 this；
# 参数二，是此域的宽度；
# 参数三，是此域的最低位在整个寄存器的位置，从0开始计数；
# 参数四，表示此字段的存取方式；
# 参数五，表示是否是易失的（volatile），这个参数一般不会使用；
# 参数六，表示此域上电复位后的默认值；
# 参数七，表示此域时都有复位；
# 参数八，表示这个域是否可以随机化；
# 参数九，表示这个域是否可以单独存取。
class YenpRegField(YenpNodeItem):
    fieldRange: tuple = (0, 0)
    defaultVal: int # resetVal
    fieldType: str = "RW"

    def __init__(self, name, size, lsb_pos, reset_value = 0, description = "") -> None:
        super().__init__(name, 0, description, YenpNodeItem.NodeType.NODE_TYPE_FIELD)
        self.fieldRange = (lsb_pos + size, lsb_pos)
        self.defaultVal = reset_value
        self.fieldType = "RW"

        print(self.__dict__)
        print(self.name)

    @staticmethod
    def MakeField():
        pass

    @staticmethod
    def MakeFields(fieldsList: list):
        pass

    @staticmethod
    def CheckFieldsValid(fieldsList: list):
        pass

if __name__ == "__main__":
    field1 = YenpRegField("field1", 1, 0, 0, "desc")
    field2 = YenpRegField("field2", 1, 0, 0, "desc")

    reg_item1 = YenpRegItem("reg1", 0)
    reg_item1.AddFeilds([field1, field2])

    print(reg_item1.__dict__)
