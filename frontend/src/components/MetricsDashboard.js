import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

const MetricsDashboard = () => {
  const [cpu, setCpu] = useState([]);
  const [memory, setMemory] = useState([]);
  const [latency, setLatency] = useState([]);

  useEffect(() => {
    api.get('/api/metrics/cpu').then(res => setCpu(res.data));
    api.get('/api/metrics/memory').then(res => setMemory(res.data));
    api.get('/api/metrics/latency').then(res => setLatency(res.data));
  }, []);

  return (
    <div>
      <h2>CPU Usage</h2>
      <LineChart width={800} height={200} data={cpu}>
        <XAxis dataKey="ds" /><YAxis /><Tooltip /><CartesianGrid />
        <Line type="monotone" dataKey="y" stroke="#8884d8" />
      </LineChart>

      <h2>Memory Usage</h2>
      <LineChart width={800} height={200} data={memory}>
        <XAxis dataKey="ds" /><YAxis /><Tooltip /><CartesianGrid />
        <Line type="monotone" dataKey="y" stroke="#82ca9d" />
      </LineChart>

      <h2>Latency</h2>
      <LineChart width={800} height={200} data={latency}>
        <XAxis dataKey="ds" /><YAxis /><Tooltip /><CartesianGrid />
        <Line type="monotone" dataKey="y" stroke="#ff7300" />
      </LineChart>
    </div>
  );
};

export default MetricsDashboard;