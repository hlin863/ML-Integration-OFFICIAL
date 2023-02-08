// const editor = CodeMirror.fromTextArea(document.getElementById("code"), {
// 	mode: {
// 		name: "python",
// 		version: 3,
// 		singleLineStringErrors: false
// 	},
// 	lineNumbers: true,
// 	indentUnit: 4,
// 	matchBrackets: true
// });

document.onkeypress = function autocomplete(){
    var input = editor.getValue();

    console.log(input);

    if (input == "pri"){
        editor.setValue("print(");
        editor.setCursor(0, 6);
    } else if (input == "for"){
        editor.setValue("for i in range(0, )");
        editor.setCursor(0, 19);
    } else if (input == "if"){
        editor.setValue("if ():");
        editor.setCursor(0, 4);
    } else if (input == "def"){
        editor.setValue("def main():");
        editor.setCursor(0, 11);
    } else if (input == "whi"){
        editor.setValue("while ():");
        editor.setCursor(0, 8);
    }
}