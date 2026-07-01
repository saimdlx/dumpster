let shapes = [];
let img;

async function setup() {
  img = await loadImage('assets/E75BE740-16C7-4910-91E5-F236EBDB493C.jpg');
  createCanvas(windowWidth ,windowHeight, WEBGL);
}

function draw() {
  let angle = frameCount * 0.01;
  background("lavender");
  texture(img);
  push();
  rotateX(angle);
  rotateY(angle);
  box(200,200,200);
  pop();
}