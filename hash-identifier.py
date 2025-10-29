#!/bin/python3
import sys

import requests


def open_file(hashes):
  file_handle = open(hashes, "rt")
  all_lines = file_handle.readlines()
  file_handle.close()

  return all_lines


def help():
  print("Usage: python3 hash-identifier.py [option] [argument]")
  print(" The options are:")
  print("  -h\t\tShow help options")
  print("  -f\t\tRead the hashes from a file")
  print("  -s\t\tInput a single hash in the cmd line")


def hash_file():
  hashes = sys.argv[2]
  all_lines = open_file(hashes)

  for line in all_lines:
    r = requests.get(f'https://hashes.com/en/api/identifier?hash={line}')
    print(r.text)


def hash_input():
  hash = sys.argv[2]
  r = requests.get(f'https://hashes.com/en/api/identifier?hash={hash}')
  print(r.text)


try:
  flag = sys.argv[1]

  if flag == "-h":
    help()
  if flag == "-s":
    hash_input()
  if flag == "-f":
    hash_file()
except:
  help()
