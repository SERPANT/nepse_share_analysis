import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import SideBar from '../common/sidebar/sidebar';

import BarChart from '../common/charts/BarChart';

function EPSComparision(props) {
  const { shareCategories, onChangeCategory } = props;

  if (!shareCategories || shareCategories.lengh <= 0) return null;

  return (
    <div>
      <Header />
      <NavBar />
      <div className="row">
        <div className="col-sm-2">
          <SideBar
            onNavItemClick={onChangeCategory}
            shareCategories={shareCategories}
          />
        </div>
        <div className="col-sm-10">
          {shareCategories.map((category) => {
            const data = category.share.map((share) => {
              return {
                x: share.symbol,
                y: parseFloat(share.share_basic_info[0].eps_value),
              };
            });

            return (
              <div className="card share-daily-card">
                <div className="card-header">
                  <h3>{category.name} EPS</h3>
                </div>
                <div className="card-body">
                  <BarChart
                    key={category.id}
                    datasets={[{ label: 'EPS value Comparision', data: data }]}
                    height={500}
                    backgroundColor="rgba(255, 159, 64, 0.6))"
                  ></BarChart>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default EPSComparision;
