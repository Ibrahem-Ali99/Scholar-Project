import React from "react";
import Row1 from "./Row1.jsx";
import Row2 from "./Row2.jsx";
import Row3 from "./Row3.jsx";
import Button from "@mui/material/Button";
import { DownloadOutlined } from "@mui/icons-material";
import { Box, Stack, Typography, useTheme } from "@mui/material";
import DashHeader from "../../../components/DashHeader.jsx";

const Dashboard = () => {
  const theme = useTheme();
  return (
    <div>
<Stack direction={"row"} justifyContent={"space-between"} alignItems={"center"}>
        <DashHeader
          isDashboard={true}
          title={"DASHBOARD"}
          subTitle={"Welcome to your teachDashboard"}
        />
  
        <Box sx={{ textAlign: "right", mb: 1.3 }}>
          <Button
            sx={{ padding: "6px 8px", textTransform: "capitalize" }}
            variant="contained"
            color="primary"
          >
            <DownloadOutlined />
            Download Reports
          </Button>
        </Box>
</Stack>

      <Row1 />
      <Row2 />
      <Row3 />
    </div>
  );
};

export default Dashboard;
