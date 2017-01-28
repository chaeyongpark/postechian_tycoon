// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

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

	if (left && right) {
		var left_contains = $("#item-left").children().first().attr("contains");
		var right_contains = $("#item-right").children().first().attr("contains");
		$.ajax({
			method: "POST",
			url: "/combination/",
			data: { left: left_contains, right: right_contains },
		}).done(function(data) {
			if (data.nitem.id == 0) {
			}
			else {
				$('img#item-combined').replaceWith("<img id='item-combined' src='"+data.nitem.url+"' class='img-responsive img-rounded'>");
			}
		});
	}
}

$(".item img").bind("click", itemEventHandler);

$("#item-left").bind("click", function(e) {
	if (left == true) {
		var temp = $("<div class='col-xs-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		left = false;

		$('img#item-combined').replaceWith("<img id='item-combined' src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
	}
});

$("#item-right").bind("click", function(e) {
	if (right == true) {
		var temp = $("<div class='col-xs-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		right = false;

		$('img#item-combined').replaceWith("<img id='item-combined' src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
	}
});
