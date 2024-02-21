        
        $(document).ready(function () {
            $('input[id=sliderDinero]').on('input change', function () {
                $('input[id=sliderDinero]').addClass('myclass');
            });
        });

        function numberWithPoints(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }

$(document).ready(function () {
    // Usar para agregar punto de miles
	let elements = document.getElementsByTagName("toNumber");
	for(let j=0; j<elements.length; j++) {
		let num = Number(elements[j].innerHTML);
		elements[j].innerHTML = num.toLocaleString('pt-BR').toString();
	}

	// Usar para agregar punto de miles y el símbolo de pesos
	let mon_elements = document.getElementsByTagName("toMoney");
        for(let j=0; j<mon_elements.length; j++) {
            let num = Number(mon_elements[j].innerHTML);
            if (num < 0) {
                num = num * -1;
                mon_elements[j].innerHTML = "- R$ " + num.toLocaleString('pt-BR').toString();
            }else {
                mon_elements[j].innerHTML = "R$ " + num.toLocaleString('pt-BR').toString();
            }
        }

	// Agregar el enter para los inputs de números
	let in_elements = document.getElementsByClassName("inNumber");
	if(in_elements.length > 0) {
		for(let i=0; i<in_elements.length; i++) {
			in_elements[i].addEventListener("keypress", function(event) {
				if ((event.key === "Enter") || (event.which == 13)) {
					event.preventDefault();
				}
			}
		)}
	}
});
