import { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css'


function App() {
  
  const sendArquive = async (e) => {
    const arquive = e.target.files[0];
    const formData = new FormData();
    formData.append("file", arquive);

    const res = await fetch("http://127.0.0.1:5000/", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    console.log(data);
  };

  return (
    <>
    <div className="lotus">
      <h1>LOTUS ICT</h1>
    </div>

    <p>Faça o upload do arquivo abaixo.</p>
    <input type="file" accept='.csv' onChange={sendArquive} />

    <footer>
        <div className="flex">
            <div className="footer">
                <span style={{  fontSize: "15px"  }}>&copy; 2025 Designed by Guilherme dos Santos Lima.</span>
            </div>
        </div>
    </footer>
  
  
  </>
    );

}

export default App;