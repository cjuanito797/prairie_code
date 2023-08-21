console.log("Sanity check!");

function showAnswer(question) {
  var answer;
  switch (question) {
    case "1":
      answer = document.getElementById("question1");
      answer.style.display = "block";
      break;

    case "2":
      answer = document.getElementById("question2");
      answer.style.display = "block";
      break;

    case "3":
      answer = document.getElementById("question3");
      answer.style.display = "block";
      break;

    case "4":
      answer = document.getElementById("question4");
      answer.style.display = "block";
      break;

    case "5":
      answer = document.getElementById("question5");
      answer.style.display = "block";
      break;
  }
}
