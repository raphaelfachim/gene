from itertools import combinations

gene1 = "GATTACCCGATCGATTATCC"
gene2 = "CCGATTAACGATACTGCAAT"
gene3 = "CCGTATATTGCTACTTAACG"

genes = [gene1, gene2, gene3]

pattern = "GATCC"

def find_pattern(pattern, gene, max_dif):
    patterns_list = generate_patterns(pattern, max_dif)
    patterns_list.append(pattern)
    print(patterns_list)
    for p in patterns_list:
        print('gene piece ---- {}'.format(p))
        i = 0
        window_size = len(p)
        for i in range(len(gene) - window_size + 1):
            j = 0
            pieces = []
            for j in range(window_size):
                pieces.append(gene[i+j])
            str_g = "".join(str(g) for g in pieces)
            if str_g == p:
                print('found correspondence for piece {} at index {}'.format(p, i))


def generate_patterns(pattern, max_dif):
    patterns_list = list(combinations(pattern, len(pattern) - max_dif))
    patterns = []
    for p in patterns_list:
          patterns.append("".join(str(i) for i in p))
    return elim_duplicates(patterns)

def elim_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__ == '__main__':
    find_pattern(pattern, gene1, 1)
