import React from "react";
import PropTypes from "prop-types";
// import { Link } from "react-router-dom";
// import { a } from "react-router-dom/cjs/react-router-dom.min";

export default function Navbar(props) {
  return (
    <nav
      className={`navbar navbar-expand-lg navbar-${props.bh} bg-${props.bh}`}
    >
      <div className="container-fluid">
        <a className="navbar-brand" href="/">
          <strong>
            {props.title} Navbar {props.abtxt}
          </strong>
        </a>
        {/* <Link className="navbar-brand" to="/">
          <strong>
            {props.title} Navbar {props.abtxt}
          </strong>
        </Link> */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link active" aria-current="page" href="/home">
                Home
              </a>
            </li>
            {/* <li className="nav-item">
              <Link className="nav-link active" aria-current="page" to="/home">
                Home
              </Link>
            </li> */}
            <li className="nav-item">
              <a className="nav-link" href="/about">
                About
              </a>
            </li>
            {/* <li className="nav-item">
              <Link className="nav-link" to={}="/about">
                About
              </Link>
            </li> */}
          </ul>
        </div>

        <div className="form-check form-switch ">
          <input
            className="form-check-input"
            type="checkbox"
            role="switch"
            id="flexSwitchCheckDefault"
            onClick={props.togglemode}
          />
        </div>
      </div>
    </nav>
  );
}

Navbar.propTypes = { title: PropTypes.string, abtxt: PropTypes.string };

Navbar.defaultProps = {
  title: "this is the",
  abtxt: "this is abtext",
};
