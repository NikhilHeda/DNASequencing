def overlap(a, b, min_len=3):
	start = 0
	
	while True:
		start = a.find(b[:min_len], start)
		
		if start == -1:
			return 0
		
		if b.startswith(a[start:]):
			return len(a) - start
		
		start += 1

test_set = [
'GTGTACCACGTACTGATGTACTATTTGAAGCTTAT',
'CCCAATTCCTAATGTACTATTTGAAGCTTATTCGG',
'CATAAGCTTCATGATGAAGCTTATTCGGCCAATCG',
'TTTGATTCCTGCTGATGTACTATTTGATGAAGCTT',
'ATGTACTATTTGAAGCTTATTCGGCCAATCGTACT',
'GAAGCTTATTCGGCCAATCGTACTGATGTACTATT',
'CTTATTCGGCCAATCGTACTATTTACTGATGTACA',
'TGATGAAGCTTATTCGGCCAATCGTACTGATGTAC',
'GGCCAATCGTACTGATGTACTATTTGATGAAGCTT',
'CTGATGTACTATTTGATGAAGCTTATTCGGCCAAT',
'TGTACTATTTGATGAAGCTTATCAGTACGTGGAAC',
'AATCGTACTGATGTACTATTTACTGATGTACAATA',
'CTATTTACTGATGTACAATAGTACATCAGTAAAAA'
]

for k1, dna1 in enumerate(test_set, start=1):
	for k2, dna2 in enumerate(test_set, start=1):
		if k1 == k2:
			print('0', end=' ')
		else:
			print(overlap(dna1, dna2, min_len=17), end=' ')
	print()