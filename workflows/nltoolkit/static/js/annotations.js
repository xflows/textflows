

$(document).ready(function () {
    $("#DocumentText").html(htmlText);
    var text=$("#DocumentText").text();

    $('input[name="annotationTypeList"]').click(function () {
        refreshPage(text);
    });

    function refreshPage(text) {

        var elements;

        var colorArray = new Array();
        var color;

        var featureArray = new Array();

        $("input:checked").each(function () {

            elements = $(this).attr("elements");
            color = $(this).parent().next().attr('bgcolor');

            //update colorArray and featureArray
            var tmp = elements.split(':');
            for (var i = 0; i < tmp.length - 1; i++) {
                var tmp2 = tmp[i].split(',');
                var annLength = parseInt(tmp2[1]) - parseInt(tmp2[0]);

                for (var j = 0; j < annLength + 1; j++) {
                    colorArray[parseInt(tmp2[0]) + j] = color;
                    featureArray[parseInt(tmp2[0]) + j] = tmp2[2]
                }
            }

        });


        var i;

        var htmlResult = htmlEncode(text);

        if (colorArray.length > 0) {
            htmlResult = "";
            if (colorArray[0] != undefined) {
                if (featureArray[0] == undefined || featureArray[0] == "") {
                    htmlResult += "<span style='background-color:" + colorArray[0] + "; border: 2px solid white;'>";
                }
                else {
                    htmlResult += "<span style='background-color:" + colorArray[0] + ";' class='text' title='Features: <br/>" + featureArray[0] + "'>";
                }
            }
            htmlResult += htmlEncode(text.charAt(0));

            for (i = 0; i < text.length - 1; i++) {
                if (colorArray[i] != colorArray[i + 1] || featureArray[i] != featureArray[i + 1]) {
                    if (colorArray[i] != undefined) {
                        htmlResult += "</span>";
                    }
                    if (colorArray[i + 1] != undefined) {
                        if (featureArray[i + 1] == undefined || featureArray[i + 1] == "") {
                            htmlResult += "<span style='background-color:" + colorArray[i + 1] + "; border: 2px solid white;'>";
                        }
                        else {
                            htmlResult += "<span style='background-color:" + colorArray[i + 1] + ";' class='text' title='Features: <br/>" + featureArray[i + 1] + "'>";
                            console.log(featureArray[i + 1].replace("u'","").replace('\'',""));
                        }
                    }
                    htmlResult += htmlEncode(text.charAt(i + 1));
                }
                else {
                    htmlResult += htmlEncode(text.charAt(i + 1));
                }
                if (i == text.length - 1 && colorArray[i + 1] != undefined) {
                    htmlResult += "</span>";
                }
            }

        }


        $("#DocumentText")[0].innerHTML =  htmlResult;

        $('span').tipsy({
             gravity: 's',
            // use the built-in fadeIn/fadeOut effect
            effect: "fade",
            // custom opacity setting
            opacity: 0.95,
            //enable html to display break lines
            html: true

        });


    }

});
function htmlEncode(str) {
    return String(str).replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}