class GCAnalyzer:
    @staticmethod
    def analyze_and_rank(sequences):
        sequences.sort(key=lambda x: x.gc_content, reverse=True)
        results = []
        for index, seq in enumerate(sequences):
            data = seq.to_dict()
            data['rank'] = index + 1
            results.append(data)
        return results