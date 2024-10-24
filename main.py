from flask import Flask, render_template
from requests import get
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)

@app.route('/')
def index():
    # Example HTTP requests
    results = []
    
    # Simulate HTTP requests (you would replace this with your actual logic)
    response1 = get('https://example.com')
    response2 = get('https://httpbin.org/get')

    # Convert CaseInsensitiveDict to regular dict
    results.append([
        response1.request.method,
        response1.url,
        response1.status_code,
        response1.elapsed.total_seconds(),
        len(response1.content),
        response1.headers.get('Content-Type'),
        dict(response1.headers),  # Convert to a regular dict
        response1.headers.get('Date')
    ])
    
    results.append([
        response2.request.method,
        response2.url,
        response2.status_code,
        response2.elapsed.total_seconds(),
        len(response2.content),
        response2.headers.get('Content-Type'),
        dict(response2.headers),  # Convert to a regular dict
        response2.headers.get('Date')
    ])
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
