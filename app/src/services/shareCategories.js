import CONFIG from '../config';
import * as http from '../utils/http';

export async function fetch() {
  const { data } = await http.get(`${CONFIG.END_POINTS.shareCategory}`);

  return data;
}

const shareCategoryServices = {
  fetch,
};

export default shareCategoryServices;
