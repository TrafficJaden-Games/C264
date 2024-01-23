# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

#initailzing your flask, __name__ defining flask using app
app = Flask(__name__)

#open and redirect to default upload web page
#@app, known as 'decorator', tells the computer to execute the following function
#to specific page
@app.route('/')
def load_form():
    #render webpage
    return render_template('upload.html')

#function to upload image and redirect to a new webpage
#defining decorator to run function on webpage with /gray
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))

    display_message = 'image successfuly uploaded and displayed below'

    return render_template('upload.html', filename=filename, message=display_message)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()