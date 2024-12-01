import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import App from "./DashApp";
import Dashboard from "./pages/TeacherDashboard/teachDashboard/Dashboard";
import Team from "./pages/team/Team";
import Contacts from "./pages/contacts/Contacts";
import Calendar from "./pages/TeacherDashboard/calendar/Calendar";
import BarChart from "./pages/TeacherDashboard/barChart/BarChart";
import PieChart from "./pages/TeacherDashboard/pieChart/PieChart";
import LineChart from "./pages/TeacherDashboard/lineChart/LineChart";
import NotFound from "./pages/TeacherDashboard/notFound/NotFound";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<App />}>
      <Route index element={<Dashboard />} />
      <Route path="./pages/team" element={<Team />} />
      <Route path="./pages/contacts" element={<Contacts />} />
      <Route path="./pages/calendar" element={<Calendar />} />
      <Route path="./pages/bar" element={<BarChart />} />
      <Route path="./pages/pie" element={<PieChart />} />
      <Route path="./pages/line" element={<LineChart />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);