from flask import Flask, render_template, url_for, redirect, make_response, session

app = Flask(__name__)

@app.route('/')
def top_level():
	return 'youre at the fuckin top'

@app.route('/index/')
def index(name=None):
#	return 'index'
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return render_template('index.html', name=name)

@app.route('/testlate/')
def testlate(name=None):
	return render_template('first_template.html', name=name)

#redirect test
@app.route('/test/')
def test():
	# return redirect(url_for('index'))
	return render_template('test.html')

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

# Note the 404 after the render_template() call.
# This tells Flask that the status code of that page should be 404 which means not found. 
# By default 200 is assumed which translates to: all went well.



#url_for('static', filename='index.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
