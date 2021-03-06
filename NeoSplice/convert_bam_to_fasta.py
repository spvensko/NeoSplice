import pysam
import argparse


def main():
    parser = argparse.ArgumentParser(description='Utility for converting bam file to fasta files.')
    parser.add_argument('--bam_file', required=True, type=str, nargs='?', help='provide input bam file path here')
    parser.add_argument('--R1_out', required=True, type=str, nargs='?', help='provide output R1 fasta file path here')
    parser.add_argument('--R2_out', required=True, type=str, nargs='?', help='provide output R2 fasta file path here')
    args = parser.parse_args()

    outf1 = open(args.R1_out, "w")
    outf2 = open(args.R2_out, "w")
    samfile = pysam.AlignmentFile(args.bam_file, "rb")

    for read in samfile.fetch():
        if not read.is_unmapped and not read.is_secondary and read.is_proper_pair and read.is_paired and\
                not read.is_duplicate and not read.is_supplementary:
            if read.is_read1:
                outf1.write(">" + read.query_name + '\n')
                outf1.write(read.query_alignment_sequence.upper() + '\n')
            elif read.is_read2:
                outf2.write(">" + read.query_name + '\n')
                outf2.write(read.query_alignment_sequence.upper() + '\n')

    samfile.close()
    outf1.close()
    outf2.close()


if __name__ == '__main__':
    main()