d3.select("#addSvgCircle")
    .append('svg')
    .attr('class', 'svg ');


for (var i = 0; i < avgcircle.length; i++) {
    makeCircle(
        avgcircle[i].r,
        avgcircle[i].left,
        avgcircle[i].top,
        avgcircle[i].color)
}

// ---------------------------------------- Album ---------------------------------------
 function changeCover(image) {

     if (image.id === 'left1'){
         const src = document.getElementById('left1').style.backgroundImage.slice(4, -1).replace(/"/g, "");
         document.getElementById('albumcoverimg').src = src
     }
     if (image.id === 'left2'){
            const src = document.getElementById('left2').style.backgroundImage.slice(4, -1).replace(/"/g, "");
            document.getElementById('albumcoverimg').src = src
     }
     if (image.id === 'left3'){
         const src = document.getElementById('left3').style.backgroundImage.slice(4, -1).replace(/"/g, "");
         document.getElementById('albumcoverimg').src = src
     }
     if (image.id === 'right1'){
         const src = document.getElementById('right1').style.backgroundImage.slice(4, -1).replace(/"/g, "");
         document.getElementById('albumcoverimg').src = src
     }
     if (image.id === 'right2'){
         const src = document.getElementById('right2').style.backgroundImage.slice(4, -1).replace(/"/g, "");
         document.getElementById('albumcoverimg').src = src
     }
     if (image.id === 'right3'){
         const src = document.getElementById('right3').style.backgroundImage.slice(4, -1).replace(/"/g, "");
         document.getElementById('albumcoverimg').src = src
     }

 }


// -------------------------------- Carousel ------------------------------
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
        dist: -50,
        padding: 10,
        fullWidth: false,
        indicators: false,
        duration: 200,
    });


    // hide the one with no picture, first get background url
    const all = document.querySelectorAll('.carousel-item');

    var i;
    for (i = 0; i < all.length; i++) {
        const item = all[i] ;
        if (item.style.backgroundImage === 'url("/")'){
            all[i].remove(elems)
            // instances[i].destroy();
            console.log(instances)
        }
    }


});

// function nextPage() {
//     // $('.carousel').carousel('next');
//     // setTimeout(nextPage, 400);
//     var elems = document.querySelectorAll('.carousel');
//     var instances = M.Carousel.init(elems, {
//         dist: -100,
//         padding: 0,
//         fullWidth: false,
//         indicators: false,
//         duration: 200,
//     });
//     console.log('huh')
//     instances[1].destroy()
//     instances[0].next(3);
// }
