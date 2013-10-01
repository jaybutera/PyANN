(function() {
    var canvas = document.getElementById('canvas'),
         context = canvas.getContext('2d');

    window.addEventListener('resize', resizeCanvas, false);

    function resizeCanvas() {
         canvas.width = window.innerWidth-300;
         canvas.height = window.innerHeight;

         drawStuff();
    }
    resizeCanvas();

    function drawStuff() {
    }
})();
