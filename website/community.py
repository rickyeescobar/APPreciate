from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort
from website.auth import login_required
from website.db import get_db


community = Blueprint("community", __name__)




@community.route('/my_community', methods=('GET','POST'))
@login_required
def my_community():
    db = get_db()
    communities = db.execute(
        'SELECT name, owner_id FROM community c '
        'JOIN community_user ON c.name = community_user.community_name '
        'WHERE community_user.user_id = ?',(g.user['id'],)
    ).fetchall()

    user_id = int(g.user['id'])

    return render_template('community/my_community.html', communities=communities, user_id=user_id)


@community.route('/create_community', methods=['GET', 'POST'])
@login_required
def create_community():

    if request.method == 'POST':
        community = request.form['create_community']

        db = get_db()
        error = None

        if community is None:
            error = 'Community name is required.'

    
        if error is None:
            try:
                db.execute(
                    "INSERT INTO community (name, owner_id) VALUES (?, ?)",
                    (community, g.user['id']))

                db.commit()

                db.execute(
                    "INSERT INTO community_user (community_name, user_id) VALUES (?, ?)",
                    (community, g.user['id']))
                
                db.commit()

            except db.IntegrityError:
                error = f"{community} is already registered."
    
        if error is not None:
            flash(error)
        else:
            flash(f"{community} has been successfully added!")

    return render_template('community/create_community.html')

@community.route('/join_community', methods=['GET', 'POST'])
@login_required
def join_community():

    if request.method == 'POST':
        community = request.form['join_community']
        db = get_db()
        error = None

        if community is None:
            error = 'Community name is required.'

        #check if community exists
        check = db.execute(
            'SELECT * FROM community WHERE name = ?', (community,)
        ).fetchone()

        if check is None:
            error = "Community does not exist yet."
            return redirect(url_for("community.create_community"))

        try:
            db.execute (
                'INSERT INTO community_user (user_id, community_name) VALUES (?, ?)',
                (g.user['id'], community)
                )

            db.commit()

        except db.IntegrityError:
            error = f"There was an error joining {community}."


        if error == None:
            flash(f"{community} has been successfully added!")
        else:
            flash(error)

        return redirect(url_for("community.my_community"))

    return render_template('community/join_community.html')

def get_community_user(community_name):
    community_user = get_db().execute(
        'SELECT * FROM community_user WHERE community_name = ?', (community_name,)
    ).fetchone()

    if community_user is None:
        abort(404, f"Community_user {community_user} doesn't exist.")

    return community_user

def get_community(name):
    community = get_db().execute(
        'SELECT * FROM community WHERE name = ?', (name,)
    ).fetchone()

    if community is None:
        abort(404, f"Community {community} doesn't exist.")

    return community

@community.route('/<community_name>/leave_community', methods=['POST',])
@login_required
def leave_community(community_name):
    get_community_user(community_name)
    db = get_db()
    db.execute('DELETE FROM community_user WHERE community_name = ?', (community_name,))
    db.commit()
    return redirect(url_for('community.my_community'))

@community.route('/<community>/delete_community', methods=['POST',])
@login_required
def delete_community(community):
    get_community_user(community)
    db = get_db()
    db.execute('DELETE FROM community WHERE name = ?', (community,))
    db.commit()
    db.execute('DELETE FROM community_user WHERE community_name = ?', (community,))
    db.commit()
    return redirect(url_for('community.my_community'))