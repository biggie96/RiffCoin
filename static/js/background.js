console.log("here");
var xhr = new XMLHttpRequest();
xhr.open("GET", "/requests", true);
xhr.onreadystatechange = function() {
  if (xhr.readyState == 4) {

  }
}
xhr.send();

/*
function tests(testjson){
	data = jQuery.parseJSON(testjson);
	console.log(data.results[0].related_links);
	var i = 0;
	while(i < data.results[0].related_links.length){
		if(data.results[0].related_links[i].category == "Official_Merchandise"){
			var rqst = data.results[0].related_links[i].url;
			var xhr = new XMLHttpRequest();
			var params = "url=" + rqst;
			xhr.open("POST", "/rqst" , true);
			xhr.onreadystatechange = function() {
			  if (xhr.readyState == 4) {
	
			  }
			}
			xhr.send(params);
		}
		i = i + 1;
	}
}
*/