from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/careers')
def careers ():
    return render_template('careers.html')

@app.route('/webmail')
def login():
    return redirect("https://p3plzcpnl505166.prod.phx3.secureserver.net:2096/cpsess2752899820/3rdparty/roundcube/?_task=mail&_mbox=INBOX", code=302)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
