import CONFIG from '../config';
import * as http from '../utils/http';

export const fetchDailyData = async (category) => {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/daily?category=${category}`
  );
  return data;
};

export async function fetchWeeklyData(category) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/weekly?category=${category}`
  );

  return data;
}

export async function fetchMonthlyData(category) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/monthly?category=${category}`
  );
  return data;
}

export async function fetchQuaterData(category) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/quaterly?category=${category}`
  );
  return data;
}

export async function fetchYearlyData(category) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/yearly?category=${category}`
  );
  return data;
}

const shareServices = {
  fetchDailyData,
  fetchWeeklyData,
  fetchMonthlyData,
  fetchQuaterData,
  fetchYearlyData,
};

export default shareServices;
