document.addEventListener('DOMContentLoaded', load);

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