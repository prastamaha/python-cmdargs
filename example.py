import argparse

# create argumentParser instance
ap = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required=True, help='name of the user')
ap.add_argument('-c', '--class-name', required=False, help='class name of the user') # value will None if not filled 
args = vars(ap.parse_args())    # will return dict

# print(args)
print('hello {}, welcome to the command line arguments'.format(args['name']))
if args['class_name'] != None:
    print('my class name is {}'.format(args['class_name']))

# --class-name will be parse to args['class_name'] by argparse when you called
    