//global variable to make use of call stack to remember what the last tab that was clicked on was.
var lastTabClicked = "";

function changeContent(value) {
  var overview = document.getElementById("techStackTitle");
  var details = document.getElementById("techStackDetails");
  //so we want to keep track of which button is currently active, and which button to make that the is-active.

  //we also need to remove the classes when we are switching tabs.

  let current_tab = "";
  let current_button = "";
  let previous_tab = "";
  let previous_button = "";
  let image = "";

  if (lastTabClicked === "" || lastTabClicked === "overview") {
    //set the display properties equal to none.
    document.getElementById("overviewSection").style.display = "none";
    previous_tab = document.getElementById("overview");
    previous_button = document.getElementById("overviewButton");
    previous_tab.classList.remove("is-active");
    previous_button.classList.add("has-text-white");
  }

  //only do this when the string is not "".
  if (!(lastTabClicked === "")) {
    console.log("The last tab you clicked on was", lastTabClicked);

    if (lastTabClicked === 'front-end') {
      //This means that front-end should have its active status removed.


      previous_tab = document.getElementById("front-end");
      previous_button = document.getElementById("frontEndButton");
      previous_tab.classList.remove("is-active");
      previous_button.classList.add("has-text-white");
      document.getElementById("frontEndTechnologies").style.display = "none";
    }

    else if (lastTabClicked == 'back-end') {
      //remove active status from back-end tab.
      previous_tab = document.getElementById("back-end");
      previous_button = document.getElementById("backEndButton");
      previous_tab.classList.remove("is-active");
      previous_button.classList.add("has-text-white");
      document.getElementById("backEndTechnologies").style.display = "none";
    }

    else if (lastTabClicked == 'hosting') {
      previous_tab = document.getElementById("hosting");
      previous_button = document.getElementById("hostingButton");
      previous_tab.classList.remove("is-active");
      previous_button.classList.add("has-text-white");
      document.getElementById("hostingTechnologies").style.display = "none";
    }

    else if (lastTabClicked === 'database') {
      previous_tab = document.getElementById("database");
      previous_button = document.getElementById("databaseButton");
      previous_tab.classList.remove("is-active");
      previous_button.classList.add("has-text-white");
      document.getElementById("databaseTechnologies").style.display = "none";
    }

    else if (lastTabClicked === 'overview') {

    }
  }

  //store the lastTab used after we have checked which one we need to remove active status for. So that we can efficiently make use of call stack.
  storePrevTab(value);


  switch (value) {

    case 'overview':
      overview.innerHTML = "Overview";
      details.innerHTML = "Hello there my name is Juan Lizarraga-Cortez. I'm a seasoned web developer. So what is it exactly that a web developer does, and what are the different aspects that go into building a sophisticated website? Below I have broken down the process, into 4 main categories, you may click on each of the tasks below to learn a little bit more about each subject.";
      current_tab = document.getElementById("overview");
      current_button = document.getElementById("overviewButton");
      current_tab.classList.add("is-active");
      current_button.classList.remove("has-text-white");
      document.getElementById("overviewSection").style.display = "block";
      break;
    case 'front-end':
      overview.innerHTML = "Front-end Technologies";
      details.innerHTML = "These are the core technologies that we utilize in order to build out the visual layout of your page, without them the web as we know it would not exist. Here is what each of them does: <li>HTML: Used to create the main layout of your page.</li> <li>CSS: Utilized for creating animations, beautiful page transitions, and adding eye popping imagery</li><li>JavaScript(JS): Allows for us to build out dynamic features for youur website. Suuch as clicking through these different tabs</li>";
      current_tab = document.getElementById("front-end");
      current_button = document.getElementById("frontEndButton");
      current_tab.classList.add("is-active");
      current_button.classList.remove("has-text-white");
      document.getElementById("frontEndTechnologies").style.display = "block";

      break;

    case 'back-end':
      overview.innerHTML = "Back-end Technologies";
      details.innerHTML = "In order to bring your application to life for providing fruitful services to you and your business, a lot of work and engineering needs to be done behind the scenes. So what exactly do each of these do? (From left to right): <li>Python: This is what allows us to build out the business logic for how your website needs to operate. Allows us to build out logic for system requirements such as user registrations, log in, and so forth.</li><li>Vue.js: this is a framework that allows for us to building out highly complex user interfaces.</li><li>Django: this is what we utilize to contain your web application so that all of the many different applications and technologies that we use can effectively communicate with each other.</li>";
      //clear the values of active and button by removing classes.
      current_tab = document.getElementById("back-end");
      current_tab.classList.add("is-active");
      current_button = document.getElementById("backEndButton");
      current_button.classList.remove("has-text-white");
      document.getElementById("backEndTechnologies").style.display = "block";
      break;

    case 'hosting':
      overview.innerHTML = "Hosting";
      details.innerHTML = "We utilize Amazon AWS Cloud platform iin order to host your website. We leverage the power of cloud technologies, because this eliminates any hardware overhead, meaning that neither parties are responsible for the management or maintenance of physical hardware devices.";
      current_tab = document.getElementById("hosting");
      current_button = document.getElementById("hostingButton");
      current_tab.classList.add("is-active");
      current_button.classList.remove("has-text-white");
      document.getElementById("hostingTechnologies").style.display = "block";
      break;

    case 'database':
      overview.innerHTML = "Database";
      details.innerHTML = "In order to store the data for your business we make use of the popular MySQL Database for its ease of use for performing data operations such as updating, accessing, creation, deletion."
      current_tab = document.getElementById("database");
      current_button = document.getElementById("databaseButton");
      current_tab.classList.add("is-active");
      current_button.classList.remove("has-text-white");
      document.getElementById("databaseTechnologies").style.display = "block";
      break;

  }
}


function storePrevTab(value) {
  lastTabClicked = value;
}
