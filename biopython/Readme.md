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

The module pairwise2 implements pairwise sequence alignment using a dynamic programming algorithm

Info: http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html

The names of the alignment functions in this module follow the convention <alignment type>XX where <alignment type> is either "global" or "local" and XX is a 2 character code indicating the parameters it takes. The first character indicates the parameters for matches (and mismatches), and the second indicates the parameters for gap penalties.

Data are two single entry fasta files containing 2 human hemoglobin sequences: (alpha.faa) and (beta.faa)

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

**Questions**
- What is the difference between a local and a global alignment
- Conduct a local alignment with no gap open penalty
- What are the alignment parameters for the follwoing code?

```
from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62
seq1 = SeqIO.read("alpha.faa", "fasta")
seq2 = SeqIO.read("beta.faa", "fasta")
alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
len(alignments)
print(pairwise2.format_alignment(*alignments[0]))
```

## Multiple Sequence objects

Data: https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/opuntia.fasta

```
from Bio import SeqIO
opuntia_dict = SeqIO.index("opuntia.fasta", "fasta")
for x in opuntia_dict:
    print x # sequence identifier/key
    print opuntia_dict[x]
    print str(opuntia_dict[x].seq) # sequence as string
    print opuntia_dict[x].description # full header
```

**Questions**
- What sequence has the highest GC content (Count the GC content for each sequence - percentage of G and C nucleotides in the sequence)?
- What sequence contains the sequence stretch "ATATTCATATTCAATTAAAATTGAA"?

## Finding the taxonomy

```
from Bio import Entrez
Entrez.email = "A.N.Other@example.com"     # Your Email
handle = Entrez.esearch(db="Taxonomy", term="Cypripedioideae") # species of interest
record = Entrez.read(handle)
record["IdList"]
entry=record["IdList"][0]

# Check the entry in the taxonomy database Taxonomy database, and then parse it:

handle = Entrez.efetch(db="Taxonomy", id=entry, retmode="xml")
records = Entrez.read(handle)

# This record stores lots of information:

records[0].keys()
# [u'Lineage', u'Division', u'ParentTaxId', u'PubDate', u'LineageEx',
#  u'CreateDate', u'TaxId', u'Rank', u'GeneticCode', u'ScientificName',
# u'MitoGeneticCode', u'UpdateDate']

#We can get the lineage directly from this record:

records[0]["Lineage"]
#'cellular organisms; Eukaryota; Viridiplantae; Streptophyta; Streptophytina;
# Embryophyta; Tracheophyta; Euphyllophyta; Spermatophyta; Magnoliophyta;
# Liliopsida; Asparagales; Orchidaceae'
```

**Questions**
- Obtain the taxonomy for the three model organisms: *Homo sapiens*, *Arabidopsis thaliana* and *Drosophila melanogaster*

# More information

An exhaustive tutorial can be found at http://biopython.org/DIST/docs/tutorial/Tutorial.html



