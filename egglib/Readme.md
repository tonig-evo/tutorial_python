# Egglib Tutorial

EggLib is a C++/Python library and program package for evolutionary genetics and genomics. Main features are sequence data management, sequence polymorphism analysis, and coalescent simulations. EggLib is a flexible Python module with a performant underlying C++ library and allows fast and intuitive development of Python programs and scripts.

Citation: De Mita S. and M. Siol. 2012. EggLib: processing, analysis and simulation tools for population genetics and genomics. BMC Genet. 13:27.

http://mycor.nancy.inra.fr/egglib/

## Installation

Instructions: http://mycor.nancy.inra.fr/egglib/install.html
Installation file: http://mycor.nancy.inra.fr/egglib/releases/3.0.0b13/egglib-3.0.0b13.tar.gz

## Importing egglib

```
import egglib
print egglib.version
```

## Load an alignment

Egglib supports different file formats, most importantly the fasta format. Details how Egglib handles fasta files can be found here: http://mycor.nancy.inra.fr/egglib/py/io.html#fasta-format 

The file [codon.aln](codon.aln) contains codon alignments for a gene transcript from Drosophila melanogaster from 28 different Drosophila individuals. Copy the file in your current working directory and try to get basic statistics:

```
import egglib
aln = egglib.io.from_fasta('codon.aln')
print aln.ns, aln.ls
```

### Group labels (e.g. subpopulations or outgroups)

Need to be labeled in the Fasta file, e.g.

```
>name1@1,1
AGGTGGCGTGC
>name2@1,2
AGCAGGGGAGC
>name3@2,3
TGGAGGGGTGC
>name4@#4
AGCAGGGGTAC
>name5@#5
AGCAGGGGAAC
```

Information based on this labelling can be accessed as follows:
```
aln = egglib.io.from_fasta("align1.fas",groups=True)
for sam in aln:
  #sam  SampleView
  sam.name # str
  sam.sequence # SequenceView
  sam.sequence.str() # str
  sam.sequence[i] # int
  sam.sequence[i:j] # list
  sam.sequence = "ACGGTGCATTC"
  sam.group # GroupView
  sam.group[i] # int
  sam.group = 5
```

## Population genetic parameters

```
aln1 = egglib.io.from_fasta('codon.aln', cls=egglib.Align, groups=True)
cs = egglib.stats.ComputeStats()

# Choose what statistic you want to use

cs.add_stats('S', 'thetaW', 'Pi', 'D', 'lseff', 'nseff')
stats = cs.process_align(aln1)

# output
print aln1.ns, aln1.ls
print stats
```

A list of the available statistics can be found here: http://mycor.nancy.inra.fr/egglib/py/stats.html#list-stats

## Using VCF Files

http://mycor.nancy.inra.fr/egglib/manual/stats-4.html

## Coalescent simulations

http://mycor.nancy.inra.fr/egglib/manual/coal.html
