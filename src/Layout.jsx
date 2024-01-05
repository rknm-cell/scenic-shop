import { Outlet } from "react-router-dom";
import { Routes, Route } from "react-router-dom";
import Home from "./Home";
import Users from "./Users";
import { Projects } from "./Projects";

const Layout = ({projects}) => {
  return (
    <>
       <Routes>
        <Route index element={<Home />} />
        <Route path="users" element={<Users />} />
        <Route path="projects" element={<Projects projects={projects} />} />
      </Routes>

      
    </>
  );
};

export default Layout;
