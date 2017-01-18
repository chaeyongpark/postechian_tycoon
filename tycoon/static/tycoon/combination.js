var left = false, right = false;

var itemEventHandler = function(e) {
	if (left == false) {
		var temp = $(this);
		$(this).parent().remove();
		$("#item-left img").replaceWith(temp);
		left = true;
	}
	else if (right == false) {
		var temp = $(this);
		$(this).parent().remove();
		$("#item-right img").replaceWith(temp);
		right = true;
	}
}

$(".item img").bind("click", itemEventHandler);

$("#item-left").bind("click", function(e) {
	if (left == true) {
		var temp = $("<div class='col-xs-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		left = false;
	}
});

$("#item-right").bind("click", function(e) {
	if (right == true) {
		var temp = $("<div class='col-xs-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		right = false;
	}
});