class SequenceRecord:
    def __init__(self, seq_id, sequence):
        self.id = seq_id.strip()
        self.sequence = sequence.strip().upper()
        self.length = len(self.sequence)
        self.freq = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}
        self._calculate_composition()
        self.gc_content = self._calculate_gc()
        self.at_content = self._calculate_at()
        self.protein = self._translate()

    def _calculate_composition(self):
        valid_bases = {'A', 'T', 'G', 'C'}
        for base in self.sequence:
            if base in valid_bases:
                self.freq[base] += 1
            else:
                self.freq['N'] += 1

    def _calculate_gc(self):
        if self.length == 0: return 0.0
        return round(((self.freq['G'] + self.freq['C']) / self.length) * 100, 2)

    def _calculate_at(self):
        if self.length == 0: return 0.0
        return round(((self.freq['A'] + self.freq['T']) / self.length) * 100, 2)

    def _translate(self):
        codon_table = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 'TGA':'*'
        }
        protein_seq = ""
        for i in range(0, len(self.sequence) - 2, 3):
            codon = self.sequence[i:i+3]
            protein_seq += codon_table.get(codon, 'X') 
        return protein_seq

    def to_dict(self):
        return {
            "id": self.id, "length": self.length,
            "A": self.freq['A'], "T": self.freq['T'],
            "G": self.freq['G'], "C": self.freq['C'], "N": self.freq['N'],
            "gc_content": self.gc_content, "at_content": self.at_content,
            "protein_preview": self.protein[:15] + "..." if len(self.protein) > 15 else self.protein,
            "protein_full": self.protein
        }