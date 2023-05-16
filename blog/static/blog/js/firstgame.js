// script.js

var score = 0;
var numQuestions = 0;
var correctAnswer; // Declare correctAnswer at a higher scope

function generateQuestion() {
  var num1 = Math.floor(Math.random() * 10) + 1;
  var num2 = Math.floor(Math.random() * 10) + 1;
  var operator = Math.random() < 0.5 ? '+' : '-';

  var question = num1 + ' ' + operator + ' ' + num2;
  correctAnswer = eval(question); // Assign correctAnswer to the higher scoped variable

  document.getElementById('question').textContent = question;
  document.getElementById('answer').value = '';
  document.getElementById('result').textContent = '';

  document.getElementById('answer').focus();

  return correctAnswer;
}

function checkAnswer() { // Remove correctAnswer as a parameter
  var userAnswer = parseInt(document.getElementById('answer').value);

  if (userAnswer === correctAnswer) {
    document.getElementById('result').textContent = 'Correct!';
    score++;
  } else {
    document.getElementById('result').textContent = 'Wrong!';
  }

  numQuestions++;
  document.getElementById('answer').value = '';
  setTimeout(generateNextQuestion, 1000);
}

function generateNextQuestion() {
  if (numQuestions < 10) {
    correctAnswer = generateQuestion(); // Assign correctAnswer to the higher scoped variable
    document.getElementById('score').textContent = 'Score: ' + score;
  } else {
    document.getElementById('question').textContent = 'Game Over';
    document.getElementById('answer').style.display = 'none';
    document.getElementById('result').textContent = 'Final Score: ' + score;
  }
}

document.getElementById('answer').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') {
    checkAnswer();
  }
});

generateNextQuestion();
