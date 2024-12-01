import React from "react";
import { ThemeProvider, createTheme, styled } from "@mui/material/styles";
import { Box, CssBaseline } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import DashTopBar from "./components/DashTopBar.jsx";
import DashSideBar from "./components/DashSideBar.jsx";
import { getDesignTokens } from "./theme";
import Dashboard from "./pages/TeacherDashboard/teachDashboard/Dashboard";
import Course from "./pages/TeacherDashboard/course/Course";
import Students from "./pages/TeacherDashboard/students/Student";
import Calendar from "./pages/TeacherDashboard/calendar/Calendar";
import BarChart from "./pages/TeacherDashboard/barChart/BarChart";
import PieChart from "./pages/TeacherDashboard/pieChart/PieChart";
import LineChart from "./pages/TeacherDashboard/lineChart/LineChart";
import NotFound from "./pages/TeacherDashboard/notFound/NotFound";

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
}));

export default function DashApp() {
  const [open, setOpen] = React.useState(false);
  const [mode, setMode] = React.useState(localStorage.getItem("currentMode") || "light");
  const theme = React.useMemo(() => createTheme(getDesignTokens(mode)), [mode]);

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ display: "flex" }}>
        <CssBaseline />
        <DashTopBar open={open} handleDrawerOpen={() => setOpen(true)} setMode={setMode} />
        <DashSideBar open={open} handleDrawerClose={() => setOpen(false)} />
        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <DrawerHeader />
          <Routes>
            <Route index element={<Dashboard />} />
            <Route path="./pages/course" element={<Course />} />
            <Route path="./pages/students" element={<Students />} />
            <Route path="calendar" element={<Calendar />} />
            <Route path="bar" element={<BarChart />} />
            <Route path="pie" element={<PieChart />} />
            <Route path="line" element={<LineChart />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Box>
      </Box>
    </ThemeProvider>
  );
}