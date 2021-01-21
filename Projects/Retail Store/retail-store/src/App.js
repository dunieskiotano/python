import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.scss";
import { HomeComponent } from "./Components/Home/HomeComponent";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route exact path="/home" component={HomeComponent} />
      </BrowserRouter>
    </div>
  );
}

export default App;
