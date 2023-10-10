#!/usr/bin/python3

import sys
import os
import iupred3_lib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("seqfile", help="FASTA formatted sequence file")
parser.add_argument("iupred_type", help="Analysis type: \"long\", \"short\" or \"glob\"")
parser.add_argument("-a", "--anchor", help="Enable ANCHOR2 prediction",
                    action="store_true")
parser.add_argument("-s", "--smoothing", help="Smoothing type: \"no\", \"medium\" or \"strong\". Default is \"medium\"",
                    default="medium")
# parser.add_argument("-e", "--experimental", help="Filter experimentally verified regions.",
#                     action="store_true")
args = parser.parse_args()

PATH = os.path.dirname(os.path.realpath(__file__))

if args.smoothing not in ['no', 'medium', 'strong']:
    raise ValueError('Smoothing (-s, --smoothing) must be either \"no\", \"medium\" or \"strong\"!')

sequence = iupred3_lib.read_seq(args.seqfile)
iupred2_result = iupred3_lib.iupred(sequence, args.iupred_type, smoothing=args.smoothing)
if args.anchor:
    anchor2_res = iupred3_lib.anchor2(sequence)
total_score = 0
num_positions = len(sequence)

for pos, residue in enumerate(sequence):
    total_score += iupred2_result[0][pos]

average_score = total_score / num_positions
print(average_score)
print("Average IUPred2 Score: {:.4f}".format(average_score))
