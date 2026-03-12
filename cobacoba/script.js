const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snapBtn = document.getElementById('snap');
const frameOverlay = document.getElementById('frame-overlay');
const downloadLink = document.getElementById('download');

// 1. Akses Kamera
navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(stream => { video.srcObject = stream; })
    .catch(err => console.error("Gagal akses kamera: ", err));

// 2. Ganti Frame Real-time
document.getElementById('frame-selector').addEventListener('change', (e) => {
    frameOverlay.src = e.target.value;
});

// 3. Logika Ambil Foto
snapBtn.addEventListener('click', () => {
    const context = canvas.getContext('2d');
    
    // Gambar Video ke Canvas
    context.drawImage(video, 0, 0, 640, 480);
    
    // Gambar Frame ke atas Video (Canvas)
    const img = new Image();
    img.crossOrigin = "anonymous"; // Hindari error CORS saat download
    img.src = frameOverlay.src;
    
    img.onload = () => {
        context.drawImage(img, 0, 0, 640, 480);
        
        // Tampilkan link download
        const dataURL = canvas.toDataURL('image/png');
        downloadLink.href = dataURL;
        downloadLink.download = 'my-photobooth.png';
        downloadLink.style.display = 'inline-block';
        
        // Sembunyikan video, tunjukkan hasil jika perlu
        video.style.opacity = "0.5"; 
    };
});