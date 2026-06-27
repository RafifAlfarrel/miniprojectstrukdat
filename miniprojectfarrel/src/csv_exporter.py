import csv
import os

class CSVExporter:
    @staticmethod
    def export(data_list, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Rank", "Sekuens_ID", "Panjang", "A", "T", "G", "C", "N", "GC(%)", "AT(%)", "Translasi_Protein"])
            for r in data_list:
                writer.writerow([r['rank'], r['id'], r['length'], r['A'], r['T'], r['G'], r['C'], r['N'], r['gc_content'], r['at_content'], r['protein_full']])