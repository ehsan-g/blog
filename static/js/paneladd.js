// ----------------------------------------------- Floating Button ----------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {toolbarEnabled: true});


// ----------------------------------------------- Receive Categories ----------------------------------------------


// ----------------------------------------------- Char Counter ----------------------------------------------

// for text counts in insert feild

$('input, textarea').characterCounter();



// ----------------------------------------------- Tags # ----------------------------------------------
$('.chips').chips();
$('.chips-placeholder').chips({
    placeholder: 'هشتگ ‌ها',
    secondaryPlaceholder: ' دیگه چی؟ ',
    onChipAdd: function (e, data) { console.log("test") },

});


//  remove image .
var reset = document.querySelector('#rst');
// When button is clicked, remove post.
reset.onclick = function() {
    document.getElementById('img1').src='';
    document.getElementById('img2').src='';
    document.getElementById('img3').src='';
    document.getElementById('img4').src='';
    document.getElementById('img5').src='';
    document.getElementById('img6').src='';

    var input = $("#multi");
    input.replaceWith(input.val('').clone(true));



};

// ----------------------------------------------- Users Posts ----------------------------------------------
// Start with first post.
counter = 0;
// Load posts 20 at a time.
quantity = 18;
// let the window scroll function load


// When DOM loads, render the first 9 posts.
load()

// If scrolled to bottom, load the next 9 posts.
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();

    }
};

// Load next set of posts.
function load() {
    console.log("ff")
    // Set start and end post numbers, and update counter.
    var start = counter;
    const end = start + quantity - 1;
    counter = end + 1 ;


    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/myposts');
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
});


// ----------------------------------------------- Send Posts ----------------------------------------------



function sendform() {

    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/add_post');

    // Add start and end points to request data.
    const data = new FormData();
    data.append("theselect", theselect);
    data.append("duration", duration);
    data.append("aut_fav", aut_fav);
    data.append("tittle", tittle);
    data.append("uptittle", uptittle);
    data.append ("mainp", mainp);
    data.append ("mainimg", mainimg);
    data.append("mainalt", mainalt);
    data.append("tittle2", tittle2);
    data.append ("video", video);
    data.append("secondp", secondp);
    data.append("subtitle", subtitle);
    data.append("tittle3", tittle3 );
    data.append("duration", duration);
    data.append("thirdp", thirdp);
    data.append("hashtags", hashtags);
    data.append("album", album);
    data.append("albumtiitle", albumtiitle);
    data.append("albump", albump);
    data.append ("albumalt1", albumalt1);
    data.append ("albumtxt1",  albumtxt1);
    data.append ("albumalt2",  albumalt2);
    data.append ("albumtxt2",  albumtxt2);
    data.append ("albumalt3", albumalt3);
    data.append ("albumtxt3", albumtxt3);
    data.append ("albumalt4", albumalt4);
    data.append ("albumtxt4", albumtxt4);
    data.append ("albumalt5", albumalt5);
    data.append ("albumtxt5", albumtxt5);
    data.append("albumalt6", albumalt6);
    data.append("albumtxt6", albumtxt6);
    // Send request.
    request.send(data);
};


function wut() {
    var chipsData = M.Chips.getInstance($('.chips')).chipsData;
    var chipsDataJson = JSON.stringify(chipsData);
    console.log("this is data =", chipsDataJson);

    let taginput = document.getElementById('mamad');
    taginput.value ='ehsan'
};


// -----------------------------------------------Image Preview ----------------------------------------------

function preview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img1')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
    if (input.files && input.files[1]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img2')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[1]);
    }
    if (input.files && input.files[2]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img3')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[2]);
    }
    if (input.files && input.files[3]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img4')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[3]);
    }
    if (input.files && input.files[4]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img5')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[4]);
    }
    if (input.files && input.files[5]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img6')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[5]);
    }
}


