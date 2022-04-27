import Bio
from Bio import Seq
"""
===============
BASICS 
===============
"""
# DEFINE A SEQ OBJECT
s                          = Seq.Seq (data='acttcatttccc')   ;s #DEFINE SEQ FROM STR
# GET LENGTH
seqLen                     = s.__len__()              ;seqLen # GET LENGTH OF SEQ

# -----------------
""" 
================
SEARCHES
================
"""
# SEARCH FOR SUBSTR
find_ind                   = s.find('ccc')            ;find_ind # 1st INDEX OF SUBSTRING
# COUNT OCCURENCES
count_substr               = s.count('tt')            ;count_substr # COUNT OCCURENCES OF SUBSTRING
count_substr_withoverlap   = s.count_overlap('tt')    ;count_substr_withoverlap # COUNT OCCURENCES, ALLOW OVERLAPS

# -----------------

# SEQUENCE OPERATIONS
rna                        = s.transcribe()           ;rna # DNA -> RNA
rna_back_tx                  = rna.back_transcribe()  ;rna_back_tx # RNA -> DNA

s.complement() # COMPLEMENT STRAND OF SEQ

aa = s.translate() # DNA/RNA TO PROTEIN SEQ

# -----------------
