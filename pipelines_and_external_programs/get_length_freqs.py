length_dict = {}
for line in open('dmel_17flys_chr4_indels_over10bp.vcf'):
    if not line.startswith('#'):
        split_line = line.rstrip('\n').split('\t')
        ref_allele = split_line[3]
        alt_allele = split_line[4]
        indel_length = abs(len(ref_allele) - len(alt_allele))
        if indel_length not in length_dict.keys():
            length_dict[indel_length] = 1
        else:
            length_dict[indel_length] += 1

for x in sorted(length_dict.keys()):
    print ','.join([str(x), str(length_dict[x])])
