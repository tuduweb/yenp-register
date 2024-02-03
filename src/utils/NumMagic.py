class RangeMagic(object):

    class MagicSettings(object):
        pass

    @staticmethod
    def CheckRangeListValid(rangeList, order = "asc"):
        # default 0 -> start Check
        _fatal_index = []

        _max_val = -1
        
        for idx, (_start, _end) in enumerate(rangeList):
            if _start != _max_val + 1:
                _fatal_index.append(idx)
            _max_val = _end
        
        # endup check

        print("_fatal_index", _fatal_index)
        pass

if __name__ == "__main__":
    tuple_list = [(0, 1), (2, 4), (5, 6), (6, 9)]
    RangeMagic.CheckRangeListValid(tuple_list)
    RangeMagic.CheckRangeListValid([(0,31),])