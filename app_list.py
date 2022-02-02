from flask import Blueprint, render_template, redirect, url_for, render_template, request, session, flash

from db import all_items, delete_item, new_item, update_item

first = Blueprint("first", __name__)

@first.route("/home")
@first.route('/')
def home():
    """
    Halaman utama.
    """
    return render_template('index.html', todos=all_items())


@first.route('/new', methods=['POST'])
def new():
    """
    Untuk membuat todo baru, hanya menerima request bertipe POST.
    """
    name= request.form.get('name')
    return new_item(name)
    # return redirect(url_for('home'))


@first.route('/update', methods=['POST'])
def update():
    """
    Untuk memperbarui status todo, hanya menerima request bertipe POST.
    """
    id = request.form.get('id')
    update_item(id)
    return 'ok'


@first.route('/delete', methods=['POST'])
def delete():
    """
    Untuk menghapus todo, hanya menerima request bertipe POST.
    """
    id = request.form.get('id')
    delete_item(id)
    return 'ok'

    