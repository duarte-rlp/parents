        
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

                    dinero_pa.innerHTML = "$ "+numberWithPoints(slider_value);
                    dinero_pb.innerHTML = "$ "+numberWithPoints(slider_max-slider_value);
                    check_sli.value = 1;

                    var next_button = document.getElementsByClassName('otree-btn-next');
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

window.onload = function(){
    // Usar para agregar punto de miles y el símbolo de pesos
    let mon_elements = document.getElementsByTagName("toMoney");
    for(let j=0; j<mon_elements.length; j++) {
        let num = Number(mon_elements[j].innerHTML);
        if (num < 0) {
            num = num * -1;
            mon_elements[j].innerHTML = "- $ " + num.toLocaleString('es-CO').toString();
        }else {
            mon_elements[j].innerHTML = "$ " + num.toLocaleString('es-CO').toString();
        }
    }
};
