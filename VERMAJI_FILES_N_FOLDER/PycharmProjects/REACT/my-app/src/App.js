// import logo from "./logo.svg";
import "./App.css";
import React from "react";
import Navbar from "./components/Navbar";
import Textform from "./components/Textform";
// import About from "./components/About";
import Alert from "./components/Alert";
import { useState } from "react";
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  const [mode, setmode] = useState("light"); // tells whether dark mode is enabled or not
  const [alert, setalert] = useState(null);

  let showalert = (message, type) => {
    setalert({
      msg: message,
      type: type,
    });
    setTimeout(() => {
      setalert(null);
    }, 1500);
  };

  let setothermode = () => {
    if (mode === "dark") {
      setmode("light");
      document.body.style.backgroundColor = "white";
      document.body.style.color = "black";
      showalert(" Light mode has been enabled", "success");
    } else {
      setmode("dark");
      document.body.style.backgroundColor = "rgb(0 0 0   / 99%)";
      document.body.style.color = "white";
      showalert(" Dark mode has been enabled", "success");
    }
  };

  return (
    <>
      {/* <Router> */}
        <Navbar abtxt="over here" bh={mode} togglemode={setothermode} />
        <Alert alert={alert} />
        <div className="container my-3">
          {/* <Switch> */}
            {/* <Route exact path="/about"> */}
              {/* <About /> */}
            {/* </Route> */}

            {/* <Route exact path="/"> */}
              <Textform
                showalert={showalert}
                heading="TRY TEXT-UTILS -WORD COUNTER, CHARACTER COUNTER
                "
              />
            {/* </Route> */}

            {/* <Route exact path="/home"> */}
              <Textform
                showalert={showalert}
                heading="TRY TEXT-UTILS -WORD COUNTER, CHARACTER COUNTER
                "
              />
            {/* </Route> */}
          {/* </Switch> */}
        </div>
      {/* </Router> */}
    </>
  );
}

export default App;
