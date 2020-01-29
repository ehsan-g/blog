// When DOM loads
document.addEventListener('DOMContentLoaded', load);

// Load next set of posts.
function load() {

    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/posts/categories/add');

    // For each set of data received, add a card
    request.onload = () => {
        const data = JSON.parse(request.response);
        console.log('hi')

        if (data["error"] !== "There are no categories"){
            data.forEach(add_post);
        }

    };
};

// Add a new post with given contents to DOM.
function add_post(content) {

    // Create tr.
    const tr = document.createElement('tr');

    // Create td.
    const catid = document.createElement('td');
    catid.innerHTML = content.id;

    const catname = document.createElement('td');
    catname.innerHTML = content.name;


    document.querySelector('tbody').append(tr);
    tr.appendChild(catid);
    tr.appendChild(catname);
};

