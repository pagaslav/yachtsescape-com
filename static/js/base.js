/* jshint esversion: 11 */
/* global $ */

$(document).ready(function () {
  let scrollTrigger = 70;

  /**
   * Function to update the logo based on scroll position and window width
   */
  function updateLogo() {
    let windowWidth = $(window).width();
    let scrollTop = $(window).scrollTop();
    let lightLogo = $("#logo").data("light-logo");
    let darkLogo = $("#logo").data("dark-logo");
    let smallLightLogo = $("#logo").data("small-light-logo");
    let smallDarkLogo = $("#logo").data("small-dark-logo");

    if (scrollTop > scrollTrigger) {
      if (windowWidth < 689) {
        $("#logo").attr("src", smallDarkLogo);
      } else {
        $("#logo").attr("src", darkLogo);
      }
    } else {
      if (windowWidth < 689) {
        $("#logo").attr("src", smallLightLogo);
      } else {
        $("#logo").attr("src", lightLogo);
      }
    }
  }

  /**
   * Function to handle scroll events and update UI elements accordingly
   */
  function handleScroll() {
    let scrollTop = $(window).scrollTop();
    let heroTrigger = 300;
    let searchFormTrigger = 550;

    if (scrollTop > scrollTrigger) {
      $("#main-nav").addClass("fixed-menu").css("z-index", "999");
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
      $("#main-nav").removeClass("fixed-menu").css("z-index", "auto");
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

    if (scrollTop > heroTrigger) {
      $(".hero-index-content").fadeOut();
    } else {
      $(".hero-index-content").fadeIn();
    }

    if (scrollTop > searchFormTrigger) {
      $(".search-form-container").fadeOut();
    } else {
      $(".search-form-container").fadeIn();
    }

    updateLogo();
  }

  $(window).on("scroll", function () {
    handleScroll();
  });

  $(window).on("resize", function () {
    updateLogo();
  });

  handleScroll();

  /**
   * Function to toggle password visibility
   */
  $(".password-toggle").on("click", function () {
    const passwordField = $(this).siblings("input");
    const icon = $(this).find("i");
    if (passwordField.attr("type") === "password") {
      passwordField.attr("type", "text");
      icon.removeClass("fa-eye").addClass("fa-eye-slash");
    } else {
      passwordField.attr("type", "password");
      icon.removeClass("fa-eye-slash").addClass("fa-eye");
    }
  });
});

/**
 * Function to get a cookie value by name
 */
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie("csrftoken");

$.ajaxSetup({
  headers: { "X-CSRFToken": csrftoken },
});
