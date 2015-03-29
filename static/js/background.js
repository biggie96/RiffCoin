console.log("here");

getInfo();

function getInfo(){
var xhr = new XMLHttpRequest();
xhr.open("GET", "/randAlbumPrice", true);
xhr.onreadystatechange = function() {


  if (xhr.readyState == 4) {
  		convert(xhr.responseText);
  }
}
xhr.send();
}

function convert(priceJson){
	var price = jQuery.parseJSON(priceJson);
	console.log(price.price);
	console.log(price.name);
	console.log(price.album);

	$("#data").empty();

	$("#data").append("Instead of spending " + price.tRac + " dollars on other stuff......");

	var howMany = price.tRac/price.price;

	$("#data").append("You could have bought " + "<b><u> " + howMany + " </u></b>" + " copies of " + price.album + ", a great album by " + price.name + ".");


}