// Generate HTML using double data
function generateHTML(data) {
    let container = document.querySelector(".container");
    container.innerHTML = ''

    let htmlData =
        '<div class="content">' +
        '<p class="title">Did The Rockies Get a Double Yesterday?</p>' +
        '<div class="line"></div>' +
        `<p class="answer">${data.answer}</p>` +
        `<p class="details">${data.details}</p>` +
        '<div class="line"></div>' +
        `<p class="moreDetails">${data.moreDetails}</p>` +
        "</div>" +
        "<footer>" +
        '<p class="footer-message">' +
        "This website was built for fun and is an " +
        '<a target="_blank" href="https://github.com/jfinley6/did-the-rockies-get-a-double-yesterday"' +
        ">Open Source Project</a>" +
        "</p>" +
        '<p class="footer-message">' +
        "Created and maintained by  " +
        '<a target="_blank" href="https://www.linkedin.com/in/john-tyler-finley/"' +
        ">John Finley</a>" +
        "</p>" +
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
        yesterdays_date: data.yesterdays_date,
        last_rockie_game_date: data.last_rockie_game_date
    };
    localStorage.setItem("doubleData", JSON.stringify(localStorageObject));
}

// If current day double results already exist then just use localstorage, otherwise fetch from server
function checkLocalStorage() {
    const storedUserData = JSON.parse(localStorage.getItem("doubleData"));
    const currentDate = new Date().toLocaleDateString();
    if (storedUserData !== null && storedUserData.dateAccessed === currentDate) {
        return Promise.resolve(storedUserData);
    } else {
        return fetch("/_internal/get_double_data",
        {
            headers: {
                'Accept': 'application/json'
            }
        })
            .then((response) => response.json())
            .then((data) => {
                saveToLocalStorage(data);
                return data;
            })
            .catch((error) => {
                console.log(error);
            });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    checkLocalStorage().then((userData) => {
        generateHTML(userData);
    });
});
