
#parseGenomeFile.py
#parsing the file formats
from Bio import SeqIO

#fetch content from the file formats - FASTA and genbank
for seq_record in SeqIO.parse("ls_orchid.fasta","fasta"):
    print(seq_record.id) 
    print(repr(seq_record.seq))
    print(len(seq_record))

for seq_record in SeqIO.parse("ls_orchid.gbk","genbank"):
    print(seq_record.id) 
    print(repr(seq_record.seq))
    print(len(seq_record))