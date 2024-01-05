import React, {createContext, useContext, useEffect, useState} from 'react'

const ProjectsContext = createContext();

const ProjectsProvider = ({children}) => {
    const [projects, setProjects] = useState([]);
    useEffect(() => {
        // Define the URL of the API endpoint where your projects are hosted.
        const apiUrl = "http://localhost:3000/projects"; // Replace with your API endpoint URL.
    
        fetch(apiUrl)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            setProjects(data);
            console.log(data);
            setLoading(false);
          })
          .catch((error) => {
            console.error("Error fetching data:", error);
            setLoading(false);
          });
      }, []);
    return (
        <ProjectsContext.Provider value={{projects, setProjects}}>
            {children}
        </ProjectsContext.Provider>
        )
}
export {ProjectsContext};
export default ProjectsProvider;