import Bio
from Bio import Seq

# BASICS
s = Seq.Seq (data='acttcatttccc')   ;s #DEFINE SEQ FROM STR
seqLen = s.__len__()    ;seqLen # GET LENGTH OF SEQ

# -----------------

# SEARCH
find_ind = s.find('ccc')   ;find_ind # 1st INDEX OF SUBSTRING
count_substr = s.count('tt')     ;count_substr # COUNT OCCURENCES OF SUBSTRING
count_substr_withoverlap = s.count_overlap('tt')   ;count_substr_withoverlap # COUNT OCCURENCES, ALLOW OVERLAPS

# -----------------

# SEQUENCE OPERATIONS
rna = s.transcribe()    ;rna # DNA -> RNA
rna_back_tx = rna.back_transcribe()   ;rna_back_tx # RNA -> DNA

s.complement() # COMPLEMENT STRAND OF SEQ

aa = s.translate() # DNA/RNA TO PROTEIN SEQ

# -----------------
