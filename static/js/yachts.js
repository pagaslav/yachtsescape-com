console.log("yachts.js loaded") // Confirm the file is loaded

document.addEventListener("DOMContentLoaded", async function () {
  console.log("DOMContentLoaded event fired")

  // Select the carousel inner container
  const imageContainer = document.querySelector("#yachtGallery .carousel-inner")

  // Check if the carousel container exists
  if (!imageContainer) {
    console.error("Carousel container not found.")
    return // Stop further execution if the carousel is not found
  }
  console.log("Carousel container found successfully")

  let selectedDateRange = [] // Store selected date range globally
  let dateRange = [] // New array to store start and end dates
  const dateRangeInput = document.querySelector("#dateRange")

  // Initialize yacht ID variable
  let yachtId = null
  const listItems = document.querySelectorAll("li")

  // Find yacht ID by looping through all <li> elements
  listItems.forEach((item) => {
    if (item.textContent.includes("ID:")) {
      yachtId = item.textContent.replace("ID:", "").trim()
    }
  })

  // Check if yacht ID was found
  if (!yachtId) {
    console.error("Yacht ID not found.")
    return // Stop execution if yacht ID is not found
  }
  console.log("Yacht ID found:", yachtId)

  // Get the image data from the data attribute as JSON
  const imageDataElement = document.getElementById("image-data")

  if (!imageDataElement) {
    console.error("Element with id 'image-data' not found.")
    return // Stop execution if image data element is not found
  }

  let images
  try {
    images = JSON.parse(imageDataElement.dataset.images) // Extract the images array
    console.log("Images array:", images)
  } catch (error) {
    console.error("Error parsing JSON for images:", error)
    return
  }

  // Create carousel items for each image
  images.forEach((imageUrl, index) => {
    const carouselItem = document.createElement("div")
    carouselItem.className = `carousel-item ${index === 0 ? "active" : ""}`
    carouselItem.innerHTML = `<img src="${imageUrl}" class="d-block w-100" alt="Yacht ${yachtId} Image ${
      index + 1
      }">`
    imageContainer.appendChild(carouselItem)
  })

  // Fetch booked dates
  async function fetchBookedDates() {
    try {
      const response = await fetch(`/yachts/yacht/${yachtId}/bookings/`)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }
      const data = await response.json()
      return data.booked_dates // Return booked dates directly
    } catch (error) {
      console.error("Error fetching booked dates:", error)
      return [] // Return an empty array on error
    }
  }

  // Generate a list of dates to disable for booking
  function getDisabledDates(bookedDates) {
    const disabledDates = []

    bookedDates.forEach((dateRange) => {
      const startDate = new Date(dateRange.start)
      const endDate = new Date(dateRange.end)
      let currentDate = new Date(startDate)

      while (currentDate <= endDate) {
        disabledDates.push(currentDate.toISOString().split("T")[0]) // Convert to YYYY-MM-DD format
        currentDate.setDate(currentDate.getDate() + 1) // Increment the date
      }
    })

    return disabledDates
  }

  // Log yacht ID to ensure it's found correctly
  console.log("Yacht ID:", yachtId)

  // Fetch booked dates and initialize Flatpickr
  const bookedDates = await fetchBookedDates()
  const disabledDates = getDisabledDates(bookedDates)

  // Initialize Flatpickr for date selection
  if (dateRangeInput) {
    flatpickr("#dateRange", {
      mode: "range",
      minDate: "today",
      dateFormat: "Y-m-d",
      disable: disabledDates, // Use the array of disabled dates directly
      onChange: function (selectedDates) {
        if (selectedDates.length === 2) {
          // Store the selected date range globally
          selectedDateRange = [selectedDates[0], selectedDates[1]]

          // Store start and end dates in the dateRange array
          const startDate = new Date(selectedDates[0])
          const endDate = new Date(selectedDates[1])

          // Convert dates to local format
          dateRange = [
            `${startDate.getFullYear()}-${String(
              startDate.getMonth() + 1
            ).padStart(2, "0")}-${String(startDate.getDate()).padStart(
              2,
              "0"
            )}`, // Start Date
            `${endDate.getFullYear()}-${String(endDate.getMonth() + 1).padStart(
              2,
              "0"
            )}-${String(endDate.getDate()).padStart(2, "0")}`, // End Date
          ]
        }
      },
    })
  }

  // Fetch CSRF token for form submission
  function getCSRFToken() {
    let cookieValue = null
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split("; ")
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim()
        if (cookie.startsWith("csrftoken=")) {
          cookieValue = decodeURIComponent(
            cookie.substring("csrftoken=".length)
          )
          break
        }
      }
    }
    return cookieValue
  }

  // Handle form submission for booking
  function handleFormSubmit(event) {
    event.preventDefault() // Prevent default form submission

    if (dateRange.length === 2) {
      console.log("Date Range:", `${dateRange[0]} to ${dateRange[1]}`)

      const formData = new FormData()
      formData.append("yacht", yachtId)
      formData.append("date_range", `${dateRange[0]} to ${dateRange[1]}`)

      // Send a POST request for booking
      fetch("/booking/booking/create/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": getCSRFToken(),
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`)
          }
          return response.json()
        })
        .then((data) => {
          console.log("Success:", data)
          if (data.success) {
            window.location.href = data.redirect_url
          } else {
            alert(data.message || "An error occurred.")
          }
        })
        .catch((error) => {
          console.error("Error during booking:", error)
          alert("An error occurred during booking.")
        })
    } else {
      alert("No valid date range selected.")
    }
  }

  // Attach form submission handler globally
  window.handleFormSubmit = handleFormSubmit
})
