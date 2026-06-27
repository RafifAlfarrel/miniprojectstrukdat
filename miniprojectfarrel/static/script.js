const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const statusMsg = document.getElementById('status-message');
const tbody = document.querySelector('#result-table tbody');
const canvas = document.getElementById('gc-canvas');
const ctx = canvas.getContext('2d');

dropZone.addEventListener('click', () => fileInput.click());
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.style.background = 'rgba(255, 255, 255, 0.7)';
});
dropZone.addEventListener('dragleave', () => {
    dropZone.style.background = 'rgba(255, 255, 255, 0.45)';
});
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.style.background = 'rgba(255, 255, 255, 0.45)';
    handleUpload(e.dataTransfer.files);
});
fileInput.addEventListener('change', (e) => handleUpload(e.target.files));

async function handleUpload(files) {
    if (files.length === 0) return;
    
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('file', files[i]);
    }

    statusMsg.textContent = 'Mengekstrak data sekuens...';
    statusMsg.style.color = '#0071e3';

    try {
        const response = await fetch('/upload', { method: 'POST', body: formData });
        const data = await response.json();
        
        if (!response.ok) throw new Error(data.error);

        
        document.getElementById('sum-total').textContent = data.summary.total;
        document.getElementById('sum-avg-gc').textContent = data.summary.avg_gc + '%';

       
        tbody.innerHTML = '';
        data.all_data.forEach(r => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${r.rank}</strong></td>
                <td style="font-family: monospace; font-size: 0.85rem;">${r.id}</td>
                <td>${r.length}</td>
                <td>${r.A}</td>
                <td>${r.T}</td>
                <td>${r.G}</td>
                <td>${r.C}</td>
                <td>${r.N}</td>
                <td style="color: #0071e3; font-weight: 600;">${r.gc_content}%</td>
                <td>${r.at_content}%</td>
                <td style="font-family: monospace; color: #d946ef; font-weight: 600;">${r.protein_preview}</td>
            `;
            tbody.appendChild(tr);
        });

        drawChart(data.top_sequences);
        
        document.getElementById('summary-section').classList.remove('hidden');
        document.getElementById('main-content').classList.remove('hidden');
        
        statusMsg.textContent = 'Analisis berhasil!';
        statusMsg.style.color = '#28cd41';

    } catch (err) {
        statusMsg.textContent = err.message;
        statusMsg.style.color = '#ff3b30';
    }
}

function drawChart(topData) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if(topData.length === 0) return;

    const maxGC = Math.max(...topData.map(d => d.gc_content)) + 10;
    const barWidth = 100;
    const spacing = 80;
    const startX = (canvas.width - ((barWidth * topData.length) + (spacing * (topData.length - 1)))) / 2;

    topData.forEach((data, index) => {
        const barHeight = (data.gc_content / maxGC) * (canvas.height - 60);
        const x = startX + (index * (barWidth + spacing));
        const y = canvas.height - barHeight - 40;

        ctx.fillStyle = 'rgba(0, 113, 227, 0.85)'; 
        ctx.beginPath();
        ctx.roundRect(x, y, barWidth, barHeight, [8, 8, 0, 0]);
        ctx.fill();

        ctx.fillStyle = '#1d1d1f';
        ctx.font = '600 16px Poppins, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`${data.gc_content}%`, x + (barWidth / 2), y - 12);
        
        ctx.fillStyle = '#86868b';
        ctx.font = '14px Poppins, sans-serif';
        ctx.fillText(`Rank ${data.rank}`, x + (barWidth / 2), canvas.height - 15);
    });
}