# Hash-Identifier
Uses hashes.com to identify an individual hash or a file containing hashes

usage: hash-identifier.py [-h] (-s STRING | -f FILE)

Hash Identifier - Takes an individual hash or a wordlist of hashes and identifies the hash type

options:
  -h, --help            show this help message and exit
  -s STRING, --string STRING
                        Hash: Provide the individual hash (only one, if more add to a file)
  -f FILE, --file FILE  File: Provide the file name with the list of hashes (Each hash on a new line)
