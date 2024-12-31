from flask import Blueprint, request,url_for, redirect, session,jsonify
import logging
from models import db,Podcast
from model_utils import role_check
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

podcast = Blueprint("podcast", __name__)

@podcast.get('/api/v1/podcasts')
def list_podcasts() -> list[Podcast]:
    podcast_list:list[Podcast] = Podcast.query.all()
    return podcast_list

@podcast.get('/api/v1/podcasts/<id>')
def get_podcast(id):
    podcast_ = Podcast.query.filter_by(id=id).first()
    if podcast_:
        return podcast_
    else:
        return

@podcast.post('/api/v1/podcasts')
def create_podcast():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    category = str(data.get('category')).upper()
    publisher = data.get('publisher')
    image_url = data.get('image_url')
    feed_url = data.get('feed_url')
    audio_url = data.get('audio_url')
    duration = data.get('duration')

    try:
        new_podcast = Podcast(title=title,description = description,category = category,publisher = publisher,image_url = image_url,feed_url = feed_url,audio_url = audio_url,duration =duration)
        db.session.add(new_podcast)

    # Commit the transaction (this makes the changes permanent in the database)
        db.session.commit()
        return jsonify({'msg':'successfully created podcast'})
    except Exception as e:
        db.session.rollback()
        return f"Error occurred: {str(e)}"

@podcast.put('/api/v1/podcasts/<int:id>')
def update_podcast(id):
    data = request.json
    title = data.get('title')
    description = data.get('description')
    category = str(data.get('category')).upper()
    image_url = data.get('image_url')

    podcast_ = Podcast.query.get(id)
    if podcast_:
        if 'title' in data:
            Podcast.title = title
        if 'description' in data:
            Podcast.description = description
        if 'category' in data:
            Podcast.category = category
        if 'image_url' in data:
            Podcast.image_url = image_url
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error':str(e)})

        return jsonify({
            'message': 'Podcast updated successfully!'
        })
    else:
        return jsonify({'message': 'Podcast not found!'}), 404

@podcast.delete('/api/v1/podcasts/<int:id>')
def delete_podcast(id):
    try:
        podcast_ = Podcast.query.get(id)

        if podcast_:
            # Mark the user for deletion
            db.session.delete(podcast_)

            # Commit the transaction (this deletes the user from the database)
            db.session.commit()

            return jsonify({'message': f'Podcast {id} deleted successfully!'}), 200
        else:
            return jsonify({'message': 'Podcast not found!'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'message':str(e)})


#TODO : change relationship to be with the parent to enable smart-deletion