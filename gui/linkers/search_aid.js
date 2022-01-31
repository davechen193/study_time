const { clipboard } = require('electron')
const keyCodes = {
  V: 86,
}
document.onkeydown = function(event){
  let toReturn = true
  if(event.ctrlKey || event.metaKey){  // detect ctrl or cmd
    if(event.which == keyCodes.V){
      document.activeElement.value += clipboard.readText()
      document.activeElement.dispatchEvent(new Event('input'))
      toReturn = false
    }
  }

  return toReturn
}
function render(){
  input_text = document.getElementById("input").value;
  document.getElementById("result").innerHTML = "";
  const { spawn } = require('child_process');
  const proc = spawn('/usr/local/bin/python3', [__dirname + '/linkers/search_aid.py', input_text]);
  proc.stdout.on('data', (data) => {
    document.getElementById("result").style.fontSize = "medium";
    document.getElementById("result").innerHTML= document.getElementById("result").innerHTML + data.toString();
  });
  proc.stderr.on('data', (data) => {
    document.getElementById("result").innerHTML= data.toString();
  });
}