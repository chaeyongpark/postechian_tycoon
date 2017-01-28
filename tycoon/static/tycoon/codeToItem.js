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

var do_animation = function(index, item_img) {
	if (index == 0) {
		$("img#code_to_item_box").attr("src", "/static/tycoon/code_to_item_box/01_new_box.png");
		setTimeout(function() { do_animation(1, item_img) }, 500);
	}
	else if (1 <= index && index < 14) {
		$("img#code_to_item_box").attr("src", "/static/tycoon/code_to_item_box/" + (index < 10 ? "0" : "") + index + "_new_box.png");
		setTimeout(function() { do_animation(index + 1, item_img) }, 75);
	}
	else if (index == 14) {
		$("img#code_to_item_box").attr("src", "/static/tycoon/code_to_item_box/14_new_box.png");
		$("img#code_to_item_box").animate({
			opacity: 0
		}, 1000, function() {
			$("img#code_to_item_box").attr("src", item_img);
			$("img#code_to_item_box").animate({
				opacity: 100
			}, 5000, function() {
				$("form#codeToItemForm :input").prop("disabled", false);
			});
		});
	}
}

$("form#codeToItemForm").submit(function (e) {
	e.preventDefault();

	$("form#codeToItemForm :input").prop("disabled", true);

	$.ajax({
		method: "POST",
		url: "/codeToItem",
		data: { codeToItem: $("input#codeToItem").val() },
	}).done(function(data) {
		do_animation(0, data.item_img);
	});
});