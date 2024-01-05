import React, { useContext } from 'react';
import ProjectContainer from './ProjectContainer';
import { ProjectsContext } from './ProjectsContext';

const Projects = () => {
  const { projects, loading } = useContext(ProjectsContext); // Access projects from the context

  console.log(projects); // Log projects to the console
  if (loading) {
    return <div>Loading...</div>; // Render a loading message or a spinner
  }
  return (
    <ProjectContainer projects={projects} />
  );
}

export default Projects;