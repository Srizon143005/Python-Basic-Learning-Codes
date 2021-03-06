#    Modify the program from Exercise 3 to ask for a sequence then say whether each restriction site is or is not present
#    
#    Enter a sequence: AGAATTC
#    GAATTC is in the sequence: True
#    GGATCC is in the sequence: False
#    AAGCTT is in the sequence: False


restriction_sites = [
    "GAATTC",   # EcoRI
    "GGATCC",   # BamHI
    "AAGCTT",   # HinDIII
]

seq = input("Enter a sequence: ")

for sites in restriction_sites:
    print(sites, "is in the sequence:", sites in seq)