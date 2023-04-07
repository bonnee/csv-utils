#!/usr/bin/python

import sys
import argparse
import pandas

parser=argparse.ArgumentParser(description='Subtract two CSV datasets')
parser.add_argument('first', metavar='first', type=open, help='Source dataset')
parser.add_argument('second', metavar='second', type=open, help='Data to remove')
parser.add_argument('-o', '--out', default='output', metavar='output', type=argparse.FileType('w'), help='output file name. default: \'out.csv\'')
parser.add_argument('-c', '--col', default='email', nargs='*', help='space-separated list of columns to match. default: \'email\'')
args=parser.parse_args()

first = pandas.read_csv(args.first, index_col=False, skipinitialspace=True)
second = pandas.read_csv(args.second, index_col=False, skipinitialspace=True)
print('List size:\n{}: {}\n{}: {}'.format(args.first.name, len(first), args.second.name, len(second)))

total = pandas.concat([first, second, second])
diff = total.drop_duplicates(subset=args.col, keep=False)
print('{}: {}'.format(args.out.name, len(diff)))

diff.to_csv(args.out, index=False)

