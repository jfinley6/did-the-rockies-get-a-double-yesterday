// Generate HTML using double data
function generateHTML(data) {
    let container = document.querySelector(".container");

    let htmlData =
        '<div class="content">' +
        "<h1>Did The Rockies Get a Double Yesterday?</h1>" +
        '<div class="double-answer">' +
        `${data.answer}` +
        `<h2>${data.details}</h2>` +
        "</div>" +
        `<h2>${data.moreDetails}</h2>` +
        "</div>" +
        "<footer>" +
        "<h4>" +
        "This website was built for fun and is an " +
        '<a target="_blank" href="https://github.com/jfinley6/did-the-rockies-get-a-double-yesterday"' +
        ">Open Source Project</a>" +
        "</h4>" +
        "<h4>" +
        "Created and maintained by " +
        '<a target="_blank" href="https://www.linkedin.com/in/john-tyler-finley/">John Finley</a>' +
        "</h4>" +
        "</footer>";

    container.innerHTML += htmlData;
    return;
}

// Fetch the previous day double result
async function fetchDoubleData() {
    const response = await fetch("/_internal/get_double_data");
    return response;
}

function saveToLocalStorage(data) {
    const localStorageObject = {
        answer: data.answer,
        details: data.details,
        moreDetails: data.moreDetails,
        dateAccessed: new Date().toLocaleDateString(),
    };
    localStorage.setItem("doubleData", JSON.stringify(localStorageObject));
}

// If current day double results already exist then just use localstorage, otherwise fetch from server
function checkLocalStorage() {
    const storedUserData = JSON.parse(localStorage.getItem("doubleData"));
    const currentDate = new Date().toLocaleDateString()
    if (storedUserData !== null && storedUserData.dateAccessed === currentDate) {
        return Promise.resolve(storedUserData);
    } else {
        return fetch("/_internal/get_double_data")
            .then((response) => response.json())
            .then((data) => {
                saveToLocalStorage(data)
                return data;
            })
            .catch((error) => {
                console.log(error)
            })
    }
}

document.addEventListener("DOMContentLoaded", function () {
    checkLocalStorage().then((userData) => {
        generateHTML(userData)
    })
});
