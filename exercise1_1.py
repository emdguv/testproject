codon = "ATG" # initial codon

codon_backwards_lowercase = codon[::-1].lower() # reverse string and convert to lowercase
print(codon_backwards_lowercase) # print codon string

sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg" # sequence to find codon in

codon_position = sequence.find(codon.lower()) # find position of codon (lowercase)
print(codon_position + 1) # print codon position (zero indexed so add 1)

translation_frame = (codon_position % 3) + 1 # modulo by three to find translation frame
print(translation_frame) # print translation frame