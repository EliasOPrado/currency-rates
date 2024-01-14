import "./App.css";
import React, { useEffect, useState } from 'react';
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

function App() {
  const [endDate, setEndDate] = useState('');
  const [loading, setLoading] = useState(false);
  const [startDate, setStartDate] = useState('');
  const [exchangeData, setExchangeData] = useState([]);
  const [targetCurrency, setTargetCurrency] = useState('BRL');

  useEffect(() => {
    fetchData();
  }, [targetCurrency, startDate, endDate]);

  const fetchData = async () => {
    try {
      setLoading(true); // Set loading to true when starting the request

      if (startDate && endDate) {
        const response = await fetch(
          `http://127.0.0.1:8000/api/currency-rates/?start_date=${startDate}&end_date=${endDate}&target_currency=${targetCurrency}`
        );
        const data = await response.json();
        setExchangeData(data);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false); // Set loading to false after the request, whether it succeeds or fails
    }
  };

  const handleButtonClick = (newTargetCurrency) => {
    setTargetCurrency(newTargetCurrency);
  };

  const handleStartDateChange = (event) => {
    setStartDate(event.target.value);
  };

  const handleEndDateChange = (event) => {
    setEndDate(event.target.value);
  };

  const options = {
    chart: {
      type: 'line',
      borderColor: '#ccc',
      borderRadius: 10,
      borderWidth: 2,
      responsive: true,
      padding: 10
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
      <div className="body-container">
        <div className="chart-info-holder">
          <div className="chart-info">
            <div className="section base">
              <h3 className="title">Moeda Base</h3>
              <div className="buttons">
                <button className="button-design-fixed">
                <i className="flag-icon flag-icon-us"></i>
                USD
                </button>
              </div>
            </div>
            <div className="section ">
              <h3 className="title">Moedas</h3>
              <div className="buttons">
                <button className="button-design" onClick={() => handleButtonClick('BRL')} disabled={loading}>
                <i className="flag-icon flag-icon-br"></i>
                BRL
                </button>
                <button className="button-design" onClick={() => handleButtonClick("EUR")} disabled={loading}>
                <i className="flag-icon flag-icon-ua"></i>
                EUR
                </button>
                <button className="button-design" onClick={() => handleButtonClick("JPY")} disabled={loading}>
                <i className="flag-icon flag-icon-jp"></i>
                JPY
                </button>
              </div>
            </div>
            <div className="dates">
              <div className="start-date">
                <label>Start Date:</label>
                <input type="date" className="calendar" value={startDate} onChange={handleStartDateChange} max={new Date().toISOString().split('T')[0]} />
              </div>
              <div className="end-date">
                <label>End Date:</label>
                <input type="date" className="calendar" value={endDate} onChange={handleEndDateChange} max={new Date().toISOString().split('T')[0]} />
              </div>
            </div>
          </div>
          {loading && <div className="loading-spinner">Loading...</div>}
          <div className="high-chart">
            <HighchartsReact
             containerProps={{ style: {width: "80%", padding: "30px" } }}
             highcharts={Highcharts} 
             options={options} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
