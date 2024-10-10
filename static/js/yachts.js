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

  // Define the base URL for images
  const bucketUrl =
    "https://yachtsescape.s3.eu-west-2.amazonaws.com/media/yachts/details/"
  const totalImages = 4 // Maximum number of images to display

  // Loop to create image elements
  for (let i = 1; i <= totalImages; i++) {
    const imageUrl = `${bucketUrl}${yachtId}/yacht-${yachtId}-detail-${i}.webp`
    const carouselItem = document.createElement("div")
    carouselItem.className = `carousel-item ${i === 1 ? "active" : ""}`
    carouselItem.innerHTML = `<img src="${imageUrl}" class="d-block w-100" alt="Yacht ${yachtId} Image ${i}">`
    imageContainer.appendChild(carouselItem)
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
  // Form submission handler
  window.handleFormSubmit = function (event) {
    event.preventDefault() // Prevent default form submission
    const form = document.getElementById("bookingForm")
    const dateRange = form.elements["date_range"].value

    // Log yacht ID and date range
    console.log("Yacht ID:", yachtId)
    console.log("Date Range:", dateRange)
  }
})
