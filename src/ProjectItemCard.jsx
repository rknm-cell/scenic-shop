import React from 'react'

const ProjectItemCard = ({project}) => {
  return (
    <>
    <h1>{project.name}</h1>
    <p>{project.description}</p>
    <p>{project.colors}</p>{}
    </>
  )
}

export default ProjectItemCard