import "./App.css";
import React, { useEffect, useState } from 'react';
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

function App() {
  const [exchangeData, setExchangeData] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const startDate = '2023-01-01';
        const endDate = '2023-10-05';
        const targetCurrency = 'JPY';

        const response = await fetch(`http://127.0.0.1:8000/api/currency-rates/?start_date=${startDate}&end_date=${endDate}&target_currency=${targetCurrency}`);
        const data = await response.json();
        setExchangeData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const options = {
    chart: {
      type: 'line', 
    },
    title: {
      text: 'Exchange Rate Data',
    },
    xAxis: {
      categories: exchangeData.map(entry => entry.date),
    },
    yAxis: {
      title: {
        text: 'Exchange Rate',
      },
    },
    series: [
      {
        name: `HAS TO PASS THE DATA WHEN BUTTON IS PRESSED......`,
        data: exchangeData.map(entry => parseFloat(entry.exchange_rate)),
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
                <h4 className="button-design">BRL</h4>
                <h4 className="button-design">EUR</h4>
                <h4 className="button-design">JPY</h4>
                <input type="date" id="start" name="trip-start" value="2024-01-12" min="2018-01-01" max="2024-12-31" />
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
