import { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Home from "./Home";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);
  const [projects, setProjects] = useState([]);

  useEffect(()=> {
    fetch("/projects")
    .then(response => response.json())
    .then(data => setProjects(data))
  }, [])

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
            <Projects />
          </Route>
        </div>
      </Router>
    </>
  );
}

export default App;
