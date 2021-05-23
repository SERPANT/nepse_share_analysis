import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function QuaterlySubPlotAll(props) {
  return (
    <div>
      <Header />
      <NavBar />
      <ChartMapperLine shareData={props.bankShareQuaterlyData} />
    </div>
  );
}

export default QuaterlySubPlotAll;
