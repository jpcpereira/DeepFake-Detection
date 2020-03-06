from __future__ import unicode_literals
from flask import Flask
from flask_restful import Api,Resource,reqparse
import requests

import youtube_dl
import os
#import Pass_face_video_path
from Pass_face_video_path import *

from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from pytube import YouTube

app = Flask(__name__)
api = Api(app)

class fakedetect(Resource):

    @app.route('/get/<url>')
    def get(url):
        predict='False'
        ydl_opts = {'outtmpl': 'C:\\Users\\20190060\\Desktop\\New folder\\test_video\\'+'1.mp4'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v='+url])


        path=find_processed_faces('C:\\Users\\20190060\\Desktop\\New folder\\test_video\\'+'1.mp4')

        #result='false'
        if path[0] == True:
            result=predict(path[1])
        else:
            return False
        return result

    def post(self):
        image={'url':uri,'is_prop':"",'prob':'70%'}
        return image,201

api.add_resource(fakedetect,'/api')
app.run(debug=True)
