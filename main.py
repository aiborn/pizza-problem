import sys


input = open(sys.argv[1], "r")

str_args = input.readline().split(" ")
args = [int(str_arg) for str_arg in str_args]

[rows, cols, l, h] = args

print rows, cols, l, h
