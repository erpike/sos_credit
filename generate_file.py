# ==== TASK 5 ==== #
#
# use the next command in command line for file generation:
# python generate_file.py --rows-count=<enter rows count>


import getopt, random, sys


START_RAMGE = 0
END_RANGE = 1000000


def generate_rand_number():
    return random.randint(START_RAMGE, END_RANGE)


def generate_file(file='test.txt', mode='w', encoding='utf-8', rows_count=0):
    with open(file=file, mode=mode, encoding=encoding) as f:
        for i in range(rows_count):
            f.write(f'{generate_rand_number()}\n')


def main(argv):
    # filename = None
    rows_count = None
    try:
        opts, args = getopt.getopt(argv, "r:", ["rows-count=",])
    except getopt.GetoptError:
        sys.exit()
    for opt, arg in opts:
        if opt in ("-r", "--rows-count"):
            try:
                rows_count = int(arg)
            except ValueError:
                sys.exit('Rows count should be integer!')
        # elif opt in ("-f", "--filename"):
        #     filename = arg
    if not rows_count: # or not filename:
        sys.exit()
    generate_file(rows_count=rows_count)


if __name__ == '__main__':
    main(sys.argv[1:])
