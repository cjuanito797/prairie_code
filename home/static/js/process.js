console.log("Sanity Check!");

function openModal(card) {
  console.log("Showing details for: ", card);
  var modal = document.getElementById("information_card");
  var content = document.getElementById("card_content");
  modal.classList.add("is-active");

  switch (card) {
    case 'initial_meeting':
      content.innerHTML = "Our initial meeting may be conducted either in person in your location of choice or may be conducted entirely online. The purpose of our initial meeting is simple to get to know you as a busineess owner and your business. During our initial meeting we want to know what is it that you feel is important for your business.";
      break;
  }
}

function closeModal() {
  var modal = document.getElementById("information_card");
  modal.classList.remove("is-active");
}
