import { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Home from "./Home";
import "./App.css";
import { Projects } from "./Projects";

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Define the URL of the API endpoint where your projects are hosted.
    const apiUrl = 'https://api.example.com/projects'; // Replace with your API endpoint URL.

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setProjects(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  return (
    
    <>
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
                <Link to="/projects">Projects</Link>
                <Link to="/clients">Clients</Link>
              </li>
            </ul>
          </nav>

          <Route path="/">
            <Home />
          </Route>
          <Route path="/projects">
            <Projects projects={projects}/>
          </Route>
        </div>
      </Router>
    </>
  );
}

export default App;
