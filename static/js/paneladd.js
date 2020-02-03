// ----------------------------------------------- Floating Button ----------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {toolbarEnabled: true});


// ----------------------------------------------- Receive Categories ----------------------------------------------


// ----------------------------------------------- Char Counter ----------------------------------------------

// for text counts in insert feild

$('.validate, textarea').characterCounter();



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

});


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


