import React, {useEffect, useState} from "react";
import {DataGrid} from "@mui/x-data-grid";
import {Box, Typography, useTheme} from "@mui/material";
import Header from "../../components/Header";

// Import data from the data file
import {courses, teachers} from "./data";

const Course = () => {
    const theme = useTheme();
    const [courseData, setCourseData] = useState([]);

    useEffect(() => {
        // Map over courses and add teacher names directly
        const courseRows = courses.map(course => {
            // Get the teacher's name from the teachers array based on teacher_id
            const teacher = teachers.find(teacher => teacher.teacher_id === course.teacher_id);
            return {
                id: course.course_id,
                course_name: course.course_name,
                teacher_name: teacher ? teacher.name : "Unknown",
                course_description: course.course_description,
            };
        });
        setCourseData(courseRows);
    }, []);

    // Define columns for DataGrid
    const columns = [
        {
            field: "id",
            headerName: "ID",
            width: 100,
            align: "center",
            headerAlign: "center",
        },
        {
            field: "course_name",
            headerName: "Course Name",
            flex: 1,
            align: "center",
            headerAlign: "center",
        },
        {
            field: "teacher_name",
            headerName: "Teacher",
            flex: 1,
            align: "center",
            headerAlign: "center",
            renderCell: ({value}) => {
                return (
                    <Typography sx={{fontSize: "13px", color: "#fff"}}>{value}</Typography>
                );
            },
        },
        {
            field: "course_description",
            headerName: "Description",
            flex: 2,
            align: "center",
            headerAlign: "center",
        },
    ];

    return (
        <Box>
            <Header title={"Courses"} subTitle={"Managing the Courses and Instructors"}/>

            <Box sx={{height: 600, mx: "auto"}}>
                <DataGrid
                    rows={courseData}
                    columns={columns}
                />
            </Box>
        </Box>
    );
};

export default Course;
