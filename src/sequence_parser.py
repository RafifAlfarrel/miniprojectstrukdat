from src.sequence_record import SequenceRecord

class SequenceParser:
    @staticmethod
    def parse(file_data):
        records = []
        lines = file_data.decode('utf-8').splitlines()
        current_id, current_seq = None, []

        for line in lines:
            line = line.strip()
            if not line: continue
            if line.startswith(">"):
                if current_id:
                    records.append(SequenceRecord(current_id, "".join(current_seq)))
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
                
        if current_id:
            records.append(SequenceRecord(current_id, "".join(current_seq)))
        
        if not records:
            raise ValueError("File FASTA kosong atau format salah.")
        return records