$(document).ready(function() {
	$('#submit').on('click', submit_burger);
    console.log("ready");
});

const submit_burger = async() => {
	$('#submit').prop('disabled', true);

	// prepare alert
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.text("The grillmaster is evaluating your recipe. Please wait....");
	card.show();

	// validate
	let title = $("#title").val();
	let comments = $("#comments").val();

    let ingredients = [];
    $(".ingredient").each(function() {
        if ($(this).prop('checked')) {      
        ingredients.push($(this).val());
        }
    });

	if ($.trim(title) === '') {
		$('#submit').prop('disabled', false);
		card.text("Please enter a title for your burger!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	} else if (ingredients.length == 0) {
		$('#submit').prop('disabled', false);
		card.text("You must select some ingredients for your burger!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	}

	await fetch(`/submission`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({title: title, recipe: ingredients, comments: comments}),
		})
		.then((response) => response.json()
			.then((resp) => {
				card.attr("class", "alert alert-danger");
				if (response.status == 200) {
					card.attr("class", "alert alert-info");
					card.text(resp.message);
					card.show();
					return;
				}
				card.text(resp.message);
				card.show();
			}).catch((error) => {
				card.text("An error occurred, if this continues please alert an admin.");
				card.attr("class", "alert alert-danger");
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

		$('#submit').prop('disabled', false);
}