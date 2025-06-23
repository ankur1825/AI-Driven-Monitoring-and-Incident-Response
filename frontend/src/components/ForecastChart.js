import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';

const ForecastChart = ({ data }) => (
  <ResponsiveContainer width="100%" height={300}>
    <LineChart data={data}>
      <XAxis dataKey="ds" />
      <YAxis />
      <Tooltip />
      <CartesianGrid strokeDasharray="3 3" />
      <Line type="monotone" dataKey="yhat" stroke="#8884d8" />
    </LineChart>
  </ResponsiveContainer>
);

export default ForecastChart;