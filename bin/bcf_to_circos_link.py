#!/usr/bin/env python3

"""
A Python3 script to convert BCF files from Delly2 (v0.7.7) to a Circos
compatible file.
"""
from pysam import VariantFile
import argparse
import os
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", help="file to process in Variant Call Format (required)")
    parser.add_argument("--filter", help="flag to filter the data", action="store_true") 
    args = parser.parse_args()

    print("Converting file", args.vcf, "to Circos compatible link file...\n\n")
    bcf_in = VariantFile(args.vcf)
    if args.verbose:
        output_file = ".".join([os.path.splitext(args.vcf)[0], "filtered", "txt"])
    else:
        output_file = ".".join([os.path.splitext(args.vcf)[0], "txt"])
    f = open(output_file, 'w')

    # note that we need to replace "chr" with "hs" for circos to work correctly
    for rec in bcf_in.fetch():
        if args.verbose:
            f.write(" ".join([
                str(rec.contig).replace("chr", "hs"),
                str(rec.pos),
                str(rec.pos + 1),
                str(rec.info["CHR2"]).replace("chr", "hs"),
                str(rec.stop),
                str(rec.stop + 1)]) +
                "\n")
    f.close()

if __name__ == "__main__":
    main()

