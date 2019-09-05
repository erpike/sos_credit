# ==== TASK 5 ==== #
#
# use the next command in command line for reading last n rows:
# python read_rows.py --rows-count=<n>


import getopt, sys


def read_last_n_rows(file='test.txt', encoding='utf-8', rows_count=0):
    try:
        with open(file=file, mode='r', encoding=encoding) as f:
            for line in f.readlines()[-rows_count:]:
                print(line, end='')
    except FileNotFoundError:
        sys.exit('There\'s no file to read. Generate file by running '
                 'script: python generate_file.py --rows-count=<enter rows count>')

def main(argv):
    rows_count = None
    try:
        opts, args = getopt.getopt(argv, "r:", ["rows-count=",])
    except getopt.GetoptError:
        sys.exit()
    for opt, arg in opts:
        if opt in ("-r", "--rows-count"):
            try:
                row_count = int(arg)
            except ValueError:
                sys.exit('Rows count should be integer!')
    if not row_count:
        sys.exit()
    read_last_n_rows(rows_count=row_count)


if __name__ == '__main__':
    main(sys.argv[1:])
