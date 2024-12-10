import React, { useEffect, useState } from "react";
import { Stack } from "@mui/material";
import Card from "./card.jsx";
import SchoolIcon from '@mui/icons-material/School';
import AttachMoneyIcon from "@mui/icons-material/AttachMoney";
import PendingIcon from '@mui/icons-material/Pending';
import AssignmentTurnedInIcon from '@mui/icons-material/AssignmentTurnedIn';
import { data1 as defaultData1, data2, data3, data4 } from "./data.js";

const Row1 = () => {
    const [studentCount, setStudentCount] = useState("0");
    const [moneyObtained, setMoneyObtained] = useState("0.00");
    const [chartData, setChartData] = useState(defaultData1);

    useEffect(() => {
        const teacherId = localStorage.getItem('teacher_id');
        if (teacherId) {
            // fetch Students Enrolled
            fetch(`http://127.0.0.1:5000/dashboard/students-enrolled?teacher_id=${teacherId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.title) {
                        setStudentCount(data.title);
                        setChartData([
                            { id: 'Enrolled', label: 'Enrolled', value: parseInt(data.title.replace(/,/g, '')), color: "hsl(111, 90%, 90%)" },
                            { id: 'Others', label: 'Others', value: 100 - parseInt(data.title.replace(/,/g, '')), color: "hsl(22, 90%, 90%)" },
                        ]);
                    }
                });

            // fetch Money Obtained
            fetch(`http://127.0.0.1:5000/dashboard/money-obtained?teacher_id=${teacherId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.title) {
                        setMoneyObtained(data.title);
                    }
                });
        }
    }, []);

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
                title={studentCount}
                subTitle="Students enrolled"
                data={chartData}
                scheme="nivo"
            />

            {/* card for Money obtained */}
            <Card
                icon={<AttachMoneyIcon style={{fontSize: 35, color: "green"}}/>}
                title={moneyObtained}
                subTitle="Money obtained"
                data={data2}
                scheme="category10"
            />

            {/* Other cards remain unchanged */}
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