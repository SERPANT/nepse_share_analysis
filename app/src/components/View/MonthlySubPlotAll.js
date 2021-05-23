import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function MonthlySubPlotAll(props) {
  return (
    <div>
      <Header />
      <NavBar />
      <ChartMapperLine shareData={props.bankShareMonthlyData} />
    </div>
  );
}

export default MonthlySubPlotAll;
