console.log("yachts.js loaded"); // Check if the file is loaded

document.addEventListener("DOMContentLoaded", async function () {
  const imageContainer = document.querySelector("#yachtGallery .carousel-inner"); 
  const bucketUrl = "https://yachtsescape.s3.eu-west-2.amazonaws.com/media/yachts/details/";
  const totalImages = 4; // Maximum number of images to display
  let selectedDateRange = []; // Store selected date range globally
  let dateRange = []; // New array to store start and end dates
  const dateRangeInput = document.querySelector("#dateRange");
  let yachtId = null;
  const listItems = document.querySelectorAll("li");

  // Find yacht ID by looping through all <li> elements
  listItems.forEach((item) => {
    if (item.textContent.includes("ID:")) {
      yachtId = item.textContent.replace("ID:", "").trim();
    }
  });

  if (!yachtId) {
    console.error("Yacht ID not found.");
    return; // Stop execution if yachtId is not found
  }

  async function fetchBookedDates() {
    try {
      const response = await fetch("/bookings/");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data.booked_dates; // Return booked dates directly
    } catch (error) {
      console.error("Error fetching booked dates:", error);
      return []; // Return an empty array on error
    }
  }

  function getDisabledDates(bookedDates) {
    // Generate a list of dates to disable
    const disabledDates = [];

    bookedDates.forEach((dateRange) => {
      const startDate = new Date(dateRange.start);
      const endDate = new Date(dateRange.end);
      let currentDate = new Date(startDate);

      while (currentDate <= endDate) {
        disabledDates.push(currentDate.toISOString().split("T")[0]); // Convert to YYYY-MM-DD
        currentDate.setDate(currentDate.getDate() + 1); // Increment date
      }
    });

    return disabledDates;
  }

  console.log("Yacht ID:", yachtId); // Log the yacht ID to check if it was found

  // Loop to create image elements
  for (let i = 1; i <= totalImages; i++) {
    const imageUrl = `${bucketUrl}${yachtId}/yacht-${yachtId}-detail-${i}.webp`;
    const carouselItem = document.createElement("div");
    carouselItem.className = `carousel-item ${i === 1 ? "active" : ""}`;
    carouselItem.innerHTML = `<img src="${imageUrl}" class="d-block w-100" alt="Yacht ${yachtId} Image ${i}">`;
    imageContainer.appendChild(carouselItem);
  }

  // Fetch booked dates and initialize Flatpickr
  const bookedDates = await fetchBookedDates();
  const disabledDates = getDisabledDates(bookedDates);

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
          selectedDateRange = [selectedDates[0], selectedDates[1]];

          // Store start and end dates in the dateRange array
          const startDate = new Date(selectedDates[0]);
          const endDate = new Date(selectedDates[1]);

          // Convert to local date format
          dateRange = [
            `${startDate.getFullYear()}-${String(startDate.getMonth() + 1).padStart(2, "0")}-${String(startDate.getDate()).padStart(2, "0")}`, // Start Date
            `${endDate.getFullYear()}-${String(endDate.getMonth() + 1).padStart(2, "0")}-${String(endDate.getDate()).padStart(2, "0")}`, // End Date
          ];
        }
      },
    });
  }

  function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Check if this cookie string begins with the CSRF token name
        if (cookie.startsWith("csrftoken=")) {
          cookieValue = decodeURIComponent(cookie.substring("csrftoken=".length));
          break;
        }
      }
    }
    return cookieValue;
  }

  function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    if (dateRange.length === 2) {
      console.log("Date Range:", `${dateRange[0]} to ${dateRange[1]}`);

      const formData = new FormData();
      formData.append("yacht", yachtId);
      formData.append("date_range", `${dateRange[0]} to ${dateRange[1]}`);

      // Send a POST request
      fetch("/booking/booking/create/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": getCSRFToken(),
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log("Success:", data);
          if (data.success) {
            window.location.href = data.redirect_url;
          } else {
            alert(data.message || "An error occurred.");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("An error occurred during booking.");
        });
    } else {
      alert("No valid date range selected.");
    }
  }

  // Attach handleFormSubmit globally
  window.handleFormSubmit = handleFormSubmit;
});
