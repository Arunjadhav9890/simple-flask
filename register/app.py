from flask import Flask, request, redirect, url_for, session, Response

# Import necessary modules from Flask
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = "supersecretkey"

# Create a simple login page with Flask
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123':
            session['user'] = username
            return redirect(url_for('welcome')) 
        else:
            return Response("Invalid credentials", mimetype='text/plain')
    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f'''
        <h2>Welcome {session['user']}!</h2>
        <a href={url_for('logout')}>Logout</a>
        '''
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)