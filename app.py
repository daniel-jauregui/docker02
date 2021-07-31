from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
    <head>
    <title>Docker HW2</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/momentjs/2.14.1/moment.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.37/js/bootstrap-datetimepicker.min.js"></script>
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.37/css/bootstrap-datetimepicker.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

</head>
<body>
    <table>
        <tr>
            <td>
                <div class="card-body" align="left">
                    <p class="lead"><b>The rule of three</b></p>
                    <div class="card" style="width: 100%;">
                        <div class="card-body">
                            <input name="n1r3p" id="n1r3p" type="text" onchange="r3pOnChange();"> 
                            <input name="n2r3p" type="text"
                                                                                                         disabled
                                                                                                         value="100%" size="10"><br>
                            <input name="n3r3p" id="n3r3p" type="text" onchange="r3pOnChange();"> <input name="n4r3p" id="n4r3p"
                                                                                                         type="text"
                                                                                                         disabled value="0%"
                                                                                                         size="10">
                            <div id="errorR3P" style="color: red"></div>
                            <script>
                                function r3pOnChange() {
                                    var n1r3p = document.getElementById('n1r3p').value;
                                    var n3r3p = document.getElementById('n3r3p').value;
                                    if (n1r3p != "" && n3r3p != "") {
                                        if (isNaN(n1r3p) || isNaN(n3r3p)) {
                                            document.getElementById('errorR3P').innerHTML = "String are not allowed!, please use numbers.";
                                            document.getElementById('n4r3p').value = "Error!";
                                        } else {
                                            document.getElementById('errorR3P').innerHTML = "";
                                            document.getElementById('n4r3p').value = round(((n3r3p / n1r3p) * 100), 1) + '%';
                                        }
                                    }
                                }
                            </script>
                        </div>
                        <br>
                        <hr style="margin-top: 5px; margin-bottom: 5px">
                        <br>
                        <div class="card-body">
                            <input name="n1r3v" id="n1r3v" type="text" onchange="r3vOnChange();"> <input name="n2r3v" type="text"
                                                                                                         disabled value="100%"
                                                                                                         size="10"><br>
                            <input name="n3r3v" id="n3r3v" disabled type="text" value="0"> <input name="n4r3v" id="n4r3v"
                                                                                                  type="text"
                                                                                                  onchange="r3vOnChange();"
                                                                                                  size="10">%
                            <div id="errorR3V" style="color: red"></div>
                            <script>
                                function r3vOnChange() {
                                    var n1r3v = document.getElementById('n1r3v').value;
                                    var n4r3v = document.getElementById('n4r3v').value;
                                    if (n1r3v != "" && n4r3v != "") {
                                        if (isNaN(n1r3v) || isNaN(n4r3v)) {
                                            document.getElementById('errorR3V').innerHTML = "String are not allowed!, please use numbers.";
                                            document.getElementById('n3r3v').value = "Error!";
                                        } else {
                                            document.getElementById('errorR3V').innerHTML = "";
                                            document.getElementById('n3r3v').value = round(((n4r3v * n1r3v) / 100), 1);
                                        }
                                    }
                                }

                                function round(value, precision) {
                                    var multiplier = Math.pow(10, precision || 0);
                                    return Math.round(value * multiplier) / multiplier;
                                }
                            </script>
                        </div>
                    </div>
                </div>
            </td>    
        </tr>
            </table>
</body>
</html>'''

if __name__ == "__main__":
    app.run()
