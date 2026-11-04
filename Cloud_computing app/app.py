<<<<<<< HEAD

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home page
@app.route("/")
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)

# Upload file
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    if not filename:
        return "Invalid filename"

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return redirect(url_for("index"))

# Download file
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(
        UPLOAD_FOLDER,
        filename,
        as_attachment=True
    )

# Delete file
@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.isfile(filepath):
        os.remove(filepath)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
=======

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home page
@app.route("/")
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)

# Upload file
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    if not filename:
        return "Invalid filename"

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return redirect(url_for("index"))

# Download file
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(
        UPLOAD_FOLDER,
        filename,
        as_attachment=True
    )

# Delete file
@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.isfile(filepath):
        os.remove(filepath)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 40b8b4c09836ca51437dee7d4ac6aad593c46334
