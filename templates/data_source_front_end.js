"use strict";

let formElem = null;
let endPointSource = null;

if (document.URL.includes("data_frame")) {
    formElem = document.getElementById("formElementDataFrame");
    endPointSource = "data_frame";
} else if (document.URL.includes("database")) {
    formElem = document.getElementById("formElementDatabase");
    endPointSource = "database";
} else {
    formElem = document.getElementById("formElementGoogleDrive");
    endPointSource = "drive";
}

formElem.removeAttribute("hidden")

formElem.onsubmit = async (e) => {
    e.preventDefault();

    await fetch('/post_' + endPointSource, {
      method: 'POST',
      body: new FormData(formElem)
    });
};