
function validateAnswer(input_answer, answerTrue) {
	if((input_answer.value == "") || (input_answer.value == null)) {
		let btn = document.getElementById("id_next");
		btn.click();
	} else {
		if(input_answer.value == answerTrue) {
			let btn = document.getElementById("id_next");
			btn.click();
		} else {
			let div_error = document.getElementById("div_error");
			div_error.style.display = "block";
			input_answer.style.boxShadow = "0px 0px 3px 1px rgba(255, 0, 0, 0.65)";
		}
	}
}

function restore_error(id_div) {
	let div_error = document.getElementById("div_error");
	if(div_error.style.display == "block") {
		let in_answ = document.getElementById(id_div);
		div_error.style.display = "none";
		in_answ.style.boxShadow = "none";
	}
}

