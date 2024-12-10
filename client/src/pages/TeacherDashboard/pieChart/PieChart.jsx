import React from "react";
import { ResponsivePie } from "@nivo/pie";
import { Box, useTheme } from "@mui/material";
import Pie from "./pie.jsx";
import DashHeader from "../../../components/TeacherDashboard/DashHeader.jsx";

const PieChart = () => {
  const theme = useTheme();
  return (
    <Box>
      <DashHeader title="Pie Chart" subTitle="Simple Pie Chart" />

      <Pie />
    </Box>
  );
};

export default PieChart;
