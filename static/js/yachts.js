// static / js / yachts.js

console.log("yachts.js loaded"); // Проверка загрузки файла

document.addEventListener("DOMContentLoaded", function () {
  // Get the element with booked dates from HTML
  const bookedDatesElement = document.getElementById("bookedDates")

  // Initialize an empty array for booked dates
  let bookedDates = []

  // Check if the element exists
  if (bookedDatesElement) {
    try {
      // Parse the JSON content inside the element
      bookedDates = JSON.parse(bookedDatesElement.textContent)
      console.log("Booked Dates:", bookedDates) // Log booked dates for debugging
    } catch (error) {
      console.error("Error parsing booked dates:", error) // Log any parsing error
    }
  }
function handleFormSubmit(event) {
  console.log("Submit button clicked.") // Сообщение для проверки клика
  event.preventDefault() // Остановка стандартного поведения отправки формы
  console.log("Form submission intercepted.") // Подтверждение перехвата отправки формы

  // Получаем все <li> элементы
  const listItems = document.getElementsByTagName("li")
  let yachtId = null

  // Ищем <li>, содержащий "ID:"
  for (let i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent.includes("ID:")) {
        yachtId = listItems[i].textContent.replace("ID:", "").trim()
        console.log(yachtId)
      break // Останавливаем цикл после нахождения нужного элемента
    }
  }

  // Получаем диапазон дат из формы
  const form = document.getElementById("bookingForm")
  const dateRange = form.elements["date_range"].value

  // Логирование значений для отладки
  console.log("Yacht ID:", yachtId) // Вывод идентификатора яхты
  console.log("Date Range:", dateRange) // Вывод диапазона дат

  // Проверка наличия значений
  if (yachtId && dateRange) {
    console.log("Yacht ID and Date Range captured correctly.")
    // Здесь можно добавить AJAX для отправки данных, если нужно
  } else {
    console.error("Yacht ID or Date Range is missing.")
  }
}

window.handleFormSubmit = handleFormSubmit

    window.handleFormSubmit = handleFormSubmit

  // Initialize Flatpickr for date range selection
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
      onChange: function (selectedDates, dateStr) {
        console.log("Selected date range: ", dateStr) // Log the selected date range as a string
        console.log("Selected dates array: ", selectedDates) // Log the selected dates as an array
      },
    })
  }
})
