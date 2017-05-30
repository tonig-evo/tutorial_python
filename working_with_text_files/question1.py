# open output file
output_csv = open('gt_indels_in_frame_freqs.csv', 'w')

vcf_file = open('gt_chrLGE22.vcf', 'r')

# loop through the vcf file
for line in vcf_file:

    # skip header lines
    if line.startswith('#'):
        continue

    # process data lines
    split_line = line.rstrip().split('\t')
    ref_allele = split_line[3]
    alt_allele = split_line[4]
    indel_length = abs(len(ref_allele) - len(alt_allele))

    # get positions for INDELs longer than 10bp
    if indel_length % 3 == 0:
        chromo = split_line[0]

        # get the info column, split it by ;, take the AF column, delete the AF=
        allele_freq = split_line[7].split(';')[1].replace('AF=', '')

        start = split_line[1]
        output_string = ','.join([chromo, start, allele_freq]) + '\n'
        output_csv.write(output_string)

# close files
output_csv.close()
vcf_file.close()
