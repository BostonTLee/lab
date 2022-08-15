import './App.css';

//import useFetch from "react-fetch-hook"
import { useState, useEffect } from "react";



// const fetchData = () => {
//     return fetch("http://127.0.0.1:5000/test-data?id=2")
//           .then((response) => response.json())
//           .then((data) => console.log(data));}

function App() {
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
useEffect(() => {
    fetch('http://127.0.0.1:5000/test-data?id=2')
      .then((response) => {
        setData(response);
        setError(null);
      })
      .then((actualData) => {
        setData(actualData);
        setError(null);
      })
      .catch((err) => {
        setError(err.message);
        setData(null);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>API Posts</h1>
      {loading && <div>A moment please...</div>}
      {error && (
        <div>{`There is a problem fetching the post data - ${error}`}</div>
      )}
	  {data && <div>hmm...</div>}
    Test
    </div>
  );
}

export default App;
