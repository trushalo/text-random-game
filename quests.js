let questArray=[

]




//functions built for use

function randomIntFromInterval(min,max) {
    return Math.floor(Math.random() * (max- min + 1)+ min);

function resultsFromQuestRandom (
  randVal, greatSuccess, fail, badFail, greatSuccessNode, successNode, failNode, badFailNode
  ) 
{
    if (randVal>greatsuccess) return greatSuccessNode
    else if (randVal>fail) return successNode
    else if (randVal>badFail) return failNode
    else return badFailNode
}

function pullQuest()
  {
  }


