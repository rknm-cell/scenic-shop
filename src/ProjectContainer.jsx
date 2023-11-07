import React from 'react'
import ProjectCard from './ProjectCard'

const ProjectContainer = ({projects}) => {

  function renderProjects(projects){
    return (
      projects.map((project) => 
      <ProjectCard key={project.id} name={project.name} description={project.description} client={project.client} />)

    )
  }
  return (
    <>{renderProjects()}</>
  )
}

export default ProjectContainer