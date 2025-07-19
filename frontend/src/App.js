import React, { useEffect, useRef, useState } from 'react';

function App() {
  const videoRef = useRef(null);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        videoRef.current.srcObject = stream;
        setInterval(() => captureAndSendFrame(), 5000);
      });
  }, []);

  const captureAndSendFrame = async () => {
    const canvas = document.createElement('canvas');
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    canvas.getContext('2d').drawImage(videoRef.current, 0, 0);

    canvas.toBlob(async blob => {
      const formData = new FormData();
      formData.append('frame', blob, 'frame.jpg');

      const res = await fetch('http://localhost:5000/video_feed', {
        method: 'POST',
        body: formData
      });

      const data = await res.json();
      setAlerts(data.alerts);
    }, 'image/jpeg');
  };

  return (
    <div>
      <h1>Proctoring Tool</h1>
      <video ref={videoRef} autoPlay playsInline width="640" height="480" />
      <div>
        <h2>Alerts:</h2>
        <ul>
          {alerts.map((a, i) => <li key={i}>{a}</li>)}
        </ul>
      </div>
    </div>
  );
}

export default App;
