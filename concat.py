#!/usr/bin/python

import sys
import argparse
import pandas

parser=argparse.ArgumentParser(description='Concatenates CSV datasets excluting duplicates')
parser.add_argument('source', metavar='source', type=open)
parser.add_argument('file', metavar='file', type=open, nargs='+')
parser.add_argument('-o', '--out', default='out.csv', metavar='output', type=argparse.FileType('w'), nargs='?', help='output file name')
parser.add_argument('-c', '--col', default='email', nargs='*', help='space-separated list of columns to match for duplicate detection')
args=parser.parse_args()

source = pandas.read_csv(args.source, index_col=False, skipinitialspace=True)
print('List size:\n{}: {}'.format(args.source.name, len(source)))

file=[]
for f in args.file:
    file.append(pandas.read_csv(f, index_col=False, skipinitialspace=True))
    print('{}: {}'.format(f.name, len(file[-1])))

total = pandas.concat([source, *file])
diff = total.drop_duplicates(subset=args.col, keep="first")
print('{}: {}'.format(args.out.name, len(diff)))

diff.to_csv(args.out, index=False)

