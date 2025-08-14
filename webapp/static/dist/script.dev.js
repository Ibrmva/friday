"use strict";

document.getElementById("message-form").onsubmit = function (e) {
  e.preventDefault();
  var formData = new FormData(this);
  fetch("/send", {
    method: "POST",
    body: formData
  }).then(function (res) {
    return res.json();
  }).then(function () {
    return location.reload();
  });
};
//# sourceMappingURL=script.dev.js.map
