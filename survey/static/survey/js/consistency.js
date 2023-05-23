$(document).ready(function () {
    $('.items1').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items1');
            var i_clicked = -1;

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A' && radio === clickedRadio) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B' && i_clicked != (i-1)) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    i_clicked = i;
                    continue;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items2').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items2');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if(clickedRadio.value === 'B'){
                    if (!afterClickedRadio && radio.value === 'B') {
                        radio.checked = true;
                    }
                    if (afterClickedRadio && radio.value === 'A') {
                        radio.checked = true;
                    }
                    if (radio === clickedRadio) {
                        afterClickedRadio = true;
                        i_clicked = i;
                        continue;
                    }
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items3').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items3');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if(clickedRadio.value === 'B'){
                    if (!afterClickedRadio && radio.value === 'B') {
                        radio.checked = true;
                    }
                    if (afterClickedRadio && radio.value === 'A') {
                        radio.checked = true;
                    }
                    if (radio === clickedRadio) {
                        afterClickedRadio = true;
                        i_clicked = i;
                        continue;
                    }
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.slider_efficacy').change(
        function (event) {
            var slider_id = event.target.id;
            var slider_input = document.getElementById(slider_id);
            var efficacy_score = document.getElementById('efficacy_score');
            var check_sli = document.getElementById('id_check_slider_educsup');

            var slider_value = slider_input.value;

            efficacy_score.innerHTML = numberWithPoints(slider_value);
            check_sli.value = 1;

            var next_button = document.getElementsByClassName('otree-btn-next');
            next_button[0].style.cssText += 'display: block !important;';
        }
    );
});

$(document).ready(function () {
    $('.multislider_efficacy').change(
        function (event) {
            var slider_id = event.target.id;
            var slider_input_value = document.getElementById(slider_id).value;
            var efficacy_score = document.getElementById(slider_id).parentElement.parentElement.parentElement.children[0].children[1].children[0];
            var check_sli = document.getElementById(slider_id).parentElement.children[1];

            efficacy_score.innerHTML = numberWithPoints(slider_input_value);
            check_sli.value = 1;
        }
    );
});

$(document).ready(function () {
    $('.multislider_money').change(
        function (event) {
            var slider_id = event.target.id;
            var slider_input_value = document.getElementById(slider_id).value;
            var money_score = document.getElementById(slider_id).parentElement.parentElement.parentElement.children[0].children[1].children[0];
            var check_sli = document.getElementById(slider_id).parentElement.children[1];

            money_score.innerHTML = "$ " + numberWithPoints(slider_input_value);
            check_sli.value = 1;
        }
    );
});

$(document).ready(function () {
    $('input[class=multislider_efficacy]').on('input change', function (event) {
        var slider_id = event.target.id;
        $('input[id='+slider_id).addClass('myclass');
    });
});

$(document).ready(function () {
    $('input[class=multislider_money]').on('input change', function (event) {
        var slider_id = event.target.id;
        $('input[id='+slider_id).addClass('myclass');
    });
});

$(document).ready(function () {
    $('.slider_tiempo').change(
        function (event) {
            var slider_id = event.target.id;
            var parent_slider = document.getElementById(slider_id).parentElement.parentElement;
            var childs = parent_slider.children;

            var dinero_pa = childs[0].firstElementChild;
            var slider_max = childs[1].firstElementChild.max;
            var slider_value = childs[1].firstElementChild.value;
            var dinero_pb = childs[2].firstElementChild;

            var check_sli = childs[1].lastElementChild;

            dinero_pa.innerHTML = "Horas: "+slider_value;
            dinero_pb.innerHTML = "Horas: "+(slider_max-slider_value);
            check_sli.value = 1;

            var next_button = document.getElementsByClassName('otree-btn-next');
            next_button[0].style.cssText += 'display: block !important;';
        }
    );
});

function numberWithPoints(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

$(document).ready(function () {
    $('.otree-btn-next').click(
        function () {
            var radios = $('.items1');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
            var radios = $('.items2');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
            var radios = $('.items3');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
        }
    );
});


document.getElementById("_study").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });

        document.getElementById("_militar").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });

        document.getElementById("_worker").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });

        document.getElementById("_selfemployed").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });

        document.getElementById("_nonwage").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });

        document.getElementById("_nini").addEventListener("change", function() {
            let v = parseInt(this.value);
            if (v < 0) this.value = 0;
            if (v > 100) this.value = 100;
            var all_inputs = document.getElementsByClassName('input_number');
            var sum_prob = Number(0);
            for(const i of all_inputs) {
                sum_prob = Number(sum_prob) + Number(i.value);
            }
            var html_sum_prob = document.getElementById("sum_prob");
            html_sum_prob.innerHTML = sum_prob;
            if(sum_prob == 100) {
                html_sum_prob.style.color = "green";
            } else {
                html_sum_prob.style.color = "red";
            }
        });


function enviar(){
    formulario = document.getElementById("form");
    var html_sum_prob = document.getElementById("sum_prob");
    if(Number(document.getElementById("sum_prob").innerHTML) == 100) {
        formulario.submit();
    } else {
        alert('La suma de las probabilidades no da 100, por favor revise');
    }
}




