        
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