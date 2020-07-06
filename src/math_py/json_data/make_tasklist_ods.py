from pandas_ods_reader import read_ods

def main():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'    
    path = '{}/data-structures/website-data/data-structures-topics.ods'.format(ROOT)
    
    # https://pypi.org/project/pandas-ods-reader/

    sheet_idx = 1
    df = read_ods(path, sheet_idx, columns=['ID', 'Sub', 'Key', 'Value'])
    
    df.to_csv('{}/data-structures/website-data/data-structures-topics.txt'.format(ROOT), 
               index = False, header=True)
    

if __name__ == '__main__':
    main()

