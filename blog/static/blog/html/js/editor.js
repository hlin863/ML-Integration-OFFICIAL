
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

jQuery("input#upload").change(
	function handleFileSelect(evt) {
		let files = evt.target.files; // FileList object
	
		// use the 1st file from the list
		let f = files[0];

		console.log(f.name);
		
		let reader = new FileReader();
	
		// Closure to capture the file information.
		reader.onload = (function(theFile) {
			return function(e) {
			  jQuery( '#code' ).val( e.target.result );
			};
		  })(f);
	
		  // Read in the image file as a data URL.
		reader.readAsText(f);
	
		document.getElementById('upload').addEventListener('change', handleFileSelect, false);
	}
);
