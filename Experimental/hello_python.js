// hello_python.js
const { loadPyodide } = require("pyodide");

async function hello_python() {
  let pyodide = await loadPyodide();
  return pyodide.runPythonAsync("print(\"Hello World!\""); // change to a print statement to see the output
}

hello_python().then((result) => {
  //console.log("Python says that 1+1 =", result);
  console.log("Python says that Hello World!");
});