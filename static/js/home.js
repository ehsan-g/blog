// Start with first post.
counter = 0;
// Load posts 20 at a time.
quantity = 5;
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
    console.log(request);
    request.open('POST', '/api/users/12');

    // For each set of data received, add a card
    request.onload = () => {
        const data = JSON.parse(request.response);
        data.forEach(add_post);

    };
    // Add start and end points to request data.
    const data = new FormData();
    data.append("start", start);
    console.log(start ,end, data);
    data.append('end', end);

    // Send request.
    request.send(data);
};

// Add a new post with given contents to DOM.
function add_post(content) {
    // Create first Div.
    const card = document.createElement('div');
    card.className = 'col s4 z-depth-2 card post';
    // card.innerHTML = contents;
    const imageContainer = document.createElement('div');
    imageContainer.className = 'card-image waves-effect waves-block waves-light';

    const image = document.createElement('img');
    image.className = 'activator';
    image.src = "static/img/office.jpg";

    // Create Second Div.
    const cardContent = document.createElement('div');
    cardContent.className = 'card-content';

    const theSpan = document.createElement("span");
    theSpan.className = 'card-title activator grey-text text-darken-4';
    const theI = document.createElement("i");
    theI.className = 'material-icons right';
    const spanText = document.createTextNode(content.title);
    const iText = document.createTextNode('more_vert');

    const theP = document.createElement('p');
    const theA = document.createElement('a');
    theA.href = '#';
    const aText = document.createTextNode('Link');

    // Create Third Div.
    const cardReveal = document.createElement("div");
    cardReveal.className = 'card-reveal';

    const theSpan2 = document.createElement("span");
    theSpan2.className = 'card-title grey-text text-darken-4';
    const theI2 = document.createElement("i");
    theI2.className = 'material-icons right';
    const spanText2 = document.createTextNode('Card Title');
    const iText2 = document.createTextNode('close');
    const theP2 = document.createElement('p');
    const pText = document.createTextNode('Here is some more information about this product that is only revealed once clicked on.');



    document.querySelector('#posts').append(card);
    card.appendChild(imageContainer);
    imageContainer.appendChild(image);

    card.appendChild(cardContent);
    cardContent.appendChild(theSpan);
    cardContent.appendChild(theP);

    theSpan.appendChild(theI);
    theI.appendChild(iText);
    theP.appendChild(theA);
    theSpan.appendChild(spanText);
    theA.appendChild(aText);

    card.appendChild(cardReveal);
    cardReveal.appendChild(theSpan2);
    cardReveal.appendChild(theP2);

    theSpan2.appendChild(theI2);
    theI2.appendChild(iText2);
    theSpan2.appendChild(spanText2);
    theP2.appendChild(pText)


};


