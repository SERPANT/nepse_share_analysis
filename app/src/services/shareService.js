import CONFIG from '../config';
import * as http from '../utils/http';

export const fetchDailyData = async (shareSymbol, name) => {
  const { data } = await http.get(
    `${CONFIG.END_POINTS.shareinfo}/d?shareSymbol=${shareSymbol}&shareName=${name}`
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
