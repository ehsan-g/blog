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
    const randm = Math.floor((Math.random() * 3) + 1);

    if ( randm === 1){
        var card = document.createElement('div');
        card.className = 'grid-item';

        var image = document.createElement('img');
        image.src = "static/img/golden-hour.png";
    }

    else if ( randm === 2){
        var card = document.createElement('div');
        card.className = 'grid-item';

        var image = document.createElement('img');
        image.src = "static/img/office.png";


    }
    // Create first Div.
    else {
        var card = document.createElement('div');
        card.className = 'grid-item';

        var image = document.createElement('img');
        image.src = "static/img/look-out.jpg";


    }

    document.querySelector('#posts').append(card);
    card.appendChild(image);



    const overlay = document. createElement('div');
    overlay.className = 'overlay';
    card.appendChild(overlay);

    const overtxt = document.createElement('div');
    overtxt.className = 'text';
    overtxt.innerHTML = content.tittle;
    overlay.appendChild(overtxt)


;

    imageload();

};



