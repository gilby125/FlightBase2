$(document).ready(function() {

	$(".clickable-row").click(function() {

		var link = $(this).data('href');
    	window.open(link, '_blank');

  	});
});