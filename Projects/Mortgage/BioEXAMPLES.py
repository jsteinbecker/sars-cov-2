import Bio
from Bio import Seq
"""
===============
BASICS 
===============
"""
# DEFINE A SEQ OBJECT
fx_STR_TO_SEQ_               = lambda sequence : Seq.Seq(sequence)
s = fx_STR_TO_SEQ_("accggttacgttttttagcgttcagcagtt")


# GET LENGTH
fx_SEQ_LEN_                  = lambda seq : seq.__len__()
fx_SEQ_LEN_(s)
# -----------------




""" 
================
SEARCHES
================
"""
# SEARCH FOR SUBSTR
fx_FIND_IND_                 = lambda seq , pat :       seq.find(pat)

fx_FIND_IND_(Seq.Seq("ACCGGTCGCA"), "TCG")



# COUNT OCCURENCES
fx_COUNT_SUBSTR_             = lambda seq , substr :    seq.count(substr)
fx_COUNT_SUBSTR_OVERLAP_     = lambda seq, substr :     seq.count_overlap(substr)


fx_COUNT_SUBSTR_(s,'tt')
fx_COUNT_SUBSTR_OVERLAP_(s,'tt')

# -----------------

fx_DNA_TO_RNA_              = lambda dna : dna.transcribe()
fx_RNA_TO_DNA_              = lambda rna : rna.back_transcribe()

fx_GET_COMPLEMENT_           = lambda seq : seq.complement()
fx_RNA_TO_PROT_              = lambda seq : seq.translate()

X = fx_RNA_TO_PROT_(Seq.Seq("acucga"))
fx_RNA_TO_PROT_()
rna                        = s.transcribe()           ;rna # DNA -> RNA
rna_back_tx                  = rna.back_transcribe()  ;rna_back_tx # RNA -> DNA

s.complement() # COMPLEMENT STRAND OF SEQ

aa = s.translate() # DNA/RNA TO PROTEIN SEQ

# -----------------

