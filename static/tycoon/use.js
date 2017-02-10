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

$("div.item img").bind("click", function(e) {
	var name = $(this).attr("name");
	var strength = $(this).attr("strength");
	var intelligence = $(this).attr("intelligence");
	var charm = $(this).attr("charm");
	var surplus = $(this).attr("surplus");
	var luck = $(this).attr("luck");

	var contains = $(this).attr("contains");

	strength = strength == 0 ? "" : " 체력: " + (strength > 0 ? "+" : "") + strength;
	intelligence = intelligence == 0 ? "" : " 지력: " + (intelligence > 0 ? "+" : "") + intelligence;
	charm = charm == 0 ? "" : " 매력: " + (charm > 0 ? "+" : "") + charm;
	surplus = surplus == 0 ? "" : " 잉여력: " + (surplus > 0 ? "+" : "") + surplus;
	luck = luck == 0 ? "" : " 운: " + (luck > 0 ? "+" : "") + luck;

	var use = confirm(name + ": 이 아이템을 사용하시겠습니까?\n\n" +
		"효과:" + strength + intelligence + charm + surplus + luck);

	if (use) {
		$.ajax({
			method: "POST",
			url: "/use/",
			data: { contains_id: contains },
		}).done(function() {
			location.reload();
		});
	}
});