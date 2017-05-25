# Egglib Tutorial

EggLib is a C++/Python library and program package for evolutionary genetics and genomics. Main features are sequence data management, sequence polymorphism analysis, and coalescent simulations. EggLib is a flexible Python module with a performant underlying C++ library and allows fast and intuitive development of Python programs and scripts.

Citation: De Mita S. and M. Siol. 2012. EggLib: processing, analysis and simulation tools for population genetics and genomics. BMC Genet. 13:27.

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
