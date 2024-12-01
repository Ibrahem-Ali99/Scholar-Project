import { Box, useTheme } from "@mui/material";
import React from "react";
import { ResponsiveLine } from "@nivo/line";
import Line from "./Line.jsx";
import DashHeader from "../../../components/DashHeader.jsx";

const LineChart = () => {
  const theme = useTheme();
  return (
    <Box>
      <DashHeader title="Line Chart" subTitle="Simple Line Chart" />

      <Line />
    </Box>
  );
};

export default LineChart;
