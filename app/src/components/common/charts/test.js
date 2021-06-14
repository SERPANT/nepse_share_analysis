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
      label: 'largest Value',
      value: largestValue.y,
    },
    {
      label: 'Value at start',
      value: valueAtTheStart.y,
    },
    {
      label: 'Value at End',
      value: valueAtTheEnd.y,
    },
    {
      label: 'Largest Change',
      value: largestValue.y - smallestValue.y,
    },
    {
      label: 'Percentage Value',
      value: percentageChange,
    },
    {
      label: 'Price Change Value',
      value: valueAtTheEnd.y - valueAtTheStart.y,
    },
    {
      label: 'Book Value',
      value: shareBasicInfo.book_value,
    },
    {
      label: 'EPS',
      value: shareBasicInfo.eps,
    },
    {
      label: 'One year yeild',
      value: shareBasicInfo.one_year_yield,
    },
    {
      label: 'PBV',
      value: shareBasicInfo.pbv,
    },
    {
      label: 'PE Ratio',
      value: shareBasicInfo.pe_ratio,
    },
    {
      label: 'Percentage Bonus',
      value: shareBasicInfo.percentage_bonus,
    },
    {
      label: 'Percentage Divident',
      value: shareBasicInfo.percentage_bonus,
    },
    {
      label: 'Right Share',
      value: shareBasicInfo.right_share,
    },
    {
      label: 'Out standing Share',
      value: shareBasicInfo.share_outstanding,
    },
  ];

  Object.keys(movingAverageValue).forEach((key) => {
    const obj = {
      label: key,
      value: movingAverageValue[key],
    };
    displayObj.push(obj);
  });

  return (
    <div className="share_detail-border-color row">
      <table className="table table-dark">
        <tbody>
          {displayObj.map((data, index) => {
            console.log((index + 1) % 3 === 0, index);
            if ((index + 1) % 3 === 0) {
              return (
                <tr>
                  <td>
                    {displayObj[index - 2].label} :{' '}
                    {displayObj[index - 2].value}
                  </td>
                  <td>
                    {displayObj[index - 1].label} :{' '}
                    {displayObj[index - 1].value}
                  </td>
                  <td>
                    {displayObj[index].label} : {displayObj[index].value}
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
