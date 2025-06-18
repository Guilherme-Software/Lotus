import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [graphType, setGraphType] = useState("monthly");
  const [selectedYears, setSelectedYears] = useState([]);
  const [selectedMonths, setSelectedMonths] = useState([]);

  const handleGraphChange = (e) => {
    setGraphType(e.target.value);
  };

  const handleYearChange = (e) => {
    const year = parseInt(e.target.value);
    if (e.target.checked) {
      setSelectedYears(prev => [...prev, year]);
    } else {
      setSelectedYears(prev => prev.filter(y => y !== year));
    }
  };

  const handleMonthChange = (e) => {
    const options = e.target.options;
    const selected = [];
    for (let i = 0; i < options.length; i++) {
      if (options[i].selected && options[i].value !== "0") {
        selected.push(parseInt(options[i].value));
      }
    }
    setSelectedMonths(selected);
  };

  const handleSubmit = async () => {
    try {
      const res = await axios.post(`http://127.0.0.1:5000/api/sales/${graphType}`, {
        years: selectedYears,
        months: selectedMonths,
      });

      console.log(res.data);
    } catch (error) {
      console.error("Erro:", error);
    }
  };

  return (
    <>
      <div className="lotus">
          <h1>LOTUS ICT</h1>
        </div>

      <div className='center'>
        
          <h2>Escolha qual gráfico você deseja visualizar</h2><br />
      </div>

      <div className='center'>
        <select name="graph" id="graph" onChange={handleGraphChange}>
          <option value="monthly">vendas</option>
          <option value="seller">vendedores</option>
          <option value="product">produtos</option>
        </select>
        

        <div>
          <input type="checkbox" value="2024" onChange={handleYearChange} />
          <label htmlFor="2024">2024</label>

          <input type="checkbox" value="2025" onChange={handleYearChange} />
          <label htmlFor="2025">2025</label>
        </div>
      </div>

      <div className='center'>
        <select name="months" id="months" multiple onChange={handleMonthChange}>
          <option value="13">Todos</option>
          <option value="1">janeiro</option>
          <option value="2">fevereiro</option>
          <option value="3">março</option>
          <option value="4">abril</option>
          <option value="5">maio</option>
          <option value="6">junho</option>
          <option value="7">julho</option>
          <option value="8">agosto</option>
          <option value="9">setembro</option>
          <option value="10">outubro</option>
          <option value="11">novembro</option>
          <option value="12">dezembro</option>
        </select>
      </div>
      
      <div className='center'>
        <button type="button" onClick={handleSubmit}>Enviar</button>
      </div>

      
      <footer>
        <div className="flex">
          <div className="footer">
            <span style={{ fontSize: "15px" }}>
              &copy; 2025 Designed by Guilherme dos Santos Lima.
            </span>
          </div>
        </div>
      </footer>
    </>
  );
}

export default App;
