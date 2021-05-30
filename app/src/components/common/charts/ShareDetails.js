function ShareDetails(props) {
  const { smallestValue, largestValue, valueAtTheStart, valueAtTheEnd } = props;

  let percentageChange = (valueAtTheEnd.y - valueAtTheStart.y) / 100;

  return (
    <div className="card share_detail-border-color">
      <ul className="list-group list-group-flush">
        <li className="list-group-item">
          <strong>Smallest Value: {smallestValue.y}</strong>
        </li>

        <li className="list-group-item">
          <strong>largest Value: {largestValue.y}</strong>
        </li>

        <li className="list-group-item">
          <strong>Value at start: {valueAtTheStart.y}</strong>
        </li>

        <li className="list-group-item">
          <strong>Value at End: {valueAtTheEnd.y}</strong>
        </li>
        <li className="list-group-item">
          <strong>Largetest Change: {largestValue.y - smallestValue.y}</strong>
        </li>
        <li className="list-group-item">
          <strong>Percentage Value: {percentageChange} %</strong>
        </li>

        <li className="list-group-item">
          <strong>
            Price Change Value: {valueAtTheEnd.y - valueAtTheStart.y}
          </strong>
        </li>
      </ul>
    </div>
  );
}

export default ShareDetails;
