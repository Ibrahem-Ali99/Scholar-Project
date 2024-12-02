import React from "react";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { Box, Typography } from "@mui/material";
import { columns, rows } from "./data.js";
import DashHeader from "../../../components/TeacherDashboard/DashHeader.jsx";

const Student = () => {
  return (
    <Box>
      <DashHeader
        title="Students"
        subTitle="List of Student for Future Reference"
      />

      <Box sx={{ height: 650, width: "99%", mx: "auto" }}>
        <DataGrid
          slots={{
            toolbar: GridToolbar,
          }}
          rows={rows}
          // @ts-ignore
          columns={columns}
        />
      </Box>
    </Box>
  );
};

export default Student;