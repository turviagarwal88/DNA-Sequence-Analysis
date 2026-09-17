dna = "ATCGAGCTG

print("DNA:", dna)
print("Length:", len(dna))

print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C“))

gc = (dna.count("G") + dna.count("C“))/
len(dna)*100

print("GC%:", round(gc, 2))


complement = dna.replace("A","t")
complement = complement.replace('T","a")
complement = complement.replace("C","g")
complement = complement.replace("G","c")
complement = complement.upper()

print("Complement:", complement)
reverse = complement[::-1]

print("Reverse complement:", reverse)

if "ATG" in dna:
print("Start codon found")
else:
print("No start codon found")

if "TAA" in dna or "TAG" in dna or "TGA" in dna:
print("Stop codon found")
else:
print(“No stop codon found")