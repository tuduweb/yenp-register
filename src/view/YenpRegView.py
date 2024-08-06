import prettytable as pt
 
table = pt.PrettyTable(['No', 'JOBID', 'NAME', 'STATUS'])
table.add_row(['1', '101', 'job1', 'R'])
table.add_row(['2', '102', 'job2', 'R'])
table.add_row(['3', '103', 'job3', 'R'])
table.add_row(['4', '104', 'job4', 'R'])
print(table)

if __name__ == "__main__":
    print("hello world")