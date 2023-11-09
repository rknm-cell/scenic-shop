import React from 'react'
import ProjectCard from './ProjectCard'
import ProjectContainer from './ProjectContainer'

const ClientCard = ({projects}) => {


  function handleClientProjects(){
    return (
      projects.map((project) => {
        <ProjectContainer project={project}/>
      })
    )
  }
  return (
    <><h1>{client.name}</h1>
    <p>{client.description} </p>
    
    </>
  )
}

export default ClientCard