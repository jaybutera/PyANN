$(document).ready(function(){
    draw();
});

function draw() {  
    ctx = document.createElement('ctx');
    ctx.id     = "CursorLayer";
    ctx.width  = window.innerWidth;
    ctx.height = window.innerHeight;
    ctx.style.zIndex   = 8;
    ctx.style.position = "absolute";
    ctx.style.border   = "1px solid";
    document.body.appendChild(ctx);
}
