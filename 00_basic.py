from Bio.Seq import Seq
my_seq=Seq("AGTCACACTGGT")
print(my_seq) # o/p : AGTCACACTGGT
print(my_seq.complement()) # o/p : TCATGTGACCA
print(my_seq.reverse_complement()) # o/p : ACCAGTGTACT
