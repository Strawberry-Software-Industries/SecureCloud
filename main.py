from flask import Flask
from flask import *
from werkzeug.utils import secure_filename
from config import *

import sqlite3 as sql
import hashlib
import os
import time
import datetime
import psutil
import socket
from Cryptodome.Hash import SHAKE256


# Upload Size Function & Configuration
def max_upload_size():
    with open("./config/upload-size.conf", 'r') as f:
        data = f.read()        

    return data.rstrip()


# App Declaration
app = Flask(__name__, static_url_path="/static")


# App Config
app.config['MAX_CONTENT_LENGTH'] = int(max_upload_size()) * 1024 * 1024
app.config["SECRET_KEY"] = "xprivate_ypysKXdjbyMNkBIbx88IFaKlbwiZwn"


# Variables
release_github = "https://github.com/Strawberry-Software-Industries/SecureCloud/releases/tag/v1.6"
build_date = "2022-18-03_12-00-00"
build_ver = "1.7.0_" + build_date
version_full = "Version 1.7.0"
version_short = "v1.7.0"
revision = "rev-1"
codename = "Strawberry Mix"

is_lts_ver = "no"
is_oss = "yes"
edition_ver = "Home"
uptime = time.time()


# Functions
def get_language():
    with open("./config/language.conf", "r") as f:
        data = f.read()

    return data.rstrip()


def allowed_file(filename):
    with open("./config/file-extensions.conf", 'r') as f:
        data = f.read()

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in data


def get_hostname():
    with open("./config/hostname.conf", 'r') as f:
        data = f.read()
    
    return data.rstrip()


def get_upload_path():
    with open("./config/upload-path.conf", 'r') as f:
        data = f.read()
    
    return data.rstrip()


def memory_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def cpu_usage():
    return psutil.cpu_percent()


def get_ipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_dir():
    h = os.listdir(get_upload_path().rstrip())
    str1 = ' <br/> '.join(h)
    return str1


def check_password(hashed_password, user_password):
    return hashed_password == hashlib.shake256(user_password.encode()).hexdigest()


def logged_in(session):
    try:
        db = sql.connect('db/users.db')
        c = db.cursor()
        c.execute('SELECT * FROM users WHERE name = ? AND password = ?', (session.get("username"), session.get("password")))
        logged_in=c.fetchall()

    except:
        logged_in=False

    if logged_in:
        return True

    else:
        return False


# Login
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
        
    lang = get_language()
    hostname = get_hostname()

    if lang == "english":
        title = "Login"
        title_header = "Login"
        username_txt = "Username"
        password_txt = "Password"
        welcome = "Welcome to "


    else:
        title = "Anmelden"
        title_header = "Anmelden" 
        username_txt = "Nutzername"
        password_txt = "Passwort"
        welcome = "Willkommen bei "

    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = sql.connect('db/users.db')
        c = db.cursor()

        Password_Byte_Encoded = str.encode(password)
        Hashed_Password = SHAKE256.new()
        Hashed_Password.update(Password_Byte_Encoded)
        pw = Hashed_Password.read(26).hex()

        c.execute('SELECT * FROM users WHERE name = ? AND password = ?', (username, pw))
        if c.fetchall():
            print(f'[User Account Manager] {username} has logged in!')

            session["username"] = username
            session["password"] = pw

            return redirect("/home")

        else:
            print(f'[User Account Manager] {username} tried to log in! - But the Username or Password is wrong!')
            error = 'Invalid Credentials. Please try again.'

    db = sql.connect('db/users.db')
    c = db.cursor()
    c.execute("SELECT name, password FROM users")
    fetched = c.fetchall()

    try:
        setup = request.args.get("setup")

    except:
        setup = False

    if not fetched or setup:
        return render_template("fsetup.html")

    else:
        return render_template('login.html', title=title, title_header=title_header, username_txt=username_txt, password_txt=password_txt, error=error, welcome=welcome,
                                hostname=hostname)

# First Setup
@app.route("/fsetup")
def first_setup():
    db = sql.connect('db/users.db')
    c = db.cursor()
    c.execute("SELECT name, password FROM users")
    fetched = c.fetchall()
    if fetched:
        return redirect("/")


# Root 
@app.route('/root')
def root():
    if not logged_in(session):
        return redirect("/")

    return render_template('root.html')


# For Debugging
@app.route('/dir')
def dir():
    if not logged_in(session):
        return redirect("/")
        
    dirlist = get_dir().rstrip()
    return render_template('dir.html', dirlist=dirlist)


# Home
@app.route("/home", methods=["GET", "POST"])
def home():
    if not logged_in(session):
        return redirect("/")

    lang = get_language()

    if lang == "english":
        title = "Home"
        title_header = "Home - SecureCloud"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"
        welcome = "Welcome"
        welcome_txt = "Welcome to SecureCloud! This is your personal SecureCloud. Press Settings to personalize your SecureCloud."

    else:
        title = "Startseite"
        title_header = "Startseite - SecureCloud"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        welcome = "Willkommen"
        welcome_txt = "Willkommen! Dies ist ihre persönliche SecureCloud. Drücken sie auf Einstellungen um ihre SecureCloud zu personalisieren."


    return render_template('index.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, title_header=title_header,
                            files_link=files_link, welcome=welcome, welcome_txt=welcome_txt)


# Settings
@app.route('/settings', methods=["GET", "POST"])
def settings():
    if not logged_in(session):
        return redirect("/")
    
    with open("./config/file-extensions.conf", "r") as f:
        file_extensions_data = f.read()
        file_extensions_data_text = file_extensions_data.replace("{", "").replace("}", "").replace('"', "")

    with open("./config/language.conf", 'r') as f:
        language_data = f.read()

    lang = get_language()
    upload_size = max_upload_size()


    if request.method == 'POST':
        if request.form.get('de_lang') == 'de_lang':
            with open("./config/language.conf", 'w') as f:
                f.write("german")

        elif request.form.get('en_lang') == 'en_lang':
            with open("./config/language.conf", 'w') as f:
                f.write("english")


    if lang == "english":
        title = "Settings"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

        # Settings Language Files
        act_ext = "Active File Extensions"
        add_ext = "Add File Extension..."
        add = "Add"
        up_av = "Update available"
        up_txt = "An update for SecureCloud is available. To install the update, save all your settings and press Perform Update."
        up_perf = "Perform Update"
        goto_about = "To go to the information page press about"
        about_link = "About"
        german = "German"
        english = "English"
        language = "Language"
        changed_german = "Language changed to German"
        changed_english = "Language changed to English"
        memory = "Memory"
        memory_usage_mb = f"{format(int(memory_usage() / 1024 / 1024))} MB of {format(int(psutil.virtual_memory().total / 1024 / 1024))} MB"
        upload_limit = "Upload Size"
        change = "Change"
        more = "More..."

    else:
        title = "Einstellungen"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"

        # Settings Language Files
        act_ext = "Aktive Dateiendungen"
        add_ext = "Dateiendung hinzufügen..."
        add = "Hinzufügen"
        up_av = "Update verfügbar"
        up_txt = "Ein Update für SecureCloud ist verfügbar. Um das Update zu installieren sichern sie alle ihre Einstellungen, und drücken sie auf Update durchführen"
        up_perf = "Update durchführen"
        goto_about = "Um zur Informationsseite zu gelangen drücken sie auf Über"
        about_link = "Über"
        language = "Sprache"
        german = "Deutsch"
        english = "Englisch"
        changed_german = "Sprache wurde zu Deutsch geändert"
        changed_english = "Sprache wurde zu Englisch geändert"
        memory = "Arbeitsspeicher"
        memory_usage_mb = f"{format(int(memory_usage() / 1024 / 1024))} MB von {format(int(psutil.virtual_memory().total / 1024 / 1024))} MB"
        upload_limit = "Hochladegröße"
        change = "Ändern"
        more = "Weiteres..."

    memory_usage_percent = f"{psutil.virtual_memory()[2]} %"
    cpu_usage_percent = cpu_usage()
    uptime_conv = str(datetime.timedelta(seconds=int(round(time.time()-uptime))))
     
    

    return render_template('settings.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                           act_ext=act_ext, up_av=up_av, up_txt=up_txt, up_perf=up_perf, goto_about=goto_about, about_link=about_link, language=language,
                           german=german, english=english, add_ext=add_ext, file_extensions_data=file_extensions_data, memory_usage_mb=memory_usage_mb,
                           memory_usage_percent=memory_usage_percent, memory=memory, file_extensions_data_text=file_extensions_data_text, changed_german=changed_german,
                           changed_english=changed_english, upload_limit=upload_limit, change=change, upload_size=upload_size, more=more, cpu_usage_percent=cpu_usage_percent,
                           uptime_conv=uptime_conv, add=add)


# Change Upload Size
@app.route('/change-upload-size', methods=["GET", "POST"])
def change_upload_size():
    if not logged_in(session):
        return redirect("/")    
    
    lang = get_language()


    if lang == "english":
        title = "Change Upload Size"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        size_in_mb = "Size in MB"
        postscr = ""
        submitvalue = "Change"


    else:
        title = "Hochladegröße ändern"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        size_in_mb = "Größe in MB"
        postscr = ""
        submitvalue = "Ändern"

    if request.method == "POST":
        with open("./config/upload-size.conf", "w") as f:

            if request.form["upload_size"] == "":
                if lang == "english":
                    postscr = "Invalid Upload Size"
                else:
                    postscr = "Inkorrektr Hochladegröße"

                data = f.write("32")

            else:
                data = f.write(request.form["upload_size"])
                if lang == "english":
                    postscr = "Upload Size was updated"
                else:
                    postscr = "Hochladegröße wurde aktualisiert"

    return render_template("change-upload-size.html", title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, size_in_mb=size_in_mb, postscr=postscr, submitvalue=submitvalue)


# Change Hostname
@app.route('/change-hostname', methods=["GET", "POST"])
def change_hostname():
    if not logged_in(session):
        return redirect("/")    
    
    lang = get_language()


    if lang == "english":
        title = "Change Hostname"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        postscr = ""
        submitvalue = "Change"


    else:
        title = "Hostname ändern"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        postscr = ""
        submitvalue = "Ändern"

    if request.method == "POST":
        with open("./config/hostname.conf", "w") as f:

            if request.form["hostname"] == "":
                if lang == "english":
                    postscr = "Invalid Hostname"
                else:
                    postscr = "Inkorrekter Hostname"
                    
                data = f.write("Personal SecureCloud")

            else:
                data = f.write(request.form["hostname"])

                if lang == "english":
                    postscr = "Hostname was updated"
                else:
                    postscr = "Hostname wurde geupdated"

    return render_template("change-hostname.html", title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, postscr=postscr, submitvalue=submitvalue)


# Change Upload Path
@app.route('/change-upload-path', methods=["GET", "POST"])
def change_upload_path():
    if not logged_in(session):
        return redirect("/")    
    
    lang = get_language()


    if lang == "english":
        title = "Change Upload Path"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        postscr = ""
        submitvalue = "Change"
        upload_path = "Upload Path"


    else:
        title = "Hochladeort ändern"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        postscr = ""
        submitvalue = "Ändern"
        upload_path = "Hochladeort"

    if request.method == "POST":
        with open("./config/upload-path.conf", "w") as f:

            if request.form["upload_path"] == "":
                if lang == "english":
                    postscr = "Invalid Upload Path"
                else:
                    postscr = "Inkorrekter Hochladeort"
                    
                data = f.write("./")

            else:
                data = f.write(request.form["upload_path"])

                if lang == "english":
                    postscr = "Upload Path was updated"
                else:
                    postscr = "Hochladeort wurde geupdated"

    return render_template("change-upload-path.html", title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, postscr=postscr, submitvalue=submitvalue, upload_path=upload_path)


# About
@app.route('/about', methods=["GET", "POST"])
def about():
    if not logged_in(session):
        return redirect("/")

    with open("./config/file-extensions.conf", "r") as f:
        data = f.read()

    hostname = get_hostname()
    up_path = get_upload_path()

    if is_lts_ver == "yes":
        lts = "LTS"
    elif is_lts_ver == "rr":
        lts = "Rolling"
    else:
        lts = "Stable"

    if is_oss == "yes":
        oss = "OSS"
    else:
        oss = "Non-OSS"


    # BETA
    with open("./config/theme.conf", "r") as f:
        dark = f.read()
        

    if dark == "y":
        dark_mode = '<link rel="stylesheet" href="../static/dark.css">'
    else:
        dark_mode = '<link rel="stylesheet" href="../static/white.css">'
    
    

    lang = get_language()

    if lang == "english":
        title = "About"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

        check_update = "Check for Updates"
        change_hostname = "Change Hostname"
        upload_path = "Upload Path"
        upload_path_info = "All files are uploaded there:"
        change_upload_path = "Change"
        edition = "Edition"
        gh_o = "Our GitHub"
        av_editions = "Avaible Editions"
        update_no = "You're on the lastest build!"

    else:
        title = "Über"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"

        check_update = "Auf Updates überprüfen"
        change_hostname = "Hostnamen ändern"
        upload_path = "Hochladeort"
        upload_path_info = "Dort werden alle Dateien hochgeladen:"
        change_upload_path = "Ändern"
        edition = "Edition"
        gh_o = "Unser GitHub"
        av_editions = "Verfügbare Editionen"
        update_no = "Du bist auf dem letzten Stand!"

    return render_template('about.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                           check_update=check_update, change_hostname=change_hostname, hostname=hostname, upload_path=upload_path, upload_path_info=upload_path_info,
                           change_upload_path=change_upload_path, up_path=up_path, build_ver=build_ver, build_date=build_date, version_full=version_full, 
                           version_short=version_short, revision=revision, edition=edition, lts=lts, gh_o=gh_o, av_editions=av_editions, update_no=update_no, 
                           dark_mode=dark_mode, oss=oss, edition_ver=edition_ver, codename=codename)



@app.route('/files')
def file_choosing():
    if not logged_in(session):
        return redirect("/")

    lang = get_language()
    upload_path = get_upload_path()
    username = session.get('username')

    if lang == "english":
        title = "Files"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"
        global_file_str = "Shared Files"
        personal_file_str = "Personal Files"
        cur_up_path = "Current Shared Path: "
        logged_in_as = "Logged in as"

    else:
        title = "Dateien"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        global_file_str = "Geteilte Daten"
        personal_file_str = "Personal Files"
        cur_up_path = "Aktueller Geteilte Pfad: "
        logged_in_as = "Angemeldet als"
    

    return render_template('file_choosing.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, dir=dir, global_file_str=global_file_str, personal_file_str=personal_file_str, cur_up_path=cur_up_path,
                            logged_in_as=logged_in_as, upload_path=upload_path, username=username)



# Files
@app.route("/shared-files", defaults={'req_path': ''})
@app.route('/shared-files/<path:req_path>')
def files(req_path):
    if not logged_in(session):
        return redirect("/")

    lang = get_language()
    upload_path = get_upload_path()

    if lang == "english":
        title = "Files"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

    else:
        title = "Dateien"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
    

    abs_path = os.path.join(upload_path, req_path)

    if not os.path.exists(abs_path):
        return render_template('404_file.html'), 404

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    

    return render_template('files.html', files=files, title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, dir=dir)


# Download Files
@app.route("/shared-files/download/<path:filename>", methods=["GET", "POST"])
def download_file(filename):
    if not logged_in(session):
        return redirect("/")
    
    upload_path = get_upload_path()

    path = upload_path + filename
    return send_file(path, as_attachment=True)


# Browse Files
@app.route('/shared-files/', defaults={'req_path': ''})
@app.route('/shared-files/<path:req_path>')
def dir_browsing(req_path):
    if not logged_in(session):
        return redirect("/")
    
    upload_path = get_upload_path()
    lang = get_language()

    if lang == "english":
        title = "Files"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

    else:
        title = "Dateien"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"

    abs_path = os.path.join(upload_path, req_path)

    if not os.path.exists(abs_path):
        return render_template('404_file.html'), 404

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)

    return render_template('file_browsing.html', files=files, title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, 
                            user_link=user_link, files_link=files_link)





# Personal Files
@app.route("/personal-files", defaults={'req_path': ''})
@app.route('/personal-files/<path:req_path>')
def personal_files(req_path):
    if not logged_in(session):
        return redirect("/")

    lang = get_language()
    user_file_path = f'./data/{session.get("username")}'

    if lang == "english":
        title = "Files"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

    else:
        title = "Dateien"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
    

    abs_path = os.path.join(user_file_path, req_path)

    if not os.path.exists(abs_path):
        return render_template('404_file.html'), 404

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    

    return render_template('file_browsing_personal.html', files=files, title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, 
                            files_link=files_link, dir=dir)


# Download Personal Files
@app.route("/personal-files/download/<path:filename>", methods=["GET", "POST"])
def download_personal_file(filename):
    if not logged_in(session):
        return redirect("/")
    
    user_file_path = f'./data/{session.get("username")}'

    path = user_file_path + filename
    return send_file(path, as_attachment=True)


# Browse Personal Files
@app.route('/personal-files/', defaults={'req_path': ''})
@app.route('/personal-files/<path:req_path>')
def dir_browsing_personal(req_path):
    if not logged_in(session):
        return redirect("/")
    
    user_file_path = f'./data/{session.get("username")}'
    lang = get_language()

    if lang == "english":
        title = "Files"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"

    else:
        title = "Dateien"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"

    abs_path = os.path.join(user_file_path, req_path)

    if not os.path.exists(abs_path):
        return render_template('404_file.html'), 404

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)

    return render_template('file_browsing_personal.html', files=files, title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, 
                            user_link=user_link, files_link=files_link)


# Users
@app.route('/users', methods=['GET', 'GET'])
def users():
    if not logged_in(session):
        return redirect("/")

    lang = get_language()

    if lang == "english":
        title = "Users"
        text = "Create a New User!"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "Users"
        cr_new_usr = "Add user"
        logout = "Logout"

    else:
        title = "Benutzer"
        text = "Erstelle einen Neuen Nutzer!"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        cr_new_usr = "Nutzer hinzufügen"
        logout = "Ausloggen"

    conn = sql.connect('db/users.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
    conn.close()
    
    return render_template('users.html', title=title, text=text, upload_link=upload_link, files_link=files_link, settings_link=settings_link, home_link=home_link, 
                            user_link=user_link, user_list=[], cr_new_usr=cr_new_usr, logout=logout)


# Create User
@app.route("/users/create", methods=['GET', 'POST'])
def create_user():
    if not logged_in(session):
        return redirect("/")


    lang = get_language()

    if lang == "english":
        title = "User Creation"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        submitvalue = "Create"
        username_txt = "Name"
        password_txt = "Password"
        password_txt2 = "Repeat Password"
        postscr = ""
        create_new_account_txt = "The User Account Manager will help you! So type only the data you need"

    else:
        title = "Benutzererstellung"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        submitvalue = "Erstellen"
        username_txt = "Name"
        password_txt = "Passwort"
        password_txt2 = "Passwort wiederholen"
        postscr = ""
        create_new_account_txt = "Der User Account Manager wird dir dabei helfen! Tippe also nur die benötigten Daten ein"

    try:
        if request.method == "POST":

            if request.form["password"] == request.form["password2"]:
                pass

                if lang == "english":
                    postscr=f"A new account with the name {request.form['username']} has been created."

                else:
                    postscr=f"Ein neuer Account mit dem Namen {request.form['username']} wurde erstellt."

                try:
                    Password_Byte_Encoded = str.encode(request.form["password"])
                    Hashed_Password = SHAKE256.new()
                    Hashed_Password.update(Password_Byte_Encoded)

                    conn = sql.connect('./db/users.db')
                    conn.execute(f"INSERT INTO users (name,password) VALUES ('{request.form['username']}', '{Hashed_Password.read(26).hex()}')")
                    conn.commit()
                    conn.close()
                    print(f"[User Account Manager] New Account created » {request.form['username']}")
                    
                    try:
                        os.mkdir(f"./data/{request.form['username']}")

                    except FileExistsError:
                        print(f"Could not create Directory {request.form['username']}: This Directory already exists")

                except:
                        print(f"Error while creating User {request.form['username']}: Values cannot be inserted into the Database")


            else:
                if lang == "english":
                    postscr="Error: Both passwords are not identical"

                else:
                    postscr="Fehler: Beide Passwörter sind nicht identisch"

    except:
        pass

    return render_template('create-user.html', username_txt=username_txt,password_txt=password_txt,password_txt2=password_txt2, title=title, upload_link=upload_link, 
                            settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,submitvalue=submitvalue, postscr=postscr, 
                            create_new_account_txt=create_new_account_txt)


# Upload to Shared Files
@app.route("/upload/shared/", methods=['GET', 'POST'], defaults={'upload_path': None})
@app.route("/upload/shared/<path:upload_path>", methods=['GET', 'POST'])
def upload_to_shared(upload_path):
    if not logged_in(session):
        return redirect("/")

    lang = get_language()
    upload_limit = max_upload_size()

    if lang == "english":
        title = "Upload"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        upl_up_to = "You can upload up to " + upload_limit + "MB"
        upl_to = "Upload to Shared Files"
        change = "Change"
        cur_up_path = "Current Path: "

    else:
        title = "Hochladen"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        upl_up_to = "Du kannst bis zu " + upload_limit + "MB hochladen"
        upl_to = "Zu geteilte Daten Hochladen"
        change = "Ändern"
        cur_up_path = "Aktueller Pfad: "

    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)

            if upload_path == None:
                upload_path = ""

            file.save(os.path.join(get_upload_path() + upload_path, filename))

            path = (os.path.join(get_upload_path() + upload_path, filename))
            print("Path:", path)

            result = path.split("/")
            filename2 = result[-1:]
            print("Filename:", filename2)
            filename1 = " ".join(filename2)

    return render_template('upload_shared.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                            upl_up_to=upl_up_to, change=change, cur_up_path=cur_up_path, upload_path=upload_path, upl_to=upl_to)

# Upload to Personal Files
@app.route("/upload/personal/", methods=['GET', 'POST'], defaults={'upload_path': None})
@app.route("/upload/personal/<path:upload_path>", methods=['GET', 'POST'])
def upload_to_personal(upload_path):
    if not logged_in(session):
        return redirect("/")

    lang = get_language()
    upload_limit = max_upload_size()
    user_upload_path = f'./data/{session.get("username")}/'

    if lang == "english":
        title = "Upload"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        upl_up_to = "You can upload up to " + upload_limit + "MB"
        upl_to = "Upload to Personal Files"
        change = "Change"
        cur_up_path = "Current Path: "

    else:
        title = "Hochladen"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        upl_up_to = "Du kannst bis zu " + upload_limit + "MB hochladen"
        upl_to = "Zu persönlichen Daten Hochladen"
        change = "Ändern"
        cur_up_path = "Aktueller Pfad: "

    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            print('No file selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)

            if upload_path == None:
                upload_path = ""

            file.save(os.path.join(user_upload_path + upload_path, filename))

            path = (os.path.join(user_upload_path + upload_path, filename))
            print("Path:", path)

            result = path.split("/")
            filename2 = result[-1:]
            print("Filename:", filename2)
            filename1 = " ".join(filename2)



    return render_template('upload_personal.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                            upl_up_to=upl_up_to, change=change, cur_up_path=cur_up_path, upload_path=upload_path, upl_to=upl_to)



# Update
@app.route("/update", methods=['GET', 'POST'])
def update(): 
    if not logged_in(session):
        return redirect("/")

    lang = get_language()

    if lang == "english":
        title = "Update"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"
        update_text = "An update for SecureCloud is available. To install the update, save all your settings and press Perform Update."
        up_perf = "Perform update"

    else:
        title = "Update"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        update_text = "Ein Update für SecureCloud ist verfügbar. Um das Update zu installieren sichern sie alle ihre Einstellungen, und drücken sie auf Update durchführen"    
        up_perf = "Update durchführen"

    return render_template('update.html', title=title, settings_link=settings_link, upload_link=upload_link, files_link=files_link, home_link=home_link, user_link=user_link,
                            update_text=update_text, up_perf=up_perf, release_github=release_github)


# Whats that
@app.route("/secretpage")
def secretpage():
    return "<img src='{{url_for('static', filename='strawberry_software.png')}}' align='middle'/>"

                            
# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# 404 Page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if ip_type == "networking":
    hostip = get_ipaddr()

elif ip_type == "localhost":
    hostip = "localhost"

else:
    hostip = "localhost"


# Run SecureCloud 
if __name__ == '__main__':
    app.run(host=hostip, port=global_port, threaded=True)