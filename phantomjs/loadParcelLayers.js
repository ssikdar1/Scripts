//
// Script to load new parcel files into the Google Cloud and then click the link
//

//What I was inputing into the console manually before.
// var element1 = document.createElement("script");element1.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js";element1.type="text/javascript";document.getElementsByTagName("head")[0].appendChild(element1);
// var foo = $('.p6n-cloudstorage-browser-public-checkbox');
// foo.trigger('click');

var url = 'https://console.developers.google.com/project/660103924069/storage/kml_layers_new/Roads/';
// var url = 'https://www.google.com';

console.log('SSL support = ', require('system').isSSLSupported);
var webPage = require('webpage');
var page = webPage.create();
page.onConsoleMessage = function (msg) {
    console.log(msg);
};

page.onResourceError = function(resourceError) {
    page.reason = resourceError.errorString;
    page.reason_url = resourceError.url;
	console.log("Error opening url \"" + page.reason_url);
	console.log(page.reason);
};
   
page.open(url, function(status) {
	console.log(url)
	console.log('Status: ' + status);
	if(status === 'fail')
	{
		console.log("Terminating Script");
		phantom.exit( 1 );
	}
	else
	{
		console.log(document.getElementById('gaia_loginform'));
	}
	
	
  // page.includeJs("https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {

	// // page.evaluate(function() {
		// // console.log('Hello Moto');
		// // 
		// // //var checkboxes = $('.p6n-cloudstorage-browser-public-checkbox');
		// // //console.log(checkboxes);
		// // // checkboxes.trigger('click');
		// // phantom.exit( 0 );
	// // });
  // });
});

