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
        <div className="high-chart">
          <HighchartsReact highcharts={Highcharts} options={options} />
        </div>
        </div>
      </div>
    </div>
  );
}

export default App;
