from website import app


@app.route('/')
def hello():

    return """<h1 style="color:rgb(4, 135, 191);">Bonjour et bienvenue</h1>
    <h1 style="color:rgb(4, 104, 181);">sur le site officiel des Vancraeyvelds</h1>
    <h2 style="color:rgb(4, 81, 181);">ceci sont les membres de la famille:</h2>
    <ul>
             <h4 style="color:rgb(255, 3, 141);"><li>Julia Vancraeyveld</li>
             <h4 style="color:rgb(214, 2, 140);"><li>Saartje Vancraeyveld</li></h4>
             <h4 style="color:rgb(189, 4, 149);"><li>Michiel Vancraeyveld</li></h4>
             <h4 style="color:rgb(186, 4, 189);"><li>Pieter Vancraeyveld</li></h4>
             <h4 style="color:rgb(142, 4, 189);"><li>Frank Vancraeyveld</li></h4>
             <h4 style="color:rgb(102, 4, 189);"><li>Florent Vancraeyveld</li></h4>
             <h4 style="color:rgb(75, 4, 189);"><li>Leon Vancraeyveld</li></h4>
    </ul>  
    <h2 style="color:rgb(5, 8, 171);">Notre famille est connu pour notre don de pété non-stop :)</h2> """ 

    