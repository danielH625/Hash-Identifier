#!/bin/python3
import argparse

import requests


# -- CREATES ALL THE COMMAND LINE ARGUMENTS --
def parse_args():
  p = argparse.ArgumentParser(
      description=
      "Hash Identifier - Takes an individual hash or a wordlist of hashes and identifies the hash type"
  )
  # -- GROUP FORCES AT LEAST ONE OF THE COMMAND LINE ARGUMENTS TO BE USED OR IT WILL ERROR AND CALL HELP --
  group = p.add_mutually_exclusive_group(required=True)
  group.add_argument(
      "-s",
      "--string",
      help="Hash: Provide the individual hash (only one, if more add to a file)"
  )
  group.add_argument(
      "-f",
      "--file",
      help=
      "File: Provide the file name with the list of hashes (Each hash on a new line)"
  )
  return p.parse_args()


# -- OPENS THE SPECIFED FILE --
def open_file(hashes):
  file_handle = open(hashes, "rt")
  all_lines = file_handle.readlines()
  file_handle.close()

  return all_lines


# -- RUNS THE HASH CHECK ON A FILE --
def hash_file(hashes_file):
  all_lines = open_file(hashes_file)

  for line in all_lines:
    r = requests.get(f'https://hashes.com/en/api/identifier?hash={line}')
    better_output(r)


# -- RUNS A HASH CHECK ON A INDIVIDUAL HASH --
def hash_input(hash):
  r = requests.get(f'https://hashes.com/en/api/identifier?hash={hash}')
  better_output(r)


# -- TAKES THE REQUEST CUTS OUT THE ALGORITHM TYPE AND PRINTS IT WITHOUT ALL THE FLUFF --
def better_output(r):
  data = r.json()
  algorithms = data["algorithms"]
  hash_type = " ".join(algorithms)
  print(f"[+] Hash algorithm: {hash_type}")


def main():
  args = parse_args()

  if args.string:
    hash_input(args.string)
  elif args.file:
    hash_file(args.file)
  else:
    print(args.help)


if __name__ == "__main__":
  main()
