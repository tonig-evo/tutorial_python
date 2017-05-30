import subprocess

bed_files = ['dmel_2R_cds.bed', 'dmel_2R_intron.bed', 'dmel_2R_utr.bed']  # this is iterable

# file locations
vcf_file = 'dmel_17flys_chr2R_indels.vcf'

for bed_file in bed_files:

    # we need to change the file naming for our outputs so each iteration of the loop doesn't overwrite the previous
    new_output_prefix = bed_file.replace('.bed', '')  # this removes the '.bed' from the file name

    # we can use this to name our loop specific outputs
    our_output_vcf = new_output_prefix + '.indels.vcf'
    length_csv = new_output_prefix + '.indel_lengths.csv'
    plot_file = new_output_prefix + '.indel_length_plot.png'

    # bedtools intersect
    bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
    subprocess.call(bedtools_cmd, shell=True)

    # length csv creation
    script_cmd = 'python get_length_freqs.py ' + our_output_vcf + ' ' + length_csv
    subprocess.call(script_cmd, shell=True)

    # plot
    plot_cmd = 'Rscript plot_indel_lengths.R ' + length_csv + ' ' + plot_file
    subprocess.call(plot_cmd, shell=True)
