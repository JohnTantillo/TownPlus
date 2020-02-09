
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
  var a = JSON.parse (array)["lot"];
  console.log(a);
  var table = document.getElementById("myTable");
  for (var i = 0; i < a.length; i++){
    console.log(a.length);
    var row = table.insertRow(i);
    for (var j = 0; j <a[i].length; j++){
      var cell1 = row.insertCell(j);
      if (a[i][j] == "1"){
        console.log("run");
         cell1.innerHTML = '<img src="car.jpg" width="120" height="234">';
      }
      else{
          cell1.innerHTML = '<img src="empty.png" width="120" height="234">';
      }
    }
  }

}
