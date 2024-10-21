$(document).ready(function () {
  let scrollTrigger = 50;

  // Function to change the logo based on scroll position and window width
  function updateLogo() {
    let windowWidth = $(window).width();
    let scrollTop = $(window).scrollTop();
    let lightLogo = $("#logo").data("light-logo");
    let darkLogo = $("#logo").data("dark-logo");
    let smallLightLogo = $("#logo").data("small-light-logo");
    let smallDarkLogo = $("#logo").data("small-dark-logo");

    if (scrollTop > scrollTrigger) {
      // Change logo to dark version based on screen size
      if (windowWidth < 689) {
        $("#logo").attr("src", smallDarkLogo);
      } else {
        $("#logo").attr("src", darkLogo);
      }
    } else {
      // Change logo to light version based on screen size
      if (windowWidth < 689) {
        $("#logo").attr("src", smallLightLogo);
      } else {
        $("#logo").attr("src", lightLogo);
      }
    }
  }

  // Function to handle the scroll event
  function handleScroll() {
    let scrollTop = $(window).scrollTop();

    if (scrollTop > scrollTrigger) {
      $("#main-nav").addClass("fixed-menu");
      $("#main-nav").css("background-color", "rgba(255, 255, 255, 0.9)");
      $(".navbar-navigation .nav-link").css("color", "#333");
      $(".navbar-toggler-icon").css(
        "background-image",
        "url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3E%3Cpath stroke=%27rgba(0, 0, 0, 1)%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3E%3C/svg%3E')"
      );
      $("#logo").parent().css("padding-left", "30px");
      $(".header-main-btn").css("margin-right", "30px");
      $(".navbar-toggler").css("margin-right", "30px");
      $("#top-bar").slideUp();
    } else {
      $("#main-nav").removeClass("fixed-menu");
      $("#main-nav").css("background-color", "transparent");
      $(".navbar-navigation .nav-link").css("color", "#fff");
      $(".navbar-toggler-icon").css(
        "background-image",
        "url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3E%3Cpath stroke=%27rgba(255, 255, 255, 1)%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3E%3C/svg%3E')"
      );
      $("#logo").parent().css("padding-left", "0");
      $(".header-main-btn").css("margin-right", "0");
      $(".navbar-toggler").css("margin-right", "0");
      $("#top-bar").slideDown();
    }

    // Call the updateLogo function to ensure logo changes as needed
    updateLogo();
  }

  // Handle scroll events
  $(window).on("scroll", function () {
    handleScroll();
  });

  // Handle resize events to update logo when screen size changes
  $(window).on("resize", function () {
    updateLogo();
  });

  // Run the function immediately if the page is already scrolled or resized
  handleScroll();

    // Toggle password visibility
    $(".password-toggle").on("click", function () {
      const passwordField = $(this).siblings("input")
      const icon = $(this).find("i")
      if (passwordField.attr("type") === "password") {
        passwordField.attr("type", "text")
        icon.removeClass("fa-eye").addClass("fa-eye-slash")
      } else {
        passwordField.attr("type", "password")
        icon.removeClass("fa-eye-slash").addClass("fa-eye")
      }
    })
  })