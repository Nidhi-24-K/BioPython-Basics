from Bio import Entrez, SeqIO

# Tell NCBI who you are (required by their policy)
Entrez.email = ""

# Fetch the human Insulin gene from GenBank programmatically
handle = Entrez.efetch(db="nucleotide", id="NM_000618", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print(f"Successfully fetched: {record.description}")
print(f"Sequence Length: {len(record.seq)} base pairs")
print(f"First 50 letters: {record.seq[:50]}")
