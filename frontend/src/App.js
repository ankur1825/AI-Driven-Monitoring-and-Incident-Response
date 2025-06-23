import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import AlertsTable from './components/AlertsTable';
import RCAViewer from './components/RCAViewer';
import IncidentsPage from './components/IncidentsPage';
import MetricsDashboard from './components/MetricsDashboard';
import './App.css';

function App() {
  return (
    <Router basename="/ai-driven-monitoring">
      <div className="App">
        <h1>HorizonWatch Dashboard</h1>
        <nav>
          <Link to="/">Forecast</Link> | <Link to="/alerts">Alerts</Link> | <Link to="/incidents">Incidents</Link> | <Link to="/metrics">Metrics</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/alerts" element={<AlertsTable />} />
          <Route path="/incidents" element={<IncidentsPage />} />
          <Route path="/metrics" element={<MetricsDashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
