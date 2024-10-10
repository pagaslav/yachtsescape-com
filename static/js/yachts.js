console.log("yachts.js loaded") // Check if the file is loaded

document.addEventListener("DOMContentLoaded", function () {
  const bookedDatesElement = document.getElementById("bookedDates")
  let bookedDates = []

  // Parse booked dates from JSON
  if (bookedDatesElement) {
    try {
      bookedDates = JSON.parse(bookedDatesElement.textContent)
      console.log("Booked Dates:", bookedDates) // Log booked dates
    } catch (error) {
      console.error("Error parsing booked dates:", error) // Log parsing error
    }
  }

  // Find yacht ID by looping through all <li> elements
  let yachtId = null
  const listItems = document.querySelectorAll("li")
  listItems.forEach((item) => {
    if (item.textContent.includes("ID:")) {
      yachtId = item.textContent.replace("ID:", "").trim()
    }
  })

  if (!yachtId) {
    console.error("Yacht ID not found.")
    return // Stop execution if yachtId is not found
  }

  console.log("Yacht ID:", yachtId) // Log the yacht ID to check if it was found
  const imageContainer = document.querySelector("#yachtGallery .carousel-inner") // Select the carousel inner container

  // Fetch images from the API if yachtId is found
  fetch(`/api/yacht/${yachtId}/images`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`)
      }
      return response.json()
    })
    .then((images) => {
      if (images.length === 0) {
        console.log("No images found, using default image.")
        const carouselItem = document.createElement("div")
        carouselItem.className = "carousel-item active"
        carouselItem.innerHTML = `<img src="/media/default_image.jpg" class="d-block w-100" alt="Default Image">`
        imageContainer.appendChild(carouselItem)
      } else {
        images.forEach((image, index) => {
          const carouselItem = document.createElement("div")
          carouselItem.className = `carousel-item ${
            index === 0 ? "active" : ""
          }`
          carouselItem.innerHTML = `<img src="${image}" class="d-block w-100" alt="Image ${
            index + 1
          }">`
          imageContainer.appendChild(carouselItem) // Append the carousel item
        })
      }
    })
    .catch((error) => console.error("Error fetching images:", error)) // Log fetch error

  // Form submission handler
  window.handleFormSubmit = function (event) {
    event.preventDefault() // Prevent default form submission
    const form = document.getElementById("bookingForm")
    const dateRange = form.elements["date_range"].value

    // Log yacht ID and date range
    console.log("Yacht ID:", yachtId)
    console.log("Date Range:", dateRange)
  }

  // Initialize Flatpickr for date selection
  const dateRangeInput = document.querySelector("#dateRange")
  if (dateRangeInput) {
    flatpickr("#dateRange", {
      mode: "range",
      minDate: "today",
      dateFormat: "Y-m-d",
      disable: bookedDates.map((date) => ({
        from: date.start,
        to: date.end,
      })),
    })
  }
})
