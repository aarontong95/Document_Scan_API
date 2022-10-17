import flask
from flask import request, jsonify
from document_scan import scan

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/Scan', methods=['POST'])
def api_nude_detect():
    """

    Call the docker nudenet service to calculate the score of the safety of the url pic.
    testing_url: http://127.0.0.1:5000/NudeDetect?url=https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png

    Args:
        url_pic(str) : url of the picture
        version(int) : model's version
    Returns:
        json:
            {‘success’ : boolean, ‘reason’/‘score’ : str/float}
        Example:
            When success == True:
                return: {‘success’ : True, ‘score’ : 0.85}
            When success == False:
                return: {‘success’ : False, ‘reason’ : ‘Can not recognize the image’}

    """
    result = scan(request.values.get('image'))

    print('result :', result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8887)
