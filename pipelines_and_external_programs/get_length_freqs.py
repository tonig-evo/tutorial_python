import sys

vcf_in = sys.argv[1]  # sys.argv in the sys module allows you to have commandline options in your script
csv_out = sys.argv[2]  # in the this example: python get_length_freqs.py <vcf_in> <csv_out>

length_dict = {}
for line in open(vcf_in):
    if not line.startswith('#'):
        split_line = line.rstrip('\n').split('\t')
        ref_allele = split_line[3]
        alt_allele = split_line[4]
        indel_length = abs(len(ref_allele) - len(alt_allele))
        if indel_length not in length_dict.keys():
            length_dict[indel_length] = 1
        else:
            length_dict[indel_length] += 1

with open(csv_out, 'w') as out:
    for x in sorted(length_dict.keys()):
        out.write(','.join([str(x), str(length_dict[x])]) + '\n')
