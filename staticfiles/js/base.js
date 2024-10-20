// static / js / base.js

$(document).ready(function () {
  let scrollTrigger = 50

  // Function to change the logo based on scroll position and window width
  function updateLogo() {
    let windowWidth = $(window).width()
    let scrollTop = $(window).scrollTop()
    let lightLogo = $("#logo").data("light-logo")
    let darkLogo = $("#logo").data("dark-logo")
    let smallLightLogo = $("#logo").data("small-light-logo")
    let smallDarkLogo = $("#logo").data("small-dark-logo")

    if (scrollTop > scrollTrigger) {
      // Change logo to dark version based on screen size
      if (windowWidth < 689) {
        console.log("Switching to small dark logo:", smallDarkLogo)
        $("#logo").attr("src", smallDarkLogo)
      } else {
        console.log("Switching to dark logo:", darkLogo)
        $("#logo").attr("src", darkLogo)
      }
    } else {
      // Change logo to light version based on screen size
      if (windowWidth < 689) {
        console.log("Switching to small light logo:", smallLightLogo)
        $("#logo").attr("src", smallLightLogo)
      } else {
        console.log("Switching to light logo:", lightLogo)
        $("#logo").attr("src", lightLogo)
      }
    }
  }

  // Function to handle the scroll event
  function handleScroll() {
    let scrollTop = $(window).scrollTop()

    if (scrollTop > scrollTrigger) {
      $("#main-nav").addClass("fixed-menu")
      $("#main-nav").css("background-color", "rgba(255, 255, 255, 0.9)")
      $(".navbar-navigation .nav-link").css("color", "#333")
      $(".navbar-toggler-icon").css(
        "background-image",
        "url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3E%3Cpath stroke=%27rgba(0, 0, 0, 1)%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3E%3C/svg%3E')"
      )
      $("#logo").parent().css("padding-left", "30px")
      $(".header-main-btn").css("margin-right", "30px")
      $(".navbar-toggler").css("margin-right", "30px")
      $("#top-bar").slideUp()
    } else {
      $("#main-nav").removeClass("fixed-menu")
      $("#main-nav").css("background-color", "transparent")
      $(".navbar-navigation .nav-link").css("color", "#fff")
      $(".navbar-toggler-icon").css(
        "background-image",
        "url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3E%3Cpath stroke=%27rgba(255, 255, 255, 1)%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3E%3C/svg%3E')"
      )
      $("#logo").parent().css("padding-left", "0")
      $(".header-main-btn").css("margin-right", "0")
      $(".navbar-toggler").css("margin-right", "0")
      $("#top-bar").slideDown()
    }

    // Call the updateLogo function to ensure logo changes as needed
    updateLogo()
  }

  // Handle scroll events
  $(window).on("scroll", function () {
    handleScroll()
  })

  // Handle resize events to update logo when screen size changes
  $(window).on("resize", function () {
    updateLogo()
  })

  // Run the function immediately if the page is already scrolled or resized
  handleScroll()

  // Password validation functions
  const passwordField = document.querySelector(
    "#{{ form.password1.id_for_label }}"
  )
  const confirmPasswordField = document.querySelector(
    "#{{ form.password2.id_for_label }}"
  )
  const confirmPasswordError = document.getElementById("confirmPasswordError")
  const lengthRequirement = document.getElementById("lengthRequirement")
  const uppercaseRequirement = document.getElementById("uppercaseRequirement")
  const numberRequirement = document.getElementById("numberRequirement")

  lengthRequirement.classList.add("text-red")
  uppercaseRequirement.classList.add("text-red")
  numberRequirement.classList.add("text-red")

  function validatePassword() {
    const password = passwordField.value
    let isValid = true

    lengthRequirement.classList.remove("text-gray")
    uppercaseRequirement.classList.remove("text-gray")
    numberRequirement.classList.remove("text-gray")

    if (password.length >= 8) {
      lengthRequirement.classList.remove("text-red")
      lengthRequirement.classList.add("text-gray")
    } else {
      lengthRequirement.classList.add("text-red")
    }

    if (/[A-Z]/.test(password)) {
      uppercaseRequirement.classList.remove("text-red")
      uppercaseRequirement.classList.add("text-gray")
    } else {
      uppercaseRequirement.classList.add("text-red")
    }

    if (/\d/.test(password)) {
      numberRequirement.classList.remove("text-red")
      numberRequirement.classList.add("text-gray")
    } else {
      numberRequirement.classList.add("text-red")
    }

    isValid =
      password.length >= 8 && /[A-Z]/.test(password) && /\d/.test(password)
    if (isValid) {
      passwordField.classList.remove("is-invalid")
    } else {
      passwordField.classList.add("is-invalid")
    }
  }

  function validateConfirmPassword() {
    const password = passwordField.value
    const confirmPassword = confirmPasswordField.value

    if (password !== confirmPassword) {
      confirmPasswordError.innerText = "Passwords do not match."
      confirmPasswordField.classList.add("is-invalid")
    } else {
      confirmPasswordError.innerText = ""
      confirmPasswordField.classList.remove("is-invalid")
    }
  }

  passwordField.addEventListener("input", validatePassword)
  confirmPasswordField.addEventListener("input", validateConfirmPassword)

  const form = document.querySelector("form")
  form.addEventListener("submit", function (event) {
    validatePassword()
    validateConfirmPassword()
    if (
      passwordField.classList.contains("is-invalid") ||
      confirmPasswordField.classList.contains("is-invalid")
    ) {
      event.preventDefault() // Prevent form submission if validation fails
    }
  })
})

function togglePasswordVisibility(passwordFieldId, iconId) {
    const passwordField = document.getElementById(passwordFieldId);
    const icon = document.getElementById(iconId);
    if (passwordField.type === "password") {
        passwordField.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    } else {
        passwordField.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
}