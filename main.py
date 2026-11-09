from flask import Flask ,render_template ,request
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/issue-details")
def issue_details():
    return render_template("issue-details.html")
@app.route("/report",methods=["POST"])
def submit_report():
    issue_title=request.form.get("issue_title")
    category=request.form.get("category")
    location=request.form.get("location")
    description=request.form.get("description")
    if not issue_title or not category or not location or not description:
        return "please fill in all required fields"

    photo=request.files.get("photo")
    if photo and photo.filename:
        photo_name=photo.filename
    else:
        photo_name="photo not uploaded"
    print("Issue title=",issue_title,"Category=",category,"Location=",location,"Description=",description,"Photo=",photo)
    return render_template("report_success.html",issue_title=issue_title,category=category,location=location,description=description,photo_name=photo_name)
    