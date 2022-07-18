$(document).ready(function() {
	$('#login_button').on('click', login);
    console.log("ready");
});

const login = async() => {
	$('#login_button').prop('disabled', true);

	// prepare alert
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.text("Logging in...");
	card.show();

	// validate
	let username = $("#username").val();
	let code = $("#code").val();

	await fetch(`/api/login`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({username: username, code: code}),
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

		$('#login_button').prop('disabled', false);
}