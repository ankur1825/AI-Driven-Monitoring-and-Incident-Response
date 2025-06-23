import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,  //`${window.location.origin}/pipeline/api`;
  withCredentials: false,
});

export default api;