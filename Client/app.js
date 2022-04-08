//function to estimate house Price
function onClickPredictPrice() {
  //console.log('Predict Price Button Clicked', '\n');

  //get values from inputs and transform them in correct format
  var city = document.getElementById("uiCity").value;
  var floor = parseInt(document.getElementById("uiFloors").value);
  var rooms = parseInt(document.getElementById("uiRooms").value);
  var sq = document.getElementById("uiSq").value;
  var year = parseInt(document.getElementById("uiYear").value);

  var predPrice = document.getElementById("uiPredictPrice");


  // variable to store url
  var url = "http://127.0.0.1:5000/predict_house_price";

  //Route 5000 Port on Nginx conf file
  //location ~ /api/ {
  //rewrite ^/api(.*) $1 break;
  //proxy_pass http://127.0.0.1:5000;
  //}

  //var url = "/api/predict_house_price";


  // use JQuery to make a POST request to server
  $.post(url, {
    city: city,
    floor: floor,
    rooms: rooms,
    sq: sq,
    year: year
  },function(data, status){
    //print output of predict_house_price
    console.log(status);
    console.log(data.predict_price);
    predPrice.innerHTML = "<h2>&euro; " + data.predict_price.toString() + " </h2>";
  });



}
