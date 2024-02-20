        
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
            $('.slider_dinero').change(
                function (event) {
                    var slider_id = event.target.id;
                    var parent_slider = document.getElementById(slider_id).parentElement.parentElement;
                    var childs = parent_slider.children;

                    var dinero_pa = childs[0];
                    var slider_max = childs[1].firstElementChild.max;
                    var slider_value = childs[1].firstElementChild.value;
                    var dinero_pb = childs[2];

                    var check_sli = childs[1].lastElementChild;

                    dinero_pa.innerHTML = "R$ "+numberWithPoints(slider_value);
                    dinero_pb.innerHTML = "R$ "+numberWithPoints(slider_max-slider_value);
                    check_sli.value = 1;

                    let val_inv_a = document.getElementById("inv_a");
                    let val_inv_b = document.getElementById("inv_b");
                    val_inv_a.innerHTML = "R$"+numberWithPoints(slider_value);
                    val_inv_b.innerHTML = "R$"+numberWithPoints(slider_max-slider_value);

                    var next_button = document.getElementsByClassName('btnNext');
                    next_button[0].style.cssText += 'display: block !important; margin: 0 auto;';
                }
            );
        });

        $(document).ready(function () {
            $('.slider_porcentaje').change(
                function (event) {
                    var slider_id = event.target.id;
                    var slider_value = event.target.value;
                    var parent_slider = document.getElementById(slider_id).parentElement.parentElement.parentElement;
                    console.log('slider id', slider_id);
                    console.log('parent', parent_slider);
                    var child = parent_slider.children[0].children[0].firstElementChild;
                    child.innerHTML = slider_value + "%";
                    var check_sli = parent_slider.children[1].lastElementChild.lastElementChild;
                    check_sli.value = 1;
                    validate_next();
                }
            );
        });

        $(document).ready(function () {
            $('.items01').click(
                function (event) {
                    var radio_id = event.target.id;
                    var parent_radio = document.getElementById(radio_id).parentElement;
                    var check_rad = parent_radio.lastElementChild;
                    check_rad.value = 1;
                    validate_next();
                }
            );
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
            elements[j].innerHTML = "- R$" + num.toLocaleString('pt-BR').toString();
        }else {
            elements[j].innerHTML = "R$" + num.toLocaleString('pt-BR').toString();
        }
    }

    // Evitar el enter con el teclado
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
