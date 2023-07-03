from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {}

@app.route('/', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        users[name] = email
        return redirect('/users')
    return render_template('form.html')


@app.route('/users')
def show_users():
    return render_template('users.html', users=users)

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_user(name):
    if request.method == 'POST':
        new_email = request.form['email']
        users[name] = new_email
        return redirect('/users')
    email = users[name]
    return render_template('edit.html', name=name, email=email)


@app.route('/delete/<name>')
def delete_user(name):
    del users[name]
    return redirect('/users')

if __name__ == '__main__':
    app.run(port=8080)
