import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [popularTimesData, setPopularTimesData] = useState(null);
  const [location, setLocation] = useState({});
  const [trafficArray, setTrafficData] = useState({});

  const url = "http://127.0.0.1:8000/getPopularTimesData";

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    const requestData = {
      coordonates: "44.44552048018695, 26.0628307107671",
    };
    console.log(JSON.stringify(requestData));
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Specify JSON content type
        },
        body: JSON.stringify(requestData), // Stringify the data object
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const parsedData = await response.json();
      setPopularTimesData(parsedData);
      console.log(parsedData.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <>
      <div>
        {popularTimesData != null
          ? popularTimesData.data.map((element) => <h1>{element.name}</h1>)
          : "null"}
      </div>
    </>
  );
}

export default App;
