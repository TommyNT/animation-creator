
from flask import Flask
from flask import render_template, request, flash
from media import S3MediaStorage 
from media.name_generator import generate_name
import boto3
import os
import json

app = Flask(__name__)
media_storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))

photos_list = []
sqs = boto3.resource('sqs', region_name="eu-central-1")
requestQueue = sqs.get_queue_by_name(
  QueueName=os.getenv("APP_QUEUE_NAME")

@app.route("/")
def hello():
    return render_template(
       'upload_files.html'
    )

@app.route("/make-animation")
def make_animation():
  return render_template(
          "make_animation.html",
          invitation="only limit is yourself")

@app.route("/upload", methods=['POST'])
def handle_upload():
	if 'uploaded_file' not in request.files:
	flash('No file part')
  	return redirect(request.url)

uploaded_file = request.files['uploaded_file']
file_ref = generate_name(uploaded_file.filename)
media_storage.store(
	dest=file_ref,
	source=uploaded_file
	)

	orders.load(current_user()).add_photo(file_ref)
	photos_list.append(file_ref)
	return "OK"

@app.route("/proceed", methods=["POST"])
# def proceed():
# 	order = orders.load(current_user())
# 	handler.handle(order.snapshot())
def proceed_animation():
  ani_request = {
    "email": request.form['email'],
    "photos": photos_list
  }

	requestQueue.send_message(
		MessageBody=json.dumps(ani_request)
		)
	return "OK"

@app.route("/prepare")
def prepare():
	return render_template(
		'prepare.html',
		invitation="the only limit is yourself",
		photos=photos_list 
		)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
