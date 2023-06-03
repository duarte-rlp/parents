
function validateAnswer(input_answer, answerTrue) {
	if((input_answer.value == "") || (input_answer.value == null)) {
		let btn = document.getElementById("id_next");
		btn.removeAttribute("disabled");
		btn.click();
		btn.setAttribute("disabled", true);
	} else {
		if(input_answer.value == answerTrue) {
			let btn = document.getElementById("id_next");
			btn.removeAttribute("disabled");
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

window.onload = function(){
	
	// Usar para agregar punto de miles
	let elements = document.getElementsByTagName("toNumber");
	for(let j=0; j<elements.length; j++) {
		let num = Number(elements[j].innerHTML);
		elements[j].innerHTML = num.toLocaleString('es-CO').toString();
	}

	// Agregar el enter para los inputs de números
	let in_elements = document.getElementsByClassName("inNumber");
	if(in_elements.length > 0) {
		for(let i=0; i<in_elements.length; i++) {
			in_elements[i].addEventListener("keypress", function(event) {
				if (event.key === "Enter") {
					event.preventDefault();
					validate();
				}
			}
		)}
	}
};

