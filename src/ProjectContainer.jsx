import React from "react";
import ProjectCard from "./ProjectCard";

const ProjectContainer = ({ projects }) => {
  console.log(projects);
  function renderProjects(projects) {
    return projects.map((project) => (
      <ProjectCard
        key={project.id}
        name={project.name}
        description={project.description}
        client={project.client}
        active={project.active}
        colors={project.colors}
      />
    ));
  }
  return <>{renderProjects(projects)}</>;
};

export default ProjectContainer;
