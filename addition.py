#!/usr/bin/env python3
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('first_number', type=int)
parser.add_argument('second_number', type=int)

args=parser.parse_args()

def addition(x,y):
    print(x + y)

addition(args.first_number, args.second_number)
