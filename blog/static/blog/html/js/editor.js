
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

		let result = await pyodide.runPythonAsync(editor.getValue());

		console.log(result);

		addToOutput(result);
		
	} catch (err) {
		addToOutput(err);
	}
}