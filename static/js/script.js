// ---------------------------- Side NavBar -------------------------------

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge:'right'});
});


// ---------------------------- IsoTope -------------------------------


function imageLoad() {
// init Isotope
    var grid = document.querySelector('.grid');

    var iso = new Isotope(grid, {
        itemSelector: '.grid-item',
        percentPosition: true,
        masonry: {
            columnWidth: '.grid-sizer'
        }
    });


    imagesLoaded(grid).on('progress', function () {
        // layout Isotope after each image loads
        iso.layout();

    });

}

// ---------------------------- DropDown w/ Selector -------------------------------
// Initialization
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, );
});


// ---------------------------- Create Circles  -------------------------------
whatSize();
function makeCircle(r, left , top , color) {
    const svg = d3.selectAll('.svg')
    const circ = svg.append('circle')
    circ.attr('r', r)
    circ.attr('cx', left)
    circ.attr('cy', top)
    circ.style('fill', color);
}
// ---------------------------- Night Mode  -------------------------------

function nightMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

// ---------------------------- Screen Height for svg height  -------------------------------
whatSize();

window.addEventListener("resize", whatSize);

function whatSize() {
    var x =  document.body.offsetHeight + "px";
    document.getElementById("addSvgCircle").style.height = x;

}
