
function onLoad() {
  ajaxGetRequest("/front", myFunction)
}

function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function myFunction(array) {
  var table = document.getElementById("myTable");
  for (var i = 0; i < array.length; i++){
    console.log(array.length);
    var row = table.insertRow(i);
    for (var j = 0; j <array[i].length; j++){
      var cell1 = row.insertCell(j);
      if (array[i][j] == 1){
        console.log("run");
         cell1.innerHTML = '<img src="car.jpg" width="120" height="234">';
      }
      else{
          cell1.innerHTML = '<img src="empty.png" width="120" height="234">';
      }
    }
  }

}
