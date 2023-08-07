import re
import argparse

parser = argparse.ArgumentParser(description="Extract text between <<EOT and EOT in input file.")
parser.add_argument("input_file", help="Path to the input file")
parser.add_argument("output_file", help="Path to the output file")
args = parser.parse_args()

with open(args.input_file, 'r') as file, open(args.output_file, 'w') as output_file:
    output_file.write(re.search(r'<<EOT(.*?)EOT', file.read(), re.DOTALL).group(1).strip())
