var myQuest = new XMLHttpRequest()

myQuest.open('GET','https://learnwebcode.github.io/json-example/animals-1.json')

myQuest.onload = function(){
  var data = JSON.parse(myQuest.responseText);
  console.log(data[0])
};  
myQuest.send();