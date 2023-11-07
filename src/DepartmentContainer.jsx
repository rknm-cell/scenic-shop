import React from "react";
import DepartmentCard from "./DepartmentCard";

const Department = ({departments}) => {

  function handleDeptRender(){
    return (
      departments.map((department) => {<DepartmentCard key={department.id} name={department.name} description={department.description} />})
    )
  }
  return (
    <>
      <h1>Departments</h1>
      {handleDeptRender()}
    </>
  );
};

export default Department;
