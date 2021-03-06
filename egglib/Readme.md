# Egglib Tutorial

EggLib is a C++/Python library and program package for evolutionary genetics and genomics. Main features are sequence data management, sequence polymorphism analysis, and coalescent simulations. EggLib is a flexible Python module with a performant underlying C++ library and allows fast and intuitive development of Python programs and scripts.

Citation: De Mita S. and M. Siol. 2012. EggLib: processing, analysis and simulation tools for population genetics and genomics. BMC Genet. 13:27.

http://mycor.nancy.inra.fr/egglib/

## Installation

- Instructions: http://mycor.nancy.inra.fr/egglib/install.html
- Installation file: http://mycor.nancy.inra.fr/egglib/releases/3.0.0b13/egglib-3.0.0b13.tar.gz

## Quick overview

### Importing egglib

```python
import egglib
print egglib.version
```

### Load an alignment

Egglib supports different file formats, most importantly the fasta format. Details about the fasta format and how Egglib handles fasta files can be found here: http://mycor.nancy.inra.fr/egglib/py/io.html#fasta-format 

The file [codon.aln](codon.aln) contains codon alignments for a gene transcript from Drosophila melanogaster from 28 different Drosophila individuals. Copy the file in your current working directory and try to get basic statistics:

```python
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
```python
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

### Population genetic parameters

```python
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

### Using VCF Files

http://mycor.nancy.inra.fr/egglib/manual/stats-4.html

### Coalescent simulations

http://mycor.nancy.inra.fr/egglib/manual/coal.html

# Excercises 

Following excercises are based on a workshop that can be found here: http://mycor.nancy.inra.fr/egglib/training.html

## Excercise 1: Handling sequences
```python
import egglib

###
print "### exercice 1.1.1 ###"
aln = egglib.io.from_fasta("align1.fas")
###

###
print "### exercice 1.1.2 ###"
print 'Align type:', type(aln)
print 'Align content:', dir(aln)
###

###
print "### exercice 1.1.3 ###"

# two ways to get number of ingroup samples
print "number of ingroup samples:", aln.ns, "or", len(aln)

print "number of outgroup samples:", aln.no
print "length of alignment:", aln.ls
###

###
print "### exercice 1.1.4 ###"
print "first name:", aln.get_name(0)
aln = egglib.io.from_fasta("align1.fas", groups=True)
print "first name:", aln.get_name(0)
print "number of samples:", aln.ns, "outgroup:", aln.no
###

###
print "### exercice 1.2.1 ###"
first = aln[0]
print 'type of sample objects:', type(first)
print 'content of sample objects:', dir(first)
print 'name of 1st sample:', first.name
###

###
print "### exercice 1.2.2 ###"
print 'name of all samples:'
for sam in aln:
    print '   ', sam.name
###

###
print "### exercice 1.2.3 ###"
print 'name of outgroup samples:'
for sam in aln.iter_outgroup():
    print '   ', sam.name
###

###
print "### exercice 1.2.4 ###"
print 'name of 1st sample:', first.name
first.name = "the first sample"
print 'new name of 1st sample:', first.name
print 'check again:', aln.get_name(0)
###

###
print "### exercice 1.3.1 ###"
print 'type of sequence objects:', type(first.sequence)
print '1st sequence as string:', first.sequence.str()
###

###
print "### exercice 1.3.2 ###"
print 'length of sequence:', len(first.sequence)
print 'also:', first.ls
print 'alignment length:', aln.ls
###

###
print "### exercice 1.3.3 ###"
print '1st base of 1st sequence:', first.sequence[0]
print '10 first bases of 1st sequence:', first.sequence[:10]
###

###
print "### exercice 1.3.4 ###"
item = first.sequence[0]
items = first.sequence[:10]
print 'first base as str:', chr(item)
print 'first 10 bases as str:', map(chr, items)
print 'first 10 bases as single str:', ''.join(map(chr, items))
###

###
print "### exercice 1.3.5 ###"
first.sequence[0] = 'N'
print 'set base as N:', chr(first.sequence[0])
first.sequence[0] = 78 # equal to ord('N')
print 'set base as N (as integer):', chr(first.sequence[0])
###

###
print "### exercice 1.3.6 ###"
first.sequence[:10] = 'CGGAGAGCCA'
try:
    first.sequence[:10] = 'CGGAGAGCCAAAA'
except ValueError, e:
    print 'expected error caught with message:', e.message
# the try... except... syntax allows to run a block and catch an error
# out of the scope of this course, but very powerful
###

###
print "### exercice 1.4.1 ###"
print 'type of group objects:', type(first.group)
print 'first label:', first.group[0]
first.group[0] = 267
print 'changed first label:', first.group[0]
###

###
print "### exercice 1.4.2 ###"
print 'number of labels:', len(first.group)
print 'number of levels:', aln.ng
aln.ng = 3
print 'changed number of labels;', len(first.group)
###

###
print "### exercice 1.4.3 ###"
first_outgroup = aln.get_outgroup(0)
print 'number of labels in outgroup sample:', len(first_outgroup.group)
print 'outgroup label:', first_outgroup.group[0]
###

###
print "### exercice 1.5.1 ###"
print '1st name:', aln.get_name(0)
print 'length 1st sequence:', len(aln.get_sequence(0))
print '1st label:', aln.get_label(0, 0)
print '1st base:', chr(aln.get(0, 0))
aln.set(0, 0, 'A')
print 'changed 1st base:', chr(aln.get(0, 0))
###

###
print "### exercice 1.6.1 ###"
print aln.to_fasta()
aln.to_fasta("align1-copy.fas")
aln.to_fasta("align1-copy-lbl.fas", groups=True)
###

###
print "### exercice 1.7.1 ###"
cnt = egglib.io.from_fasta("sequences1.fas")
print 'type for unaligned sequences:', type(cnt)
try:
    aln2 = egglib.io.from_fasta("sequences1.fas", cls=egglib.Align)
except ValueError, e:
    print 'expected error caught with message:', e.message
###

###
print "### exercice 1.7.2 ###"
print 'length of all sequences:'
for sam in cnt:
    print '   ', sam.ls
sample1 = cnt[0]
print 'length of first sequence (1st method):', sample1.ls
print 'length of first sequence (2nd method):', cnt.ls(0)
###

###
print "### exercice 1.7.3 ###"
sample1.sequence.insert(None, 'TATAAAAAAAAAAAAAATATA')
print 'length of first sequence after addition:', cnt.ls(0)
###

###
print "### exercice 1.8.1 ###"
fourth = aln[4]
print 'ns before - align:', aln.ns, 'container:', cnt.ns
cnt.add_sample(fourth.name, fourth.sequence)
aln.del_sample(4)
del fourth # to make sure the SampleView is not used again
print 'ns after - align:', aln.ns, 'container:', cnt.ns
###

###
print "### exercice 1.9.1 ###"
sub1 = aln.extract(100, 201)
print "1st fragment - ns:" , sub1.ns, "ls:", sub1.ls
###

###
print "### exercice 1.9.2 ###"
sub2 = aln.extract([0, 10, 20, 25, 30, 50])
print "2nd fragment - ns:" , sub2.ns, "ls:", sub2.ls
###

###
print "### exercice 1.9.3 ###"
sub3 = aln.subset([0, 1, 2, 5, 10, 15, 20, 22, 25, 28])
print "3rd fragment - ns:" , sub3.ns, "ls:", sub3.ls
###

# extract samples from group 2
sub4 = aln.subgroup(2)
print "4th fragment - ns:" , sub4.ns, "ls:", sub4.ls
###

###
print "### exercice 1.10.1 ###"
half1 = aln.extract(0, 4471)
half2 = aln.extract(4471, None)
print 'ls 1st half:', half1.ls
print 'ls 2nd half:', half2.ls

aln2 = egglib.tools.concat(half1, half2, spacer=1000)
print 'ls merged halves with spacer:', aln2.ls
print 'ls original alignment:', aln.ls
###

###
print "### exercice 1.11.1 ###"
pos = [(0, 441), (1419, 4014), (5258, 5960), (6605, 8942)]
rf = egglib.tools.ReadingFrame(pos)
prot = egglib.tools.translate(aln, frame=rf)
prot.to_fasta('align1-prot.fas')
print 'translated alignment - ns:', prot.ns, 'ls:', prot.ls
###

###
print "### exercice 1.11.2 ###"
print 'number of trailing stop codons:', egglib.tools.trailing_stops(aln, frame=rf)
print 'test for stop codons in alignment:', egglib.tools.has_stop(aln, frame=rf)
###
```
## Excercise 2: Population genetics
```python
import egglib

###
print '### exercice 2.1.1 ###'
aln = egglib.io.from_fasta('align1.fas', groups=True)
###

###
print '### exercice 2.1.2 ###'
cs = egglib.stats.ComputeStats()
cs.add_stat('S')
cs.add_stat('ls')
cs.add_stat('ls_o')
cs.add_stat('thetaW')
cs.add_stat('Pi')
cs.add_stat('D')
cs.add_stat('Hsd')
###

###
print '### exercice 2.1.3 ###'
stats = cs.process_align(aln)
print stats
###

###
print '### exercice 2.1.4 ###'
print 'analyzed sites:', stats['ls']
print 'align ls:', aln.ls
print 'thetaW/site:', stats['thetaW']/stats['ls']
print 'analyzed orientable sites:', stats['ls_o']
###

###
print '### exercice 2.2.1 ###'
struct = egglib.stats.Structure.make_from_dataset(aln, lvl_pop=0)
print struct.as_dict()
###

###
print '### exercice 2.2.2 ###'
cs.set_structure(struct)
cs.add_stat('Dxy')
cs.add_stat('Snn')
cs.add_stat('WCst')
print cs.process_align(aln)
###

###
print '### exercice 2.3.1 ###'
cs.configure(max_missing_freq=0.25)
###

###
print '### exercice 2.3.2 ###'
cs.set_structure(struct)
cs.add_stat('S')
cs.add_stat('thetaW')
cs.add_stat('Pi')
cs.add_stat('D')
cs.add_stat('Hsd')
cs.add_stat('ls')
cs.add_stat('Dxy')
cs.add_stat('Snn')
cs.add_stat('WCst')
###

###
print '### exercice 2.3.3 ###'
stats2 = cs.process_align(aln)
print stats2
###

###
print '### exercice 2.3.4 ###'
print 'ls:', stats['ls'], stats2['ls']
print 'S:', stats['S'], stats2['S']
print 'D:', stats['D'], stats2['D']
print 'thetaW:', stats['thetaW'], stats2['thetaW']
print 'thetaW/site:', stats['thetaW']/stats['ls'], stats2['thetaW']/stats2['ls']
###

####
print '### exercice 2.4.1 ###'
pos, mat = egglib.stats.matrix_LD(aln, 'rsq', max_maj=0.8)
print len(pos), len(mat)
####

####
print '### exercice 2.4.2 ###'
x = []
y = []
for i,row in enumerate(mat):
    for j,v in enumerate(row):
        if v is not None:
            x.append(pos[i]-pos[j])
            y.append(v)
####

####
print '### exercice 2.4.3 ###'
from matplotlib import pyplot
pyplot.plot(x, y, ls='None', marker='o', mec='k', mfc='None', ms=3)
pyplot.xlabel('distance')
pyplot.ylabel('r square')
pyplot.ylim(0, 1.05)
pyplot.savefig('figure1.png')
pyplot.clf()
####

####
import random
print '### exercice 2.4.4 ###'
aln2 = egglib.io.from_fasta('align2.fas')
pos, mat = egglib.stats.matrix_LD(aln2, 'rsq', max_maj=0.8)
x = []
y = []
for i,row in enumerate(mat):
    for j,v in enumerate(row):
        if v is not None:
            x.append(pos[i]-pos[j])
            y.append(v+random.normalvariate(0, 0.01))
pyplot.plot(x, y, ls='None', marker='o', mec='k', mfc='None', ms=3)
pyplot.xlabel('distance')
pyplot.ylabel('r square')
pyplot.ylim(0, 1.05)
pyplot.savefig('figure2.png')
pyplot.clf()
####

###
print '### exercice 2.5.1 ###'
rf = egglib.tools.ReadingFrame([(0, 441), (1419, 4014), (5258, 5960), (6605, 8942)])
###

###
print '### exercice 2.5.2 ###'
cd = egglib.stats.CodingDiversity(aln, frame=rf, max_missing=int(0.5*aln.ns))
###

###
print '### exercice 2.5.3 ###'
print 'codon sites:', cd.num_codons_eff
print 'sites syn:', cd.num_sites_S
print 'sites non-syn:', cd.num_sites_NS
print 'S syn:', cd.num_pol_S
print 'S non-syn:', cd.num_pol_NS
###

###
print '### exercice 2.5.4 ###'
align_S = cd.mk_align_S()
align_NS = cd.mk_align_NS()
print 'align S:', align_S.ns, align_S.ls
print 'align NS:', align_NS.ns, align_NS.ls
###

###
print '### exercice 2.5.5 ###'
codon_filter = egglib.stats.Filter(rng=(0, 63), missing=64)
###

###
print '### exercice 2.5.6 ###'
cs = egglib.stats.ComputeStats()
cs.configure(filtr=codon_filter, max_missing_freq=0.5)
cs.add_stat('nseff')
cs.add_stat('ls')
cs.add_stat('S')
cs.add_stat('D')
cs.add_stat('thetaW')
cs.add_stat('Pi')
###

###
print '### exercice 2.5.7 ###'
statsS = cs.process_align(align_S)
statsNS = cs.process_align(align_NS)
print 'synonymous stats:'
print statsS
print 'non-synonymous stats:'
print statsNS
###

###
print '### exercice 2.5.8 ###'
print 'Pi[S]/site:', statsS['Pi']/cd.num_sites_S
print 'thetaW[S]/site:', statsS['thetaW']/cd.num_sites_S
print 'Pi[NS]/site:', statsNS['Pi']/cd.num_sites_NS
print 'thetaW[NS]/site:', statsNS['thetaW']/cd.num_sites_NS
###
```
