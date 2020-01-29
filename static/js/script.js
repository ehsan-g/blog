// ---------------------------- Side NavBar -------------------------------

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge:'right'});
});


// ---------------------------- IsoTope -------------------------------


function imageload() {
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


