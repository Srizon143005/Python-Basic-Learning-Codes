#    Read the file sequences.seq 
#    Print out the line number (starting with 1) then the line.  Remember to use rstrip() to remove the extra newline.
#    
#    The output should look like this
#    1 CCTGTATTAGCAGCAGATTCGATTAGCTTTACAACAATTCAATAAAATAGCTTCGCGCTAA
#    2 ATTTTTAACTTTTCTCTGTCGTCGCACAATCGACTTTCTCTGTTTTCTTGGGTTTACCGGAA
#    3 TTGTTTCTGCTGCGATGAGGTATTGCTCGTCAGCCTGAGGCTGAAAATAAAATCCGTGGT
#    4 CACACCCAATAAGTTAGAGAGAGTACTTTGACTTGGAGCTGGAGGAATTTGACATAGTCGAT
#    5 TCTTCTCCAAGACGCATCCACGTGAACCGTTGTAACTATGTTCTGTGC
#    6 CCACACCAAAAAAACTTTCCACGTGAACCGAAAACGAAAGTCTTTGGTTTTAATCAATAA
#    7 GTGCTCTCTTCTCGGAGAGAGAAGGTGGGCTGCTTGTCTGCCGATGTACTTTATTAAATCCAATAA
#    8 CCACACCAAAAAAACTTTCCACGTGTGAACTATACTCCAAAAACGAAGTATTGGTTTATCATAA
#    9 TCTGAAAAGTGCAAAGAACGATGATGATGATGATAGAGGAACCTGAGCAGCCATGTCTGAACCTATAGC
#    10 GTATTGGTCGTCGTGCGACTAAATTAGGTAAAAAAGTAGTTCTAAGAGATTTTGATGATTCAATGCAAAGTTCTATTAATCGTTCAATTG

filename = "Chapter Specification/sequence.txt"
i=1

for line in open(filename):
    line = line.rstrip()
    print(i, line)
    i=i+1
