$(document).ready(function () {
  // Scroll distance after which the menu changes its behavior
  var scrollTrigger = 100

  // Function to handle the scroll event
  function handleScroll() {
    var scrollTop = $(window).scrollTop() // Get current scroll position
    var lightLogo = $("#logo").data("light-logo") // Get the light logo from the data attribute
    var darkLogo = $("#logo").data("dark-logo") // Get the dark logo from the data attribute

    if (scrollTop > scrollTrigger) {
      // Add the fixed-menu class when the scroll exceeds the trigger
      $("#main-nav").addClass("fixed-menu")
      $("#main-nav").css("background-color", "rgba(255, 255, 255, 0.9)") // Light background

      // Change the logo to the dark version
      $("#logo").attr("src", darkLogo)

      // Change menu items to black
      $(".navbar-navigation .nav-link").css("color", "#333")

      // Hide the top bar when scrolling
      $("#top-bar").slideUp()
    } else {
      // Remove the fixed-menu class when scrolling back to the top
      $("#main-nav").removeClass("fixed-menu")
      $("#main-nav").css("background-color", "transparent") // Transparent background

      // Change the logo back to the light version
      $("#logo").attr("src", lightLogo)

      // Reset menu items color
      $(".navbar-navigation .nav-link").css("color", "#fff")

      // Show the top bar again when scrolling back up
      $("#top-bar").slideDown()
    }
  }

  // Run the function on window scroll
  $(window).on("scroll", function () {
    handleScroll()
  })

  // Run the function immediately if the page is already scrolled
  handleScroll()
})
