# from flask import Flask, render_template, request,session,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
# import json
# from datetime import date, datetime
# import smtplib


# with open('config.json', 'r') as c:
#     params = json.load(c)["params"]

# local_server = True
# app = Flask(__name__)
# app.secret_key = 'super-secre-key'
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = 'abdulumer1205@gmail.com',
#     MAIL_PASSWORD= '#AbdUmer@203403'
# )
# mail = Mail(app)
# if(local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

# db = SQLAlchemy(app)


# class Contacts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(60), nullable=True)
#     email = db.Column(db.String(80), nullable=False)

# class Posts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     tagline = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(12), nullable=False)
#     content = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(60), nullable=True)
#     img_file = db.Column(db.String(20), nullable=True)
   
# @app.route("/")
# def home():
#     posts=Posts.query.filter_by().all()
#     return render_template('index.html', params=params,posts=posts)



# @app.route("/about")
# def about():
#     return render_template('about.html', params=params)

# @app.route("/dashboard",methods=['GET','POST'])
# def dashboard():
#     if 'user' in session and session['user']==params['admin_user']:
#         posts=Posts.query.all()
#         return render_template('dashboard.html',params=params,posts=posts)
#     if request.method=="POST":
#         username=request.form.get('uname')
#         userpass=request.form.get("pass")
#         if (username==params['admin_user'] and userpass==params['admin_password']):
#             #set the session variable
#             session['user']=username
#             posts=Posts.query.all()

#             return render_template('dashboard.html',params=params,posts=posts)
        
#     else:
#         return render_template("login.html", params=params)

# @app.route('/post')
# def post():
#     return render_template('post.html',params=params)

# @app.route("/post/<string:post_slug>",methods=['GET'])
# def post_route(post_slug):
#     post=Posts.query.filter_by(slug=post_slug).first()
#     return render_template('post.html', params=params,post=post)

# from flask import Flask, render_template, request, session, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)

# # Assume params and db are already set up...

# @app.route("/edit/<string:sno>", methods=['GET', 'POST'])
# def edit(sno):
#     if 'user' in session and session['user'] == params['admin_user']:
#         if request.method == 'POST':
#             # Fetch form data
#             box_title = request.form.get('title')
#             tline = request.form.get("tagline")
#             slug = request.form.get("slug")
#             content = request.form.get("content")
#             img_file = request.form.get("img_file")
#             date = datetime.now()

#             if sno == '0':
#                 # If new post
#                 post = Posts(title=box_title, tagline=tline, slug=slug, content=content, img_file=img_file, date=date)
#                 db.session.add(post)
#                 db.session.commit()
#                 return redirect(url_for('edit', sno=post.sno))
#             else:
#                 # If editing existing post
#                 post = Posts.query.filter_by(sno=sno).first()
#                 if post:
#                     post.title = box_title
#                     post.tagline = tline
#                     post.slug = slug
#                     post.content = content
#                     post.img_file = img_file
#                     post.date = date
#                     db.session.commit()
#                     return redirect(url_for('edit', sno=post.sno))

#         # For GET request, fetch the post for editing
#         post = Posts.query.filter_by(sno=sno).first()
#         return render_template('edit.html', params=params, post=post)

#     return redirect(url_for('dashboard'))  # Redirect if the user is not logged in



# @app.route("/contact", methods = ['GET', 'POST'])
# def contact():
#     if(request.method=='POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
#         db.session.add(entry)
#         db.session.commit()
#         mail.send_message('New message from ' + name,
#                           sender=email,
#                           recipients = [params['gmail-user']],
#                           body = message + "\n" + phone
#                           )
#     return render_template('contact.html', params=params)


# app.run(debug=True)


from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import math
from datetime import datetime

# Load configuration
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='abdulumer1205@gmail.com',
    MAIL_PASSWORD='#AbdUmer@203403'
)

mail = Mail(app)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

# Models
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(60), nullable=True)
    email = db.Column(db.String(80), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(12), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(60), nullable=True)
    img_file = db.Column(db.String(20), nullable=True)

# Routes
@app.route("/")
def home():
    posts=Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['no_of_posts']))

    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    
    page=int(page)

    posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]

    if(page==1):
        prev='#'
        next="/?page="+str(page+1)
    elif(page==last):
        prev="/?page="+str(page-1)
        next="#"
    else:
        prev="/?page="+str(page-1)
        next="/?page="+str(page+1)

    posts = Posts.query.all()
    return render_template('index.html', params=params, posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', params=params)



@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')



@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    
    if request.method == "POST":
        username = request.form.get('uname')
        userpass = request.form.get("pass")
        if username == params['admin_user'] and userpass == params['admin_password']:
            session['user'] = username  # Set the session variable
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
    
    return render_template("login.html", params=params,prev=prev,next=next)

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):  # Include `sno` as a parameter
    if "user" in session and session['user'] == params['admin_user']:
        if request.method == "POST":
            # Assign values from the form on POST request
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            if sno == '0':  # Adding a new post
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:  # Editing an existing post
                post = Posts.query.filter_by(sno=sno).first()
                if post:  # Ensure the post exists
                    post.title = box_title
                    post.tline = tline
                    post.slug = slug
                    post.content = content
                    post.img_file = img_file
                    post.date = date
                    db.session.commit()
                return redirect('/edit/' + sno)

    # Handle GET request: Fetch the post details to edit
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post)





@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone)
    return render_template('contact.html', params=params)

if __name__ == "__main__":
    app.run(debug=True)