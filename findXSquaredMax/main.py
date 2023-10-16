import random
class Entity:
    def __init__(self, genome_len):
        self.genome_len = genome_len
        self.genome = [random.randint(0, 1) for i in range(genome_len)]

    def __str__(self):
        print("Phenotype:", self.to_phenotype(), "Genotype:", self.genome)

    def to_phenotype(self):
        val = 0
        exp = self.genome_len - 1
        for i in range(self.genome_len):
            val += self.genome[i] * 2^(exp - 1)
        return val
