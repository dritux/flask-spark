from . import app


@app.route('/next')
def next_route():
    return "ohh yes"
