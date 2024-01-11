import "./App.css";
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

const options = {
  title: {
    text: "Currencies",
  },
  series: [
    {
      data: [1, 2, 3],
    },
  ],
};

function App() {
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
