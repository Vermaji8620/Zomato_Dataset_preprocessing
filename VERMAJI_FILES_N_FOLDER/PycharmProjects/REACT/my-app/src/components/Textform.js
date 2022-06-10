import React, { useState } from "react";

export default function Textform(props) {
  let handleupclick = () => {
    setText(text.toUpperCase());
    props.showalert("converted to uppercase", "success");
  };
  let handledownclick = () => {
    setText(text.toLowerCase());
    props.showalert("converted to lowercase", "success");
  };
  let clearall = () => {
    setText("");
    props.showalert("cleared all", "success");
  };
  let copyall = () => {
    let text = document.querySelector(".mybox");
    text.select();
    text.setSelectionRange(0, 999);
    navigator.clipboard.writeText(text.value);
    props.showalert("copied to clipboard", "success");
  };
  let clearspace = () => {
    let newtext = text.split(/[ ]+/);
    setText(newtext.join(" "));
    props.showalert("Extra spaces removed", "success");
  };
  let handleonchange = (event) => {
    setText(event.target.value);
  };

  let longword = () => {
    var textsplit = text.split(" ");
    var longestwordlength = 0;
    let longest = "";
    for (let i = 0; i < textsplit.length; i++) {
      if (textsplit[i].length > longestwordlength) {
        longestwordlength = textsplit[i].length;
        longest = textsplit[i];
      }
    }
    document.querySelector(
      "#longing"
    ).innerHTML = `the length of the longest word is ${longestwordlength} and the word is ${longest}`;
  };

  const [text, setText] = useState("");
  return (
    <>
      <div className="container">
        <div className="form-floating">
          <h2 className="my-4"> {props.heading}</h2>
          <textarea
            className="form-control mybox"
            value={text}
            onChange={handleonchange}
            style={{ height: "15rem" }}
            id="floatingTextarea"
          ></textarea>
        </div>
        <br />
        <div>
          <button className="btn btn-primary" onClick={handleupclick}>
            CONVERT TO UPPERCASE
          </button>
          <button className="btn btn-primary mx-2" onClick={handledownclick}>
            convert to lowercase
          </button>
          <button className="btn btn-primary mx-2" onClick={longword}>
            Longest word length
          </button>
          <button className="btn btn-primary mx-2" onClick={clearall}>
            clear all
          </button>
          <button className="btn btn-primary mx-2" onClick={copyall}>
            copy all
          </button>
          <button className="btn btn-primary mx-2" onClick={clearspace}>
            clear extra spaces
          </button>
        </div>
      </div>
      <div className="container my-5">
        <h1>YOUR TEXT SUMMARY</h1>
        <p>
          {
            text.split(" ").filter((element) => {
              return element.length != 0;
            }).length
          }{" "}
          words and {text.length} characters
        </p>
        <p>can be read in {0.008 * text.split(" ").length} time</p>
        <div id="longing"></div>
        <div id="shorting"></div>
        <h3>PREVIEW</h3>
        <p>
          {text.length > 0
            ? text
            : "NOTHING TO PREVIEW"}
        </p>
      </div>
    </>
  );
}
