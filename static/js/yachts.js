/* jshint esversion: 11 */
/* global flatpickr */

document.addEventListener("DOMContentLoaded", async function () {
  console.log("DOMContentLoaded event fired");

  let selectedDateRange = [];
  let dateRange = [];
  const dateRangeInput = document.querySelector("#dateRange");

  // Initialize yacht ID variable
  let yachtId = null;
  const listItems = document.querySelectorAll("li");

  // Find yacht ID by looping through all <li> elements
  listItems.forEach((item) => {
    if (item.textContent.includes("ID:")) {
      yachtId = item.textContent.replace("ID:", "").trim();
    }
  });

  // Check if yacht ID was found
  if (!yachtId) {
    console.error("Yacht ID not found.");
    return;
  }
  console.log("Yacht ID found:", yachtId);

  /**
   * Function to fetch booked dates for the selected yacht
   * @returns {Promise<Array>} - List of booked dates
   */
  async function fetchBookedDates() {
    try {
      const response = await fetch(`/yachts/yacht/${yachtId}/bookings/`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data.booked_dates;
    } catch (error) {
      console.error("Error fetching booked dates:", error);
      return [];
    }
  }

  /**
   * Function to generate a list of disabled dates based on booked dates
   * @param {Array} bookedDates - Array of booked date ranges
   * @returns {Array} - List of disabled dates
   */
  function getDisabledDates(bookedDates) {
    const disabledDates = [];

    bookedDates.forEach((dateRange) => {
      const startDate = new Date(dateRange.start);
      const endDate = new Date(dateRange.end);
      let currentDate = new Date(startDate);

      while (currentDate <= endDate) {
        disabledDates.push(currentDate.toISOString().split("T")[0]); 
        currentDate.setDate(currentDate.getDate() + 1); 
      }
    });

    return disabledDates;
  }

  // Log yacht ID to ensure it's found correctly
  console.log("Yacht ID:", yachtId);

  // Fetch booked dates and initialize Flatpickr
  const bookedDates = await fetchBookedDates();
  const disabledDates = getDisabledDates(bookedDates);

  // Initialize Flatpickr for date selection
  if (dateRangeInput) {
    flatpickr("#dateRange", {
      mode: "range",
      minDate: "today",
      dateFormat: "Y-m-d",
      disable: disabledDates,
      onChange: function (selectedDates) {
        if (selectedDates.length === 2) {
          // Store the selected date range globally
          selectedDateRange = [selectedDates[0], selectedDates[1]];

          // Store start and end dates in the dateRange array
          const startDate = new Date(selectedDates[0]);
          const endDate = new Date(selectedDates[1]);

          // Convert dates to local format
          dateRange = [
            `${startDate.getFullYear()}-${String(startDate.getMonth() + 1).padStart(2, "0")}-${String(startDate.getDate()).padStart(2, "0")}`,
            `${endDate.getFullYear()}-${String(endDate.getMonth() + 1).padStart(2, "0")}-${String(endDate.getDate()).padStart(2, "0")}`,
          ];
        }
      },
    });
  }

  /**
   * Function to fetch the CSRF token for form submission
   * @returns {string|null} - CSRF token
   */
  function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split("; ");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
          cookieValue = decodeURIComponent(cookie.substring("csrftoken=".length));
          break;
        }
      }
    }
    return cookieValue;
  }

  /**
   * Function to handle form submission for booking
   * @param {Event} event - Form submission event
   */
  function handleFormSubmit(event) {
    event.preventDefault(); 

    if (dateRange.length === 2) {
      console.log("Date Range:", `${dateRange[0]} to ${dateRange[1]}`);

      const formData = new FormData();
      formData.append("yacht", yachtId);
      formData.append("date_range", `${dateRange[0]} to ${dateRange[1]}`);

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
          console.error("Error during booking:", error);
          alert("An error occurred during booking.");
        });
    } else {
      alert("No valid date range selected.");
    }
  }

  // Attach form submission handler globally
  window.handleFormSubmit = handleFormSubmit;
});
