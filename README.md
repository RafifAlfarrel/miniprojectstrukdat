# DNA GC-Content Monitor 🧬

Aplikasi web bioinformatika untuk analisis komposisi nukleotida, perhitungan GC/AT rasio, serta translasi sekuens DNA menjadi asam amino.

## Fitur Utama
- **Multi-File Processing**: Mendukung unggah banyak file `.fasta`/`.fastq` sekaligus via *Drag & Drop*.
- **Comprehensive Analysis**: Menghitung statistik nukleotida (A, T, G, C, N), GC Content, AT Content, hingga translasi protein.
- **Dynamic Visualization**: Grafik distribusi GC Content (Top 3) dengan antarmuka yang interaktif.
- **Exportable Results**: Data lengkap hasil analisis dapat diunduh langsung dalam format `.csv`.
- **Professional UI**: Antarmuka responsif dengan tema modern, font Poppins, dan efek *Glassmorphism*.

## Arsitektur Proyek
Aplikasi ini dibangun menggunakan pendekatan *Object-Oriented Programming* (OOP) untuk menjaga kode tetap modular dan mudah dikembangkan:
- `SequenceRecord`: Objek penyimpan data sekuens dan kalkulasi statistik dasar.
- `SequenceParser`: Modul pembaca dan parsing file FASTA/FASTQ.
- `GCAnalyzer`: Modul analisis perbandingan dan *ranking* GC/AT rasio.
- `CSVExporter`: Modul pengolah data menjadi format laporan CSV.

## Pipeline Analisis
```text
Upload FASTA/FASTQ 
      ↓
SequenceParser → List[SequenceRecord]
      ↓
GCAnalyzer → Ranking & Summary
      ↓
Frontend (Dashboard) & Export (CSV)
