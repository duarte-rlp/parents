        
        $(document).ready(function () {
            $('input[id=sliderDinero]').on('input change', function () {
                $('input[id=sliderDinero]').addClass('myclass');
            });
            $('input[id=slider_porcentaje_01]').on('input change', function () {
                $('input[id=slider_porcentaje_01]').addClass('myclass');
            });
            $('input[id=slider_porcentaje_02]').on('input change', function () {
                $('input[id=slider_porcentaje_02]').addClass('myclass');
            });
        });

        $(document).ready(function () {
            $('.items02').click(
                function (event) {
                    var radio_id = event.target.id;
                    var parent_radio = document.getElementById(radio_id).parentElement;
                    var check_rad = parent_radio.lastElementChild;
                    check_rad.value = 1;
                    validate_next();
                }
            );
        });

        function numberWithPoints(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }

$(document).ready(function () {
    // Usar para agregar punto de miles
    let elements = document.getElementsByTagName("toMoney");
    for(let j=0; j<elements.length; j++) {
        let num = Number(elements[j].innerHTML);
        if (num < 0) {
            num = num * -1;
            elements[j].innerHTML = "- $ " + num.toLocaleString('es-CO').toString();
        }else {
            elements[j].innerHTML = "$ " + num.toLocaleString('es-CO').toString();
        }
    }
});

function restore_error(id_div) {
    let div_error = document.getElementById("div_error");
    if(div_error.style.display == "block") {
        let in_answ = document.getElementById(id_div);
        div_error.style.display = "none";
        in_answ.style.boxShadow = "none";
    }
}

