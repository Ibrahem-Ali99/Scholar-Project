import React from "react";
import {Stack} from "@mui/material";
import Card from "./card.jsx";
import SchoolIcon from '@mui/icons-material/School';
import AttachMoneyIcon from "@mui/icons-material/AttachMoney";
import PendingIcon from '@mui/icons-material/Pending';
import AssignmentTurnedInIcon from '@mui/icons-material/AssignmentTurnedIn';
import {data1, data2, data3, data4} from "./data.js";

const Row1 = () => {
    return (
        
        <Stack
            direction="row"
            flexWrap="wrap"
            gap={2}
            justifyContent="space-between"
        >
            {/* card for Students */}
            <Card
                icon={<SchoolIcon style={{fontSize: 35, color: "blue"}}/>}
                title="00,000"
                subTitle="Students enrolled"
                data={data1}
                scheme="nivo"
            />

            <Card
                icon={<AttachMoneyIcon style={{fontSize: 35, color: "green"}}/>}
                title="000,000"
                subTitle="Moeny obtained"
                data={data2}
                scheme="category10"
            />

            {/* card for New Clients */}
            <Card
                icon={<AssignmentTurnedInIcon style={{fontSize: 35, color: "purple"}}/>}
                title="00"
                subTitle="Completion Rate"
                data={data3}
                scheme="accent"
            />

            <Card
                icon={<PendingIcon style={{fontSize: 35, color: "orange"}}/>}
                title="65"
                subTitle="Pending Due"
                data={data4}
                scheme="dark2"
            />
        </Stack>
    );
};

export default Row1;
