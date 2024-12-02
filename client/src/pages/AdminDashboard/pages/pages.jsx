import DashboardHome from './DashboardHome'
import CourseList from './CourseList'

const pages = [
  {
    path: "",
    page: <DashboardHome />,
    buttonText: "Home",
    buttonIcon: <></>,
  },
  {
    path: "/teacher",
    page: <></>,
    buttonText: "Teacher Approval",
    buttonIcon: <></>,
  },
  {
    path: "/course",
    page: <CourseList/>,
    buttonText: "Course Performance",
    buttonIcon: <></>,
  },
  {
    path: "/payment",
    page: <></>,
    buttonText: "Payment Management",
    buttonIcon: <></>,
  },
]

export default pages