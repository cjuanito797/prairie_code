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

    case 'design_process':
      content.innerHTML = "Once we have had a good chance to sit down and learn about your business, and have received a signed and dated contract from your end can we begin the work on your website. Laying out the initial groundwork by prototyping user interface screens";
      break;

    case 'development':
      content.innerHTML = "The development process is a meticulous process involving a lot of software engineering on our end. Computers only serve the people when somebody on the backend performed strenous work as compuuters themselves can't program themselves that is the job of the developer/software engineer. This is where the system requirements gathered from our initial meeting are put into place. So that the end result is a sophisticated and reliable system that is designed specifically around you and your business.";
      break;

    case 'revisions':
      content.innerHTML = "Revisions are an ongoing process, without you giving us 100% autonomy to do our work without your input there is no possible way for us to move forward. We value your input and need to be ensured that you are favoring the progress of the project.";
      break;

    case 'deployment':
      content.innerHTML = "Once revisions, development and design have all been completed can we finally deploy. The hosting provider that we tend to prefer is Amazon AWS, AWS allows us to leverage cloud technologies so that we can avoid any hardware overhead.";
      break;

    case 'project_launch':
      content.innerHTML = "Once the project has been deployed, we have secured your website using the latest security features and packages, your domain has been registered and implemented, can the project really takeoff. After the project has been launched, we remain in the co-pilots seat so that we may conducty user experience tests, troubleshoot any issues as they may arise, contiously make improvements and so forth.";
      break;
  }
}

function closeModal() {
  var modal = document.getElementById("information_card");
  modal.classList.remove("is-active");
}
