function ShareDetails(props) {
  const {
    smallestValue,
    largestValue,
    valueAtTheStart,
    valueAtTheEnd,
    shareBasicInfo,
    movingAverageValue,
  } = props;

  const percentageChange = (valueAtTheEnd.y - valueAtTheStart.y) / 100;

  const displayObj = [
    {
      label: 'Smallest Value',
      value: smallestValue.y,
    },
    {
      label: 'EPS',
      value: shareBasicInfo?.eps,
    },
    {
      label: '52 weeks low',
      value: movingAverageValue['52 weeks low'],
    },
    {
      label: 'largest Value',
      value: largestValue.y,
    },
    {
      label: 'PE Ratio',
      value: shareBasicInfo?.pe_ratio,
    },
    {
      label: '52 weeks high',
      value: movingAverageValue['52 weeks high'],
    },
    {
      label: 'Value at start',
      value: valueAtTheStart.y,
    },
    {
      label: 'Book Value',
      value: shareBasicInfo?.book_value,
    },
    {
      label: '120 days average',
      value: movingAverageValue['120 days average'],
    },
    {
      label: 'Value at End',
      value: valueAtTheEnd.y,
    },
    {
      label: 'PBV',
      value: shareBasicInfo?.pbv,
    },
    {
      label: '180 days average',
      value: movingAverageValue['180 days average'],
    },
    {
      label: 'Largest Change',
      value: largestValue.y - smallestValue.y,
    },
    {
      label: 'Percentage Divident',
      value: shareBasicInfo?.percentage_bonus,
    },
    {
      label: '30 days average volume',
      value: movingAverageValue['30 days average volume '],
    },
    {
      label: 'Percentage Value (calculated)',
      value: percentageChange,
    },
    {
      label: 'Percentage Bonus',
      value: shareBasicInfo?.percentage_bonus,
    },
    {
      label: 'Out standing Share',
      value: shareBasicInfo?.share_outstanding,
    },
    {
      label: 'Price Change Value',
      value: valueAtTheEnd.y - valueAtTheStart.y,
    },
    {
      label: 'One year yeild',
      value: shareBasicInfo?.one_year_yield,
    },
    {
      label: 'Right Share',
      value: shareBasicInfo?.right_share,
    },
  ];

  return (
    <div className="share_detail-border-color row">
      <table className="table table-dark">
        <tbody>
          {displayObj.map((data, index) => {
            if ((index + 1) % 3 === 0) {
              return (
                <tr>
                  <td>
                    <strong>
                      {displayObj[index - 2].label} :{' '}
                      {displayObj[index - 2].value}
                    </strong>
                  </td>
                  <td>
                    <strong>
                      {displayObj[index - 1].label} :{' '}
                      {displayObj[index - 1].value}
                    </strong>
                  </td>
                  <td>
                    <strong>
                      {displayObj[index].label} : {displayObj[index].value}
                    </strong>
                  </td>
                </tr>
              );
            }

            return null;
          })}
        </tbody>
      </table>
    </div>
  );
}

export default ShareDetails;
