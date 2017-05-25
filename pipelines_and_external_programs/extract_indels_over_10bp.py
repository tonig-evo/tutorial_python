# open output file
output_bed = open('dmel_indels_over_10bp.bed', 'w')

vcf_file = open('dmel_17flys_chr4_indels.vcf', 'r')

# loop through the vcf file
for line in vcf_file:

    # skip header lines
    if line.startswith('#'):
        continue

    # process data lines
    split_line = line.rstrip('\n').split('\t')
    ref_allele = split_line[3]
    alt_allele = split_line[4]
    indel_length = abs(len(ref_allele) - len(alt_allele))

    # get positions for INDELs longer than 10bp
    if indel_length > 10:
        chromo = split_line[0]
        start = str(int(split_line[1]) - 1)  # adjust start coordinate to be 0 based for bed file
        end = str(int(split_line[1]) + len(ref_allele))
        output_string = '\t'.join([chromo, start, end]) + '\n'
        output_bed.write(output_string)

# close files
output_bed.close()
vcf_file.close()
