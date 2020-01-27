// ----------------------------------------------- Floating Button ----------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {toolbarEnabled: true});
});


// ----------------------------------------------- users posts ----------------------------------------------
// Start with first post.
counter = 0;
// Load posts 20 at a time.
quantity = 18;
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
    const end = start + quantity ;
    counter = end ;


    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/api/user/theuser');

    console.log(request)
    // For each set of data received, add a card
    request.onload = () => {
        const data = JSON.parse(request.response);
        data.forEach(add_post);

    };
    // Add start and end points to request data.
    const data = new FormData();
    data.append("start", start);
    data.append('quantity', quantity);

    console.log(start)
    // Send request.
    request.send(data);
};

// Add a new post with given contents to DOM.
function add_post(content) {

    // Create tr.
    const tr = document.createElement('tr');

    // Create td.
    const postid = document.createElement('td');
    postid.innerHTML = content.id;

    const fav = document.createElement('td');
    fav.innerHTML = content.aut_fav;

    const tittle = document.createElement('td');
    tittle.innerHTML = content.tittle;

    const autid = document.createElement('td');
    autid.innerHTML = content.author_id;

    const autname = document.createElement('td');
    autname.innerHTML = content.author_name;

    const pub = document.createElement('td');
    pub.innerHTML = content.published

    document.querySelector('tbody').append(tr);
    tr.appendChild(postid);
    tr.appendChild(fav);
    tr.appendChild(tittle);
    tr.appendChild(autid);
    tr.appendChild(autname);
    tr.appendChild(pub);

};
