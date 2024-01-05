import React from 'react'

const ProjectCard = ({name, description, client}) => {
  console.log(name, description, client)
  return (
    <>
    <h1>{name}</h1>
    <p>{description}</p>
    <p>{client}</p>
    </>
  )
}

export default ProjectCard