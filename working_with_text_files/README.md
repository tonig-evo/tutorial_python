# Reading, processing and writing text files

This workshop aims to enable you to read in a text file in python, do something with its contents, and write the output to a new file.

## Reading a file

We will be using the file ```gt_chrLGE22.vcf``` for this session. VCF files are a common way of storing genotype information for multiple individuals. The format is described here: <https://samtools.github.io/hts-specs/VCFv4.2.pdf>.

The file consists of header lines starting with ```#```:

```
##fileformat=VCFv4.1
##ALT=<ID=NON_REF,Description="Represents any possible alternative allele at this location">
##FILTER=<ID=LowQual,Description="Low quality">
##FILTER=<ID=Repeats,Description="Overlaps a user-input mask">
##FILTER=<ID=VQSRTrancheINDEL99.00to99.50,Description="Truth sensitivity tranche level for INDEL model at VQS Lod: -1.0205 <= x < -0.7054">
##FILTER=<ID=VQSRTrancheINDEL99.50to99.90,Description="Truth sensitivity tranche level for INDEL model at VQS Lod: -3.5927 <= x < -1.0205">
##FILTER=<ID=VQSRTrancheINDEL99.90to100.00+,Description="Truth sensitivity tranche level for INDEL model at VQS Lod < -66955.4784">
##FILTER=<ID=VQSRTrancheINDEL99.90to100.00,Description="Truth sensitivity tranche level for INDEL model at VQS Lod: -66955.4784 <= x < -3.5927">
##FORMAT=<ID=AD,Number=.,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth (reads with MQ=255 or with bad mates are filtered)">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
```

And data lines that don't start with ```#```:

```
chrLGE22        825     .       AT      A       992.58  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=0.781;ClippingRankSum=2.63;DP=450;FS=6.658;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.00;MQRankSum=0.966;POSITIVE_TRAIN_SITE;QD=24.21;ReadPosRankSum=-1.720e-01;SOR=1.128;VQSLOD=17.46;culprit=MQ    GT:AD:DP:GQ:PGT:PID:PL  0/0:44,0:44:99:.:.:0,108,1146        0/0:46,0:46:99:.:.:0,109,1296   0/0:58,0:58:99:.:.:0,120,1800   0/0:46,0:46:99:.:.:0,102,1366   0/0:48,0:48:99:.:.:0,114,1471   0/1:17,24:41:99:0|1:799_T_C:1027,0,636       0/0:44,0:44:99:.:.:0,114,1318   0/0:37,0:37:99:.:.:0,102,1530   0/0:39,0:39:99:.:.:0,103,1199   0/0:46,0:46:99:.:.:0,117,1755
chrLGE22        1442    .       GTGTCCCTCTCTGTCCCTCTC   G       953.41  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=1.64;ClippingRankSum=1.71;DP=496;FS=6.514;InbreedingCoeff=-0.0813;MLEAC=1;MLEAF=0.050;MQ=63.99;MQRankSum=1.56;NEGATIVE_TRAIN_SITE;POSITIVE_TRAIN_SITE;QD=21.67;ReadPosRankSum=0.028;SOR=0.914;VQSLOD=0.381;culprit=MQ       GT:AD:DP:GQ:PGT:PID:PL       0/0:51,0:51:75:.:.:0,75,1125    0/0:40,0:40:30:.:.:0,30,450     0/0:50,0:50:87:.:.:0,87,1305    0/0:66,0:66:0:.:.:0,0,1523      0/0:52,0:52:39:.:.:0,39,585 0/1:19,25:44:99:0|1:1419_A_G:987,0,735   0/0:55,0:55:99:.:.:0,108,1540   0/0:33,0:33:36:.:.:0,36,540     0/0:40,0:40:27:.:.:0,27,405     0/0:65,0:65:42:.:.:0,42,630
chrLGE22        1702    .       GC      G       938.81  PASS    AC=2;AF=0.100;AN=20;BaseQRankSum=2.06;ClippingRankSum=0.580;DP=486;FS=0.737;InbreedingCoeff=-0.1111;MLEAC=2;MLEAF=0.100;MQ=60.00;MQRankSum=1.64;POSITIVE_TRAIN_SITE;QD=9.03;ReadPosRankSum=-1.130e-01;SOR=0.596;VQSLOD=16.29;culprit=MQ      GT:AD:DP:GQ:PL  0/0:49,0:49:99:0,112,1347   0/0:43,0:43:99:0,99,1213 0/0:59,0:59:99:0,120,1800       0/0:63,0:63:99:0,119,1800       0/1:31,19:50:99:379,0,709       0/0:47,0:47:99:0,105,1365       0/1:26,28:54:99:601,0,587    0/0:30,0:30:81:0,81,1036        0/0:42,0:42:94:0,94,1227        0/0:47,0:47:99:0,100,1324
chrLGE22        6097    .       A       ATGC    7321.64 PASS    AC=8;AF=0.400;AN=20;BaseQRankSum=-2.830e-01;ClippingRankSum=0.179;DP=484;FS=2.392;InbreedingCoeff=-0.2500;MLEAC=8;MLEAF=0.400;MQ=60.00;MQRankSum=-3.860e-01;POSITIVE_TRAIN_SITE;QD=22.39;ReadPosRankSum=-1.430e-01;SOR=0.572;VQSLOD=16.88;culprit=MQ GT:AD:DP:GQ:PGT:PID:PL  0/1:29,27:56:99:0|1:6097_A_ATGC:1088,0,1434  0/1:18,25:43:99:0|1:6097_A_ATGC:996,0,677       0/1:29,26:55:99:.:.:1005,0,1218 0/0:56,0:56:99:.:.:0,113,1672   0/0:50,0:50:99:.:.:0,120,18001/1:0,36:36:99:.:.:1641,111,0   0/1:20,32:52:99:0|1:6075_C_T:1406,0,1779        0/1:17,13:30:99:.:.:516,0,705   0/0:41,0:41:99:.:.:0,108,1297   0/1:26,29:55:99:.:.:727,0,1048
chrLGE22        6846    .       A       ACTGGCCC        948.58  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=-1.348e+00;ClippingRankSum=0.036;DP=461;FS=6.439;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.00;MQRankSum=0.960;POSITIVE_TRAIN_SITE;QD=22.06;ReadPosRankSum=-3.600e-02;SOR=1.075;VQSLOD=17.54;culprit=MQ      GT:AD:DP:GQ:PGT:PID:PL  0/0:52,0:52:99:.:.:0,120,1800        0/0:39,0:39:99:.:.:0,108,1253   0/0:51,0:51:99:.:.:0,120,1535   0/0:58,0:58:99:.:.:0,120,1800   0/0:38,0:38:99:.:.:0,105,1243   0/0:52,0:52:99:.:.:0,120,1800        0/0:43,0:43:99:.:.:0,117,1601   0/0:39,0:39:99:.:.:0,99,1485    0/0:46,0:46:99:.:.:0,113,1396   0/1:22,21:43:99:0|1:6846_A_ACTGGCCC:983,0,834
chrLGE22        8746    .       CA      C       315.58  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=0.405;ClippingRankSum=-8.850e-01;DP=497;FS=2.349;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.35;MQRankSum=1.50;POSITIVE_TRAIN_SITE;QD=5.54;ReadPosRankSum=0.290;SOR=0.542;VQSLOD=2.69;culprit=QD      GT:AD:DP:GQ:PL  0/0:59,0:59:99:0,120,1800   0/0:56,0:56:99:0,120,1800        0/0:50,0:50:99:0,105,1492       0/0:51,0:51:99:0,120,1800       0/0:54,0:54:99:0,120,1800       0/0:39,0:39:99:0,101,1140       0/1:36,21:57:99:350,0,804    0/0:33,0:33:87:0,87,1305        0/0:48,0:48:99:0,110,1770       0/0:46,0:46:99:0,114,1544
chrLGE22        8937    .       GAA     G       7329.61 PASS    AC=12;AF=0.600;AN=20;BaseQRankSum=0.783;ClippingRankSum=0.042;DP=450;FS=1.852;InbreedingCoeff=0.1667;MLEAC=12;MLEAF=0.600;MQ=60.22;MQRankSum=-2.160e-01;POSITIVE_TRAIN_SITE;QD=23.64;ReadPosRankSum=0.088;SOR=0.596;VQSLOD=3.63;culprit=FS   GT:AD:DP:GQ:PL  1/1:0,43:43:99:1426,130,0   0/0:43,0:45:99:0,126,1151        0/1:17,14:31:99:371,0,483       1/1:0,52:52:99:1734,157,0       1/1:0,48:48:99:1583,144,0       0/0:51,0:51:83:0,83,1365        0/1:18,24:42:99:676,0,479    1/1:0,22:22:66:739,66,0 0/1:19,14:33:99:351,0,572       0/1:20,19:39:99:513,0,564
chrLGE22        9966    .       A       AC      1556.70 PASS    AC=5;AF=0.250;AN=20;BaseQRankSum=-3.560e-01;ClippingRankSum=0.061;DP=440;FS=14.410;InbreedingCoeff=0.2000;MLEAC=5;MLEAF=0.250;MQ=60.16;MQRankSum=-1.670e-01;NEGATIVE_TRAIN_SITE;POSITIVE_TRAIN_SITE;QD=12.35;ReadPosRankSum=-1.420e-01;SOR=2.689;VQSLOD=1.88;culprit=FS      GT:AD:DP:GQ:PL       0/0:25,0:25:72:0,72,674 0/0:39,0:39:99:0,103,1169       0/1:27,12:39:99:218,0,630       0/1:12,21:33:99:479,0,231       0/0:33,0:33:99:0,99,1013        0/0:32,0:32:61:0,61,909      0/0:34,0:34:99:0,99,1048        0/0:13,0:13:36:0,36,540 1/1:0,23:23:72:685,72,0 0/1:19,12:31:99:232,0,419
chrLGE22        10208   .       GAT     G       974.58  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=-1.933e+00;ClippingRankSum=0.982;DP=481;FS=7.306;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.36;MQRankSum=1.39;POSITIVE_TRAIN_SITE;QD=16.80;ReadPosRankSum=-3.740e-01;SOR=0.610;VQSLOD=3.99;culprit=MQRankSum GT:AD:DP:GQ:PL  0/1:31,27:58:99:1009,0,1202  0/0:48,0:48:99:0,120,1800       0/0:55,0:55:99:0,120,1800       0/0:55,0:55:99:0,120,1800       0/0:33,0:33:99:0,99,1013        0/0:41,0:41:99:0,114,1267       0/0:49,0:49:99:0,120,1800    0/0:38,0:38:99:0,100,1152       0/0:44,0:44:99:0,116,1341       0/0:58,0:58:99:0,120,1800
chrLGE22        10702   .       GCCATTTCCAAGCACTTTTGTCC G       855.58  PASS    AC=1;AF=0.050;AN=20;BaseQRankSum=0.597;ClippingRankSum=1.16;DP=563;FS=4.524;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.25;MQRankSum=-9.620e-01;POSITIVE_TRAIN_SITE;QD=19.90;ReadPosRankSum=1.08;SOR=0.275;VQSLOD=2.93;culprit=MQRankSum       GT:AD:DP:GQ:PL  0/1:20,23:43:99:890,0,755    0/0:51,0:51:99:0,120,1800       0/0:67,0:67:99:0,120,1800       0/0:63,0:63:99:0,120,1800       0/0:57,0:57:99:0,120,1800       0/0:60,0:60:99:0,120,1800    0/0:68,0:68:99:0,120,1800       0/0:38,0:38:99:0,99,1139        0/0:46,0:46:99:0,120,1800       0/0:69,0:69:99:0,120,1800
```

Whilst visually these lines look messy they are actually neatly arranged in tab separated columns, which makes working with them in python very straightforward.

The first thing we need to do is make a new python script, and save it in the same directory as this manual.

Then we need to open the file in our script and assign it to a variable, as follows:

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')
```

Once this is done we can start looping through each line in the file using a for loop:

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')
for line in vcf_file:
    # do something for each line
```

At this point it is useful to have an idea of what you want to do. In this case we are going to extract all insertions and deletions over 10 base pairs and write their positions to a ```.bed``` file.

For this task we do not need any of the VCFs header information so we skip it:

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')
for line in vcf_file:
    if line.startswith('#'):
        continue
    # do something for each line
```

We then need to split the tab separated data lines into their columns. The symbol for a tab is ```\t```.

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')
for line in vcf_file:
    if line.startswith('#'):
        continue
    split_line = line.rstrip().split('\t')
```

If we add a ```print``` statement to our code we can better understand how python is processing our file:

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')
for line in vcf_file:
    if line.startswith('#'):
        continue
    split_line = line.rstrip().split('\t')
    print(split_line)
```

Run this code and you will see that python is storing our data line in a list, where each element in the list is a column in the vcf:

```
['chrLGE22', '825', '.', 'AT', 'A', '992.58', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=0.781;ClippingRankSum=2.63;DP=450;FS=6.658;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.00;MQRankSum=0.966;POSITIVE_TRAIN_SITE;QD=24.21;ReadPosRankSum=-1.720e-01;SOR=1.128;VQSLOD=17.46;culprit=MQ', 'GT:AD:DP:GQ:PGT:PID:PL', '0/0:44,0:44:99:.:.:0,108,1146', '0/0:46,0:46:99:.:.:0,109,1296', '0/0:58,0:58:99:.:.:0,120,1800', '0/0:46,0:46:99:.:.:0,102,1366', '0/0:48,0:48:99:.:.:0,114,1471', '0/1:17,24:41:99:0|1:799_T_C:1027,0,636', '0/0:44,0:44:99:.:.:0,114,1318', '0/0:37,0:37:99:.:.:0,102,1530', '0/0:39,0:39:99:.:.:0,103,1199', '0/0:46,0:46:99:.:.:0,117,1755']
['chrLGE22', '1442', '.', 'GTGTCCCTCTCTGTCCCTCTC', 'G', '953.41', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=1.64;ClippingRankSum=1.71;DP=496;FS=6.514;InbreedingCoeff=-0.0813;MLEAC=1;MLEAF=0.050;MQ=63.99;MQRankSum=1.56;NEGATIVE_TRAIN_SITE;POSITIVE_TRAIN_SITE;QD=21.67;ReadPosRankSum=0.028;SOR=0.914;VQSLOD=0.381;culprit=MQ', 'GT:AD:DP:GQ:PGT:PID:PL', '0/0:51,0:51:75:.:.:0,75,1125', '0/0:40,0:40:30:.:.:0,30,450', '0/0:50,0:50:87:.:.:0,87,1305', '0/0:66,0:66:0:.:.:0,0,1523', '0/0:52,0:52:39:.:.:0,39,585', '0/1:19,25:44:99:0|1:1419_A_G:987,0,735', '0/0:55,0:55:99:.:.:0,108,1540', '0/0:33,0:33:36:.:.:0,36,540', '0/0:40,0:40:27:.:.:0,27,405', '0/0:65,0:65:42:.:.:0,42,630']
['chrLGE22', '1702', '.', 'GC', 'G', '938.81', 'PASS', 'AC=2;AF=0.100;AN=20;BaseQRankSum=2.06;ClippingRankSum=0.580;DP=486;FS=0.737;InbreedingCoeff=-0.1111;MLEAC=2;MLEAF=0.100;MQ=60.00;MQRankSum=1.64;POSITIVE_TRAIN_SITE;QD=9.03;ReadPosRankSum=-1.130e-01;SOR=0.596;VQSLOD=16.29;culprit=MQ', 'GT:AD:DP:GQ:PL', '0/0:49,0:49:99:0,112,1347', '0/0:43,0:43:99:0,99,1213', '0/0:59,0:59:99:0,120,1800', '0/0:63,0:63:99:0,119,1800', '0/1:31,19:50:99:379,0,709', '0/0:47,0:47:99:0,105,1365', '0/1:26,28:54:99:601,0,587', '0/0:30,0:30:81:0,81,1036', '0/0:42,0:42:94:0,94,1227', '0/0:47,0:47:99:0,100,1324']
['chrLGE22', '6097', '.', 'A', 'ATGC', '7321.64', 'PASS', 'AC=8;AF=0.400;AN=20;BaseQRankSum=-2.830e-01;ClippingRankSum=0.179;DP=484;FS=2.392;InbreedingCoeff=-0.2500;MLEAC=8;MLEAF=0.400;MQ=60.00;MQRankSum=-3.860e-01;POSITIVE_TRAIN_SITE;QD=22.39;ReadPosRankSum=-1.430e-01;SOR=0.572;VQSLOD=16.88;culprit=MQ', 'GT:AD:DP:GQ:PGT:PID:PL', '0/1:29,27:56:99:0|1:6097_A_ATGC:1088,0,1434', '0/1:18,25:43:99:0|1:6097_A_ATGC:996,0,677', '0/1:29,26:55:99:.:.:1005,0,1218', '0/0:56,0:56:99:.:.:0,113,1672', '0/0:50,0:50:99:.:.:0,120,1800', '1/1:0,36:36:99:.:.:1641,111,0', '0/1:20,32:52:99:0|1:6075_C_T:1406,0,1779', '0/1:17,13:30:99:.:.:516,0,705', '0/0:41,0:41:99:.:.:0,108,1297', '0/1:26,29:55:99:.:.:727,0,1048']
['chrLGE22', '6846', '.', 'A', 'ACTGGCCC', '948.58', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=-1.348e+00;ClippingRankSum=0.036;DP=461;FS=6.439;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.00;MQRankSum=0.960;POSITIVE_TRAIN_SITE;QD=22.06;ReadPosRankSum=-3.600e-02;SOR=1.075;VQSLOD=17.54;culprit=MQ', 'GT:AD:DP:GQ:PGT:PID:PL', '0/0:52,0:52:99:.:.:0,120,1800', '0/0:39,0:39:99:.:.:0,108,1253', '0/0:51,0:51:99:.:.:0,120,1535', '0/0:58,0:58:99:.:.:0,120,1800', '0/0:38,0:38:99:.:.:0,105,1243', '0/0:52,0:52:99:.:.:0,120,1800', '0/0:43,0:43:99:.:.:0,117,1601', '0/0:39,0:39:99:.:.:0,99,1485', '0/0:46,0:46:99:.:.:0,113,1396', '0/1:22,21:43:99:0|1:6846_A_ACTGGCCC:983,0,834']
['chrLGE22', '8746', '.', 'CA', 'C', '315.58', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=0.405;ClippingRankSum=-8.850e-01;DP=497;FS=2.349;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.35;MQRankSum=1.50;POSITIVE_TRAIN_SITE;QD=5.54;ReadPosRankSum=0.290;SOR=0.542;VQSLOD=2.69;culprit=QD', 'GT:AD:DP:GQ:PL', '0/0:59,0:59:99:0,120,1800', '0/0:56,0:56:99:0,120,1800', '0/0:50,0:50:99:0,105,1492', '0/0:51,0:51:99:0,120,1800', '0/0:54,0:54:99:0,120,1800', '0/0:39,0:39:99:0,101,1140', '0/1:36,21:57:99:350,0,804', '0/0:33,0:33:87:0,87,1305', '0/0:48,0:48:99:0,110,1770', '0/0:46,0:46:99:0,114,1544']
['chrLGE22', '8937', '.', 'GAA', 'G', '7329.61', 'PASS', 'AC=12;AF=0.600;AN=20;BaseQRankSum=0.783;ClippingRankSum=0.042;DP=450;FS=1.852;InbreedingCoeff=0.1667;MLEAC=12;MLEAF=0.600;MQ=60.22;MQRankSum=-2.160e-01;POSITIVE_TRAIN_SITE;QD=23.64;ReadPosRankSum=0.088;SOR=0.596;VQSLOD=3.63;culprit=FS', 'GT:AD:DP:GQ:PL', '1/1:0,43:43:99:1426,130,0', '0/0:43,0:45:99:0,126,1151', '0/1:17,14:31:99:371,0,483', '1/1:0,52:52:99:1734,157,0', '1/1:0,48:48:99:1583,144,0', '0/0:51,0:51:83:0,83,1365', '0/1:18,24:42:99:676,0,479', '1/1:0,22:22:66:739,66,0', '0/1:19,14:33:99:351,0,572', '0/1:20,19:39:99:513,0,564']
['chrLGE22', '9966', '.', 'A', 'AC', '1556.70', 'PASS', 'AC=5;AF=0.250;AN=20;BaseQRankSum=-3.560e-01;ClippingRankSum=0.061;DP=440;FS=14.410;InbreedingCoeff=0.2000;MLEAC=5;MLEAF=0.250;MQ=60.16;MQRankSum=-1.670e-01;NEGATIVE_TRAIN_SITE;POSITIVE_TRAIN_SITE;QD=12.35;ReadPosRankSum=-1.420e-01;SOR=2.689;VQSLOD=1.88;culprit=FS', 'GT:AD:DP:GQ:PL', '0/0:25,0:25:72:0,72,674', '0/0:39,0:39:99:0,103,1169', '0/1:27,12:39:99:218,0,630', '0/1:12,21:33:99:479,0,231', '0/0:33,0:33:99:0,99,1013', '0/0:32,0:32:61:0,61,909', '0/0:34,0:34:99:0,99,1048', '0/0:13,0:13:36:0,36,540', '1/1:0,23:23:72:685,72,0', '0/1:19,12:31:99:232,0,419']
['chrLGE22', '10208', '.', 'GAT', 'G', '974.58', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=-1.933e+00;ClippingRankSum=0.982;DP=481;FS=7.306;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.36;MQRankSum=1.39;POSITIVE_TRAIN_SITE;QD=16.80;ReadPosRankSum=-3.740e-01;SOR=0.610;VQSLOD=3.99;culprit=MQRankSum', 'GT:AD:DP:GQ:PL', '0/1:31,27:58:99:1009,0,1202', '0/0:48,0:48:99:0,120,1800', '0/0:55,0:55:99:0,120,1800', '0/0:55,0:55:99:0,120,1800', '0/0:33,0:33:99:0,99,1013', '0/0:41,0:41:99:0,114,1267', '0/0:49,0:49:99:0,120,1800', '0/0:38,0:38:99:0,100,1152', '0/0:44,0:44:99:0,116,1341', '0/0:58,0:58:99:0,120,1800']
['chrLGE22', '10702', '.', 'GCCATTTCCAAGCACTTTTGTCC', 'G', '855.58', 'PASS', 'AC=1;AF=0.050;AN=20;BaseQRankSum=0.597;ClippingRankSum=1.16;DP=563;FS=4.524;InbreedingCoeff=-0.0526;MLEAC=1;MLEAF=0.050;MQ=60.25;MQRankSum=-9.620e-01;POSITIVE_TRAIN_SITE;QD=19.90;ReadPosRankSum=1.08;SOR=0.275;VQSLOD=2.93;culprit=MQRankSum', 'GT:AD:DP:GQ:PL', '0/1:20,23:43:99:890,0,755', '0/0:51,0:51:99:0,120,1800', '0/0:67,0:67:99:0,120,1800', '0/0:63,0:63:99:0,120,1800', '0/0:57,0:57:99:0,120,1800', '0/0:60,0:60:99:0,120,1800', '0/0:68,0:68:99:0,120,1800', '0/0:38,0:38:99:0,99,1139', '0/0:46,0:46:99:0,120,1800', '0/0:69,0:69:99:0,120,1800']
```

As code gets more complicated it is good to keep track of whats going on with comments:

```python
vcf_file = open('gt_chrLGE22.vcf', 'r')

# loop through the vcf file
for line in vcf_file:
    
    # skip header lines
    if line.startswith('#'):
        continue
    
    # process data lines
    split_line = line.rstrip().split('\t')
```

As we want to identify INDEL sites with a certain length we need to know the length of each INDEL we process. We know that reference allele is in the forth column and the alternate allele is in the fifth column so we can ge the INDEL length with the following code:
 
```python
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
    indel_length = len(ref_allele) - len(alt_allele)
    # print statement to check what is going on
    print(ref_allele, alt_allele, indel_length)
```

We get the following output from our print statement:
 
```
AT A 1
GTGTCCCTCTCTGTCCCTCTC G 20
GC G 1
A ATGC -3
A ACTGGCCC -7
```
This shows that we are pulling out the correct columns, but it also shows we are getting negative numbers for lengths which is not meaningful, to fix this we can use ```abs()``` to get the absolute value of the length calculation:

```python
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
```

So now we know the lengths we can selectively process INDELs based on their lengths. In this example if an INDEL is longer than 10bp we want to know its position, (chromosome, start, end) so that we can write a bed file.

```python
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
    if indel_length > 10:
        chromo = split_line[0]
        start = str(int(split_line[1]) - 1)  # adjust start coordinate to be 0 based for bed file
        end = str(int(split_line[1]) + len(ref_allele))
        output_string = '\t'.join([chromo, start, end])
        print(output_string)
```

This code outputs the positions of INDELs over 10bp.

```
chrLGE22	1441	1463
chrLGE22	10701	10725
chrLGE22	39913	39949
chrLGE22	47631	47633
chrLGE22	69768	69770
chrLGE22	69772	69774
chrLGE22	71206	71229
chrLGE22	79124	79126
```

However now we have to write this data to a file. To do this we need open a new file, write to it and close it, in addition we also need to close the vcf file after we have finished reading it.

```python
# open output file
output_bed = open('gt_indels_over_10bp.bed', 'w')

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
    if indel_length > 10:
        chromo = split_line[0]
        start = str(int(split_line[1]) - 1)  # adjust start coordinate to be 0 based for bed file
        end = str(int(split_line[1]) + len(ref_allele))
        output_string = '\t'.join([chromo, start, end])
        output_bed.write(output_string)
        
# close files
output_bed.close()
vcf_file.close()
```

This succeeds in writting a bed file, but when we look inside we see that all the data is compressed onto one line:
 
```
chrLGE22	1441	1463chrLGE22	10701	10725chrLGE22	39913	39949chrLGE22	47631	47633chrLGE22	69768	69770chrLGE22	69772	69774chrLGE22	71206	71229chrLGE22	79124	79126chrLGE22	86321	86323chrLGE22	90821	90842chrLGE22	134979	135001chrLGE22	153956	153958chrLGE22	188528	188578chrLGE22	188930	188943chrLGE22	189180	189182chrLGE22	190405	190422chrLGE22	193655	193669chrLGE22	217604	217606chrLGE22	217625	217660chrLGE22	236384	236402chrLGE22	236404	236421chrLGE22	244930	244932chrLGE22	248170	248183chrLGE22	270343	270357chrLGE22	278074	278119chrLGE22	282490	282520chrLGE22	291811	291843chrLGE22	291902	291934chrLGE22	308885	308913chrLGE22	311307	311322chrLGE22	312629	312645chrLGE22	327394	327427chrLGE22	339846	339870chrLGE22	346699	346701chrLGE22	353756	353769chrLGE22	360069	360092chrLGE22	360343	360358chrLGE22	369710	369727chrLGE22	369850	369878chrLGE22	375985	376006chrLGE22	382705	382724chrLGE22	391925	391938chrLGE22	401980	401997chrLGE22	407394	407396chrLGE22	410060	410076chrLGE22	414250	414297chrLGE22	425014	425037chrLGE22	433077	433079chrLGE22	450051	450077chrLGE22	454477	454479chrLGE22	455444	455459chrLGE22	468515	468517chrLGE22	472525	472569chrLGE22	474798	474815chrLGE22	476146	476165chrLGE22	478309	478311chrLGE22	480926	480940chrLGE22	482358	482373chrLGE22	482551	482575chrLGE22	482574	482595chrLGE22	484195	484197chrLGE22	485779	485781chrLGE22	486196	486209chrLGE22	491073	491088chrLGE22	496078	496117chrLGE22	497801	497826chrLGE22	500720	500750chrLGE22	510949	510973chrLGE22	512267	512280chrLGE22	548308	548325chrLGE22	558314	558328chrLGE22	600296	600311chrLGE22	676795	676813chrLGE22	692562	692564chrLGE22	697314	697338chrLGE22	711377	711397chrLGE22	734750	734767chrLGE22	745451	745453chrLGE22	771889	771925
```

This is because whilst print starts on a new line with each call, write just continues where it left off. To fix this we need to add on a new line character '\n':

```python
# open output file
output_bed = open('gt_indels_over_10bp.bed', 'w')

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
    if indel_length > 10:
        chromo = split_line[0]
        start = str(int(split_line[1]) - 1)  # adjust start coordinate to be 0 based for bed file
        end = str(int(split_line[1]) + len(ref_allele))
        output_string = '\t'.join([chromo, start, end]) + '\n'
        output_bed.write(output_string)
        
# close files
output_bed.close()
vcf_file.close()
```
## Question 1

The allele frequency of each variant is listed in the 8th column of the VCF file in the format ```AF=0.5``` 
(see the extract from the file at the top this page for an example). Use this information to write a comma 
separated file (csv) with three columns: chromosome, position and allele frequency. Output data only for sites
that are a multiple of three in length. You will need to extract the allele frequency making use of ```.split()```.

<details>
<summary>Hint 1</summary>
Think of the 8th column of the VCF as lots of ';' separated columns.
</details>

A potential solution can be found here: [question1.py](question1.py).
 
[Return home](https://github.com/tonig-evo/tutorial_python).