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
			data: { real: false, left: left_contains, right: right_contains },
		}).done(function(data) {
			if (data.nitem.id == 0) {
			}
			else if(data.before) {
				$('img#item-combined').replaceWith("<img combined='true' id='item-combined' src='"+data.nitem.url+"' class='img-responsive img-rounded'>");
				$('#text_name').val(data.nitem.explanation);
			}
			else {
				$('img#item-combined').replaceWith("<img combined='false' id='item-combined' src='/static/tycoon/question.png' class='img-responsive img-rounded'>");
				$('img#item-combined').bind("click", function() {
					$(this).animate({
							opacity: 0
						}, 1000, function() {
							$(this).attr("src", data.nitem.url);
							$(this).attr("combined", 'true');
							$(this).animate({
								opacity: 100
							}, 1000, function() {
								alert("축하합니다! 다음 조합법을 발견하였습니다!\n" +
									$("#item-left").children().first().attr("alt") + " + " +
									$("#item-right").children().first().attr("alt") + " = " + data.nitem.name);
								$('#text_name').val(data.nitem.explanation);
							});
					});
				});
			}
		});
	}
}

$(".item img").bind("click", itemEventHandler);

$("#item-left").bind("click", function(e) {
	if (left == true) {
		var temp = $("<div class='col-xs-6 col-sm-4 col-lg-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		left = false;

		$('img#item-combined').replaceWith("<img combined='false' id='item-combined' src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		$('#text_name').val('');
	}
});

$("#item-right").bind("click", function(e) {
	if (right == true) {
		var temp = $("<div class='col-xs-6 col-sm-4 col-lg-3 item'>").append($(this).children().first());
		$(this).children().first().remove();
		$(this).append("<img src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		temp.children().first().bind("click", itemEventHandler)
		$("#item_basket").prepend(temp);
		right = false;

		$('img#item-combined').replaceWith("<img combined='false' id='item-combined' src='/static/tycoon/white.png' class='img-responsive img-rounded'>");
		$('#text_name').val('');
	}
});

$("button#combine").bind("click", function(e) {
	var combined = $("img#item-combined").attr("combined");
	var left_contains = $("#item-left").children().first().attr("contains");
	var right_contains = $("#item-right").children().first().attr("contains");
	
	if(combined) {
		$.ajax({
			method: "POST",
			url: "/combination/",
			data: { real: true, left: left_contains, right: right_contains },
		}).done(function(data) {
			location.reload();
		});
	}
});
