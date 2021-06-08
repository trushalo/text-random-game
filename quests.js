const textElement = document.getElementById('text')
const optionButtonsElement = document.getElementById('option-buttons')

function pullQuest()
  {
  }

class Option {
  
  constructor (text, successText, failText, income, failCost, successMin)
  {
    
  }
}

class BasicQuest {

  constructor(name, text, success, option1, option2, option3, option4) {
    this.name = name;
    this.text = text;
    this.success = 5;
    this.baseIncome = 1;
  }
let questArray=[

]



//functions built for use

function randomIntFromInterval(min,max) {
    return Math.floor(Math.random() * (max- min + 1)+ min);

/*
//Previous version success criteria
function resultsFromQuestRandom (
  randVal, greatSuccess, fail, badFail, greatSuccessNode, successNode, failNode, badFailNode
  ) 
{
    if (randVal>greatsuccess) return greatSuccessNode
    else if (randVal>fail) return successNode
    else if (randVal>badFail) return failNode
    else return badFailNode
}
*/
function pullQuest()
  {
  }
