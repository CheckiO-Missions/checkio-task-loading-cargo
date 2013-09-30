//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            var checkioInput = data.in;

            if (data.error) {
                $content.find('.call').html('Fail: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.output').html(data.error.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
                return false;
            }

            var rightResult = data.ext["answer"];
            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));

            if (!result) {
                $content.find('.call').html('Fail: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult));
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.answer').remove();
            }
            //Dont change the code before it

            var max_weight = Math.max.apply(Math, checkioInput);
            var min_weight = Math.min.apply(Math, checkioInput);
            var diff_weight = max_weight - min_weight;
            if (diff_weight === 0) {
                min_weight = min_weight / 2;
                diff_weight = max_weight;
            }

            var left_part = data.ext["explanation"][0];
            var right_part = data.ext["explanation"][1];
            var diff_part = rightResult;

            var $explanation = $content.find(".explanation");
            $explanation.find("#diff-part").html(diff_part);

            var $left_numbers = $explanation.find(".left-part").find(".numbers");
            var $right_numbers = $explanation.find(".right-part").find(".numbers");

            var weight_list_create = function(part, $part_numbers) {
                for (i in part){
                    var sp = $("<span>");
                    sp.text(part[i] + '  ');
                    sp.css("font-size", ((((part[i] - min_weight) / diff_weight) * 10) + 12));
                    $part_numbers.append(sp);
                }
            };

            weight_list_create(left_part, $left_numbers);
            weight_list_create(right_part, $right_numbers);


            this_e.setAnimationHeight($content.height() + 60);

        });

        var $tryit;

        ext.set_console_process_ret(function(this_e, ret){
            $tryit.find('.checkio-result-in').html("Checkio return: " + ret);
        });

        ext.set_generate_animation_panel(function(this_e){

            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit')));
            var weights = [];

            $tryit.find('.input-text').focus();

            $tryit.find("form .bn-reset").click(function(e){
                weights = [];
                $tryit.find(".batteries").html(weights.join(", "));
                $tryit.find(".input-text").val('');
            });

//            $tryit.find('form').submit(function(e){
//                console.log("IN FORM");
//                return false;
//            });

//            $tryit.find("form .bn-check").click(function(e){
            $tryit.find('form').submit(function(e){
                var new_weights = $tryit.find(".input-text").val().match(/(\d+)/g);
                if (new_weights !== null) {
                    for (var i=0; i < new_weights.length; i++){
                        weights.push(parseInt(new_weights[i]));
                    }
                }
                $tryit.find(".batteries").html(weights.join(", "));
                $tryit.find(".input-text").val('');
                this_e.sendToConsoleCheckiO(weights);
                e.stopPropagation();
                return false;
             });

        });

        var colorOrange4 = "#F0801A";
        var colorOrange3 = "#FA8F00";
        var colorOrange2 = "#FAA600";
        var colorOrange1 = "#FABA00";

        var colorBlue4 = "#294270";
        var colorBlue3 = "#006CA9";
        var colorBlue2 = "#65A1CF";
        var colorBlue1 = "#8FC7ED";

        var colorGrey4 = "#737370";
        var colorGrey3 = "#9D9E9E";
        var colorGrey2 = "#C5C6C6";
        var colorGrey1 = "#EBEDED";

        var colorWhite = "#FFFFFF";
        //Your Additional functions or objects inside scope
        //
        //
        //


    }
);
