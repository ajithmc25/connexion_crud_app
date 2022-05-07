from flask import abort, make_response, request

from connection import db
from models import User
from schemas import UserSchema, users_schema


def users_get():
    users = User.query.all()
    # Serialize the queryset
    data = users_schema.dump(users)
    return data, 200


def users_post():
    json_data = request.get_json()

    existing_user = (
        User.query.filter(User.name == json_data['name'])
        .one_or_none()
    )

    if existing_user is None:
        schema = UserSchema()
        new_person = schema.load(json_data, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        data = schema.dump(new_person)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f"User {json_data['name']} exists already")


def user_get(userId):
    user = User.query.filter(User.id == userId).one_or_none()
    if user:
        user_schema = UserSchema()
        data = user_schema.dump(user)
        return data
    else:
        abort(404, f'Person not found for Id: {userId}')


def user_put(userId):
    user = User.query.filter(User.id == userId).one_or_none()
    json_data = request.get_json()

    if user:
        schema = UserSchema()
        update = schema.load(json_data, session=db.session)
        update.id = user.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(user)

        return data, 200

    else:
        abort(404, f"Person not found for Id: {userId}")


def user_delete(userId):
    user = User.query.filter(User.id == userId).one_or_none()
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {userId} deleted", 200)
    else:
        abort(404, f"User not found for Id: {userId}")
