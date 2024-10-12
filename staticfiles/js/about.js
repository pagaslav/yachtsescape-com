// document.querySelectorAll(".mark-helpful").forEach((button) => {
//   button.addEventListener("click", function (event) {
//     event.preventDefault()
//     const reviewId = this.dataset.id
//     fetch(`/about/review/${reviewId}/helpful/`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": "{{ csrf_token }}",
//       },
//       body: JSON.stringify({ review_id: reviewId }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         if (data.success) {
//           location.reload()
//         } else {
//           alert(data.message)
//         }
//       })
//   })
// })
