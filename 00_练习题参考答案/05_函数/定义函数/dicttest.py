import sys

output_dict = {}

def handle_data(arg):
    a, b = arg.split(':')
    output_dict[a] = b

def print_data(a, b):
    print('ID:{} Name:{}'.format(a, b))

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])
