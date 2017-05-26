# Egglib Tutorial

EggLib is a C++/Python library and program package for evolutionary genetics and genomics. Main features are sequence data management, sequence polymorphism analysis, and coalescent simulations. EggLib is a flexible Python module with a performant underlying C++ library and allows fast and intuitive development of Python programs and scripts.

Citation: De Mita S. and M. Siol. 2012. EggLib: processing, analysis and simulation tools for population genetics and genomics. BMC Genet. 13:27.

http://mycor.nancy.inra.fr/egglib/

## Installation

### Instructions

http://mycor.nancy.inra.fr/egglib/install.html

### File

http://mycor.nancy.inra.fr/egglib/releases/3.0.0b13/egglib-3.0.0b13.tar.gz

## Importing egglib

```
import egglib
print egglib.version
```

## Load an alignment

The file [codon.aln](codon.aln) contains codon alignments for a gene transcript from Drosophila melanogaster from 28 different Drosophila individuals. Copy the file in your current working directory.

```
import egglib
aln = egglib.io.from_fasta('codon.aln')
print aln.ns, aln.ls
```

### Group labels (e.g. subpopulations)

Need to be labeled in the Fasta file, e.g.

```
>sample1 @1
ACCGTGGAGAGCGCGTTGCA
>sample2 @1
ACCGTGGAGAGCGCGTTGCA
>sample3 @1
ACCGTGGAGAGCGCGTTGCA
>sample4 @2
ACCGTGGAGAGCGCGTTGCA
>sample5 @2
ACCGTGGAGAGCGCGTTGCA
>sample6 @2
ACCGTGGAGAGCGCGTTGCA
>outgroup @#
ACCGTGGAGAGCGCGTTGCA
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

## Coalescent simulations

http://mycor.nancy.inra.fr/egglib/manual/coal.html
