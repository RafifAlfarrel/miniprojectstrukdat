from flask import Flask, render_template, request, jsonify, send_file
from src.sequence_parser import SequenceParser
from src.gc_analyzer import GCAnalyzer
from src.csv_exporter import CSVExporter
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('file')
    if not files or files[0].filename == '':
        return jsonify({'error': 'Pilih minimal satu file FASTA'}), 400

    try:
        all_sequences = []
        for file in files:
            raw_data = file.read()
            all_sequences.extend(SequenceParser.parse(raw_data))
        
        final_results = GCAnalyzer.analyze_and_rank(all_sequences)
        
        total_seq = len(final_results)
        avg_gc = round(sum(r['gc_content'] for r in final_results) / total_seq, 2) if total_seq > 0 else 0

        csv_path = 'static/taksonomi_report.csv'
        CSVExporter.export(final_results, csv_path)

        return jsonify({
            'summary': {'total': total_seq, 'avg_gc': avg_gc},
            'top_sequences': final_results[:3],
            'all_data': final_results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download')
def download():
    return send_file('static/taksonomi_report.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)