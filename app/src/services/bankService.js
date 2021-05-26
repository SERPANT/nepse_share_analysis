import CONFIG from '../config';
import * as http from '../utils/http';

export const fetchBankDayData = async () => {
  const { data } = await http.get(`${CONFIG.END_POINTS.commercialBank}/daily`);
  return data;
};

export async function fetchBankWeeklyData() {
  const { data } = await http.get(`${CONFIG.END_POINTS.commercialBank}/weekly`);

  return data;
}

export async function fetchBankMontlyData() {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.commercialBank}/monthly`
  );
  return data;
}

export async function fetchBankQuaterData() {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.commercialBank}/quaterly`
  );
  return data;
}

export async function fetchBankYearlyData() {
  const { data } = await http.get(`${CONFIG.END_POINTS.commercialBank}/yearly`);
  return data;
}

const bankServices = {
  fetchBankDayData,
  fetchBankWeeklyData,
  fetchBankMontlyData,
  fetchBankQuaterData,
  fetchBankYearlyData,
};

export default bankServices;
