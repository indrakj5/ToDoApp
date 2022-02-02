
from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from Notesmodel import Notes, db
from app_list import first


# buat Flask app
app = Flask(__name__)
app.register_blueprint(first, url_prefix="/temp")
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db.app = app
db.init_app(app)

db.create_all()

@app.route("/home")
@app.route("/", methods=['GET'])
def home():
    """
    get all data
    """
    all = Notes.query.all()
    return render_template('view.html', todos=all)

@app.route('/', methods=['POST'])
def create():
    """
    dummy insert data
    """
    name = request.form["name"]
    note = Notes(name, False)
    db.session.add(note)
    db.session.commit()
    # return redirect(url_for('home'))
    return jsonify({
        "name": name,
        "done": False
    })

@app.route('/update/<user_id>', methods=['PUT'])
def change(user_id):
    """
    get spesific row base on id
    """
    uuid = user_id
    found_user = Notes.query.filter_by(id=uuid).first()
    if found_user:
        changes = not found_user.done
        found_user.done = changes
        db.session.commit()
        if changes == True:
            activity = "Done"
        else:
            activity = "Not yet"
        return found_user.name+' is '+activity
    else:
        return 'user cannot be found'

@app.route('/delete/<user_id>', methods=['DELETE'])
def remove(user_id):
    """
    get spesific row base on id
    """
    uuid = user_id
    Notes.query.filter_by(id=uuid).delete()
    db.session.commit()
    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)