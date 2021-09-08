gene1 = "GATTACCCGATCGATGATCC"
gene2 = "CCGATTAACGATACTGCAAT"
gene3 = "CCGTATATTGCTACTTAACG"

genes = [gene1, gene2, gene3]

pattern = "GATCC"
max_dif = 3
window_size = len(pattern)

def compare_pieces(pattern, piece):
    dif = 0
    for index, p in enumerate(pattern):
        if p != piece[index]: dif += 1
    return dif

i = 0
for gene_index, g in enumerate(genes):
    for i in range(len(g) - window_size + 1):
        piece = g[i:i+window_size]
        errors = compare_pieces(pattern, piece)
        if errors < (max_dif+1): print("at gene{} -- pattern: {} -- piece: {} -- erros: {}".format(gene_index+1, pattern, piece, errors))
