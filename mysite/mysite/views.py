"""

Render the html template index.html with the data in the context variable.

"""
from django.http import HttpResponse

HTML_CODE = """

    <!DOCTYPE html>
    <html lang="en-gb">
    <head>
        <script href="style.css" rel="stylesheet"></script>
    </head>
    <body>

    <!-- Image and text -->
    <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
        <img src="Images/Icons/build-icon.png" h="30" height="30" class="d-inline-block align-top" alt="">
        <a href="Build/build.html" >Build</a>
        </a>
        <a class="navbar-brand" href="#">
            <img src="Images/Icons/test-icon.png" width="30" height="30" class="d-inline-block align-top" alt="">
            Test
        </a>
        <a class="navbar-brand" href="#">
            <img src="Images/Icons/reset-icon.png" width="30" height="30" class="d-inline-block align-top" alt="">
            Reset
        </a>
    </nav>

    <!-- Provide a section that outlines the project -->
    <div class = "ContinuousIntegrationContext" id = "ContinuousIntegrationContext">
        <h1>Continuous Integration Context</h1>
        <p>
            Continuous Integration has played a vital role in building and integrating new applications over time. In the current project, the goal is to apply automated process to validate the software updates and build some sample Machine Learning Code as sample inputs.
            <br>
            The app provides a platform to run the ML CI code and validate the results.
        </p>
    </div>

    <!-- Gallery providing an outline for the CI System structure. -->
    <div class="row">
    <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
        <img
        src="Images/Cover_Page/A-macroscopic-view-of-where-a-CI-CD-service-stands-in-modern-ML-application-development_W640.jpg"
        class="w-100 shadow-1-strong rounded mb-4"
        alt="CI Development Process Visualised"
        />
    </div>
    </div>

    <!-- Provide a section that outlines the project -->
    <h1>

        Project Structure Outline.

    </h1>

    <p>

        Our application aim to use PyScript to link the Backend CI System with the Frontend UI. The following paragraph will provide an overview into the existing research done into the CI system. 
        An example file focuses on the wine quality for classifying the different types of wine.
        The file will be available in csv format and will be used to train the model.
        <br>

    </p>

    </body>
    </html>

"""

def home_view(request):
    """
    
    Render the html template index.html with the data in the context variable.

    Input: request (HttpRequest)

    Output: response (html template)

    """
    return HttpResponse(HTML_CODE)