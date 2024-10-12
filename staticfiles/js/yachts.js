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
    
  let selectedDateRange = []; // Store selected date range globally
  let dateRange = []; // New array to store start and end dates
  
  // Initialize Flatpickr for date selection
  const dateRangeInput = document.querySelector("#dateRange");
  if (dateRangeInput) {
    flatpickr("#dateRange", {
      mode: "range",
      minDate: "today",
      dateFormat: "Y-m-d",
      disable: bookedDates.map((date) => ({
        from: date.start,
        to: date.end,
      })),
      onChange: function (selectedDates, dateStr, instance) {
        if (selectedDates.length === 2) {
          // Store the selected date range globally
          selectedDateRange = [selectedDates[0], selectedDates[1]];
          
          // Store start and end dates in the dateRange array
          const startDate = new Date(selectedDates[0]);
          const endDate = new Date(selectedDates[1]);
      
          // Convert to local date format
          dateRange = [
            `${startDate.getFullYear()}-${String(startDate.getMonth() + 1).padStart(2, '0')}-${String(startDate.getDate()).padStart(2, '0')}`, // Start Date
            `${endDate.getFullYear()}-${String(endDate.getMonth() + 1).padStart(2, '0')}-${String(endDate.getDate()).padStart(2, '0')}`  // End Date
          ];
        }
      }
      
    });
  }

  function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the CSRF token name
            if (cookie.startsWith('csrftoken=')) {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken='.length));
                break;
            }
        }
    }
    return cookieValue;
}
  
  // Form submission handler
  window.handleFormSubmit = function (event) {
    event.preventDefault(); // Prevent default form submission
  
    // Log yacht ID and date range
    console.log("Yacht ID:", yachtId);
  
    if (dateRange.length === 2) {
        console.log("Date Range:", `${dateRange[0]} to ${dateRange[1]}`);
        
        // Construct the data to send
        const formData = new FormData();
        formData.append('yacht', yachtId);
        formData.append('date_range', `${dateRange[0]} to ${dateRange[1]}`);

        // Send a POST request using Fetch API
        fetch('/booking/booking/create/', { // Replace with your actual URL
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': getCSRFToken() // Ensure you include CSRF token for security
          }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        console.log("No valid date range selected");
    }
};

})
