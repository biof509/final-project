#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqUtils import GC
import sys
import re
name = str(sys.argv[1])
name2 = name.split('.')
file1 = str(name2[0] + "_plasmid.fasta")
file2 = str(name2[0] + "_chromosome.fasta")
fh2 = open(file2, "a+")
for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
    reg = str(seq_record)
    if re.search("plasmid",reg):
          fh = open(file1, "a+")
          print(">"'%s_plasmid\n%s' % (seq_record.id, seq_record.seq), file=fh)
          fh.close()
    else:
          print(">"'%s_chromosome\n%s' % (seq_record.id, seq_record.seq), file=fh2)

fh2.close()