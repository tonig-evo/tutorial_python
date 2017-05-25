# Biopython tutorial

## Sequence handling

Please look at [Biopython_Intro.pdf](../Biopython_Intro.pdf) to answer the following questions for sequence handling.

**Questions**

- What is the fasta format?
- How to open a fasta file with Biopython?
- How to open a fasta file using the open command?
- How can you open (very) large inputfiles?
- How to convert a sequence in a string?
- How to convert a string to a sequence (e.g. DNA, RNA)
- Print the genetic code (standard code and mitochondrial code) using Biopython
- Create following DNA sequence: AAAAGAGAGATGTCCCTACCCTTT
    1) Find the motif “TACC”
    2) Produce the complement
    3) Produce the reverse complement
    4) Transcribe the sequence
    5) Transcribe the reverse complement
    6) Translate the sequence using the Standard code
- What is the difference between Seq and MutableSeq?

## Simple global and local alignments

The module pairwise2 

Info: http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html

The names of the alignment functions in this module follow the convention <alignment type>XX where <alignment type> is either "global" or "local" and XX is a 2 character code indicating the parameters it takes. The first character indicates the parameters for matches (and mismatches), and the second indicates the parameters for gap penalties.

Data: https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/opuntia.fasta


```
from Bio import pairwise2
from Bio import SeqIO
seq1 = SeqIO.read("alpha.faa", "fasta")
seq2 = SeqIO.read("beta.faa", "fasta")
alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)

# How many best alignments exist
len(alignments)

# First alignment
print(alignments[0])
```

