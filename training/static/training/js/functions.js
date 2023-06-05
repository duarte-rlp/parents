        
        $(document).ready(function () {
            $('input[id=sliderDinero]').on('input change', function () {
                $('input[id=sliderDinero]').addClass('myclass');
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

        function numberWithPoints(x) {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }

$(document).ready(function () {
    // Usar para agregar punto de miles
    let elements = document.getElementsByTagName("toMoney");
    for(let j=0; j<elements.length; j++) {
        let num = Number(elements[j].innerHTML);
        console.log('num', num);
        if (num < 0) {
            num = num * -1;
            elements[j].innerHTML = "-$" + num.toLocaleString('es-CO').toString();
        }else {
            elements[j].innerHTML = "$" + num.toLocaleString('es-CO').toString();
        }
    }
});
