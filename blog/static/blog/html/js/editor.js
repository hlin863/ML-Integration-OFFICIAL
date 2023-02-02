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
	let pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/" });
	// Pyodide ready
	output.value += "Ready!\n";
	return pyodide;
};

let pyodideReadyPromise = main();

function addToOutput(s) {
	output.value += ">>>" + s + "\n";
}

async function evaluatePython() {
	let pyodide = await pyodideReadyPromise;
	try {
		console.log(editor.getValue())

		// split editor value into lines
		let lines = editor.getValue().split("\n");

		console.log(lines.length);

		// iterate through the lines and print each line
		for (let i = 0; i < lines.length; i++) {
			console.log(i);
			console.log(lines[i]);
		}

		// determine if the instruction is a print statement
		if (lines[0].includes("print")) {
			// if it is, remove the print statement
			lines[0] = lines[0].replace("print", "");
			console.log(lines[0]);
			// set the output to the result of the print statement
			addToOutput(lines[0]);
		} else {
			let output = pyodide.runPython(lines[0]);
			addToOutput(output);
		}

		
	} catch (err) {
		addToOutput(err);
	}
}