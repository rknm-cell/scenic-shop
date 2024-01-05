import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ProjectsContext } from './ProjectsContext'; // Import the context
import Home from './Home';
import Projects from './Projects';
import NoPage from './NoPage';

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  

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

  function ProjectsWrapper({ projects }) {
    return <Projects projects={projects} />;
  }
  
  return (
    <>
    <ProjectsContext.Provider value={{ projects, setProjects, loading }}>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects/*" element={<Projects />} />
          <Route path="*" element={<NoPage />} />
        </Routes>
      </Router>
    </ProjectsContext.Provider>
    </>
  );
}

export default App;
