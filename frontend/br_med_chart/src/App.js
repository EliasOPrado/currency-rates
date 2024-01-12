import "./App.css";
import React, { useEffect, useState } from 'react';
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

function App() {
  const [endDate, setEndDate] = useState('');
  const [startDate, setStartDate] = useState('');
  const [exchangeData, setExchangeData] = useState([]);
  const [targetCurrency, setTargetCurrency] = useState('BRL');

  useEffect(() => {
    fetchData();
  }, [targetCurrency, endDate]);

  const fetchData = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/currency-rates/?start_date=${startDate}&end_date=${endDate}&target_currency=${targetCurrency}`
      );
      const data = await response.json();
      setExchangeData(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleButtonClick = (newTargetCurrency) => {
    setTargetCurrency(newTargetCurrency);
  };

  const handleStartDateChange = (event) => {
    setStartDate(event.target.value);
  };

  console.log("END DATE ----->", endDate, startDate)

  const handleEndDateChange = (event) => {
    setEndDate(event.target.value);
  };

  const options = {
    chart: {
      type: 'line', 
    },
    title: {
      text: 'Exchange Rate Data',
    },
    xAxis: {
      categories: Array.isArray(exchangeData) ? exchangeData.map(entry => entry.date) : [],
    },
    yAxis: {
      title: {
        text: 'Exchange Rate',
      },
    },
    series: [
      {
        name: `USD / ${targetCurrency}`,
        data: Array.isArray(exchangeData) ? exchangeData.map(entry => parseFloat(entry.exchange_rate)) : [],
      },
    ],
  };
  

  return (
    <div className="main-container">
      <navbar className="navbar">
        <h3>Elias Challenge</h3>
      </navbar>
      <div className="body-container">
        <div className="left-sidebar">
          <h3 className="title">Consultas</h3>
        </div>
        <div className="chart-info-holder">
          <div className="chart-info">
            <div className="section base">
              <h3 className="title">Moeda Base</h3>
              <div className="buttons">
                <h4 className="button-design">USD</h4>
              </div>
            </div>
            <div className="section ">
              <h3 className="title">Moedas</h3>
              <div className="buttons">
                <button className="button-design" onClick={() => handleButtonClick('BRL')}>BRL</button>
                <button className="button-design" onClick={() => handleButtonClick("EUR")}>EUR</button>
                <button className="button-design" onClick={() => handleButtonClick("JPY")}>JPY</button>
                <div>
                <label>Start Date:</label>
                <input type="date" value={startDate} onChange={handleStartDateChange} max={new Date().toISOString().split('T')[0]} />
        
                <label>End Date:</label>
                <input type="date" value={endDate} onChange={handleEndDateChange} max={new Date().toISOString().split('T')[0]} />
              </div>
              </div>
            </div>
          </div>
          <div className="high-chart">
            <HighchartsReact highcharts={Highcharts} options={options} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
