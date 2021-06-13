import CONFIG from '../config';
import * as http from '../utils/http';

export const fetchDailyData = async (category) => {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/daily?category=${category}`
  );
  return data;
};

export async function fetchWeeklyData(shareSymbol, name) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/w?shareSymbol=${shareSymbol}&shareName=${name}`
  );

  return data;
}

export async function fetchMonthlyData(shareSymbol, name) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/m?shareSymbol=${shareSymbol}&shareName=${name}`
  );

  return data;
}

export async function fetchQuaterData(shareSymbol, name) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/q?shareSymbol=${shareSymbol}&shareName=${name}`
  );

  return data;
}

export async function fetchYearlyData(shareSymbol, name) {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/y?shareSymbol=${shareSymbol}&shareName=${name}`
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
