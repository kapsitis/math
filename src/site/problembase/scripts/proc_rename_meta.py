import sys




# To rename metainformation field 
# ```python proc_rename_meta.py file_name questionType "Find.All" "FindAll"```
# This command searches for all the patterns:
# * questionType:label1,label2,label3
# If any of labels equals "Find.All", it is renamed into "FindAll"
def main(file_name, prop_name, label1, label2): 
    with open(file_name, mode="r") as f:
        for line in f.readlines():
            if "pattern" in line: 
                continue


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: python proc_rename_meta.py file_name prop_name label1 label2")
    file_name = sys.argv[1]
    prop_name = sys.argv[2]
    label1 = sys.argv[3]
    label2 = sys.argv[4]
    main(file_name=file_name, prop_name=prop_name, label1=label1, label2=label2)


