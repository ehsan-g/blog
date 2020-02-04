// Start with first post.
counter = 0;
// Load posts 20 at a time.
quantity = 6;
// let the window scroll function load


// When DOM loads, render the first 9 posts.
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 9 posts.
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
        }
};
// Load next set of posts.
function load() {

    // Set start and end post numbers, and update counter.
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;


    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/api/posts/all');

    // For each set of data received, add a card
    request.onload = () => {
        const data = JSON.parse(request.response);

        if (data["error"] !== "There are no posts"){
            data.forEach(add_post);
        }


    };
    // Add start and end points to request data.
    const data = new FormData();
    data.append("start", start);
    data.append('end', end);
    data.append('quantity', quantity);

    // Send request.
    request.send(data);
};

// Add a new post with given contents to DOM.
function add_post(content) {
    // Generate a random roll.

    var card = document.createElement('div');
    card.className = 'grid-item';

    var image = document.createElement('img');
        image.src = content.mainimg;

    document.querySelector('#posts').append(card);
    card.appendChild(image);



    const overlay = document. createElement('div');
    overlay.className = 'overlay';
    card.appendChild(overlay);

    const a = document .createElement("a");
    a.href = "posts/post/" + content.id;
    const a2 = document.createElement('a');
    a2.id = 'eye'
    a2.href = "posts/post/" + content.id;
    const overtxt = document.createElement('div');
    overtxt.className = 'text';
    overtxt.innerHTML = content.tittle;
    const icoon = document.createElement("i")
    icoon.className = "material-icons"
    icoon.innerText = 'remove_red_eye'


    overlay.appendChild(a);
    overlay.appendChild(a2)
    a.appendChild(overtxt)
    a2.appendChild(icoon)


;

    imageLoad();

};



