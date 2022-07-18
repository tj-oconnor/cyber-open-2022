$(document).ready(function() {
	$('#register_button').on('click', register);
    console.log("ready");
});

const register = async() => {
	$('#register_button').prop('disabled', true);

	// prepare alert
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.text("Sending registration...");
	card.show();

	// validate
	let username = $("#username").val();
	let first_name = $("#first_name").val();
    let last_name = $("#last_name").val();

	await fetch(`/api/register`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({username: username, first_name: first_name, last_name: last_name}),
		})
		.then((response) => response.json()
			.then((resp) => {
				card.attr("class", "alert alert-danger");
				if (response.status == 200) {
					card.attr("class", "alert alert-info");
					card.text(resp.message);
					card.show();
                    window.location = "/dashboard";
				}
				card.text(resp.message);
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

		$('#register_button').prop('disabled', false);
}