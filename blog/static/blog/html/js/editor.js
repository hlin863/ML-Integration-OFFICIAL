
const output = document.getElementById("output");

const editor = CodeMirror.fromTextArea(document.getElementById("code"), {
	mode: {
		name: "python",
		version: 3,
		singleLineStringErrors: false
	},
	lineNumbers: true,
	indentUnit: 4,
	matchBrackets: true
});

editor.setValue(`sum([1, 2, 3, 4, 5])`);
output.value = "Initializing...\n";

async function main() {
	let pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.22.1/full/" });
	// Pyodide ready
	output.value += "Ready!\n";
	return pyodide;
};

// Initialize pyodide ready promise as a global variable
let pyodideReadyPromise = main();

function addToOutput(s) {
	output.value += ">>>" + s + "\n";
}

async function evaluatePython() {

	let pyodide = await pyodideReadyPromise;
	try {

		// split editor value into lines
		let lines = editor.getValue().split("\n");

		// console.log(lines[0]);

		let n_lines = lines.length;

		for (let i = 0; i < n_lines; i++){
			// determine if the instruction is a print statement
			if (lines[i].includes("print")) {
				// if it is, remove the print statement
				lines[i] = lines[i].replace("print", "");

				// replace the brackets with empty strings
				lines[i] = lines[i].replace("(", "");

				lines[i] = lines[i].replace(")", "");

				console.log(lines[i]);

				// replace all quotation marks with empty strings
				lines[i] = lines[i].replace(/"/g, '');

				lines[i] = lines[i].replace(/'/g, '');

				// set the output to the result of the print statement
				addToOutput(lines[i]);
			} else {
				console.log(lines[i]);
				let output = pyodide.runPython(editor.getValue());
				addToOutput(output);
			}
		}
		
	} catch (err) {
		addToOutput(err);
	}
}