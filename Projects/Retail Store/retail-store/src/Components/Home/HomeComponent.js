import React from "react";

import { BrowserRouter } from "react-router-dom";
import { Modal, Button } from "react-bootstrap";
import {
  FaUser,
  FaGit,
  FaYoutube,
  FaTwitter,
  FaFacebook,
  FaInstagram
} from "react-icons/fa";
import { Container, Row, Col } from "reactstrap";
import shopping from "../../assets/shopping.jpg";

export class HomeComponent extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    let style = {
      marginTop: "500px",
      position: "absolute"
    };
    return (
      <>
        <div className="nav">
          <div className="nav-section">
            <ul className="nav-links">
              <li>
                <a href="/home" className="links">
                  Home
                </a>
              </li>
              <li>
                <a href="/women" className="links">
                  Women
                </a>
              </li>
              <li>
                <a href="/men" className="links">
                  Men
                </a>
              </li>
              <li>
                <a href="/accessories" className="links">
                  Accessories
                </a>
              </li>
              <li>
                <a href="/contact" className="links">
                  Contact Us
                </a>
              </li>
              <li>
                <a href="/login" id="login-link" className="links">
                  <FaUser /> Login
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="container">
          <img src={shopping} alt="shopping" className="image-center"></img>
          <div className="center-text">
            <span className="heading">Welcome to Paradise Stores</span>
            <br />
            <span className="subheading">
              When buying becomes an unforgettable experience
            </span>
          </div>
          <footer>
            <span>© 2020 Paradise Stores. All Rights Reserved</span>Hi
            <br />
            <span>
              <FaYoutube /> <FaTwitter /> <FaFacebook /> <FaInstagram />
            </span>
          </footer>
        </div>
      </>
    );
  }
}
