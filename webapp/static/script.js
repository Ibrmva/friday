document.getElementById("message-form").onsubmit = function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch("/send", { method: "POST", body: formData })
        .then(res => res.json())
        .then(() => location.reload());
};
