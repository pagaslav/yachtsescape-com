// Wait for the DOM to fully load
$(document).ready(function () {
  // Load the Lottie animation
  var animation = lottie.loadAnimation({
    container: $("#boat-animation")[0], // Container for the animation
    renderer: "svg", // Type of renderer
    loop: true, // Loop the animation
    autoplay: true, // Start playback automatically
    path: "media/lottie/preload-boat.lottie", // Path to your .lottie file
  })
})