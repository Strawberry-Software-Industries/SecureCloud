from flask import Flask
from flask import Flask, request, redirect, render_template, make_response, url_for
from werkzeug.utils import secure_filename

import sqlite3 as sql

import os
import time
import datetime
import psutil
import socket


# Upload Size Function & Configuration
def max_upload_size():
    with open("./config/upload-size.conf", 'r') as f:
        data = f.read()        

    return data.rstrip()

application = Flask(__name__, static_url_path="/static")
application.config['MAX_CONTENT_LENGTH'] = int(max_upload_size()) * 1024 * 1024


# Variables
release_github = "https://github.com/Strawberry-Software-Industries/SecureCloud/releases/tag/v1.2"
build_date = "2022-08-02_16-18-13"
build_ver = "1.3.0_" + build_date
version_full = "Version 1.3.0"
version_short = "v1.3.0"
revision = "rev-1"

is_lts_ver = "y"
is_oss = "y"
edition_ver = "Home"
developer_key = "-"
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
    
    return data


def get_upload_path():
    with open("./config/upload-path.conf", 'r') as f:
        data = f.read()
    
    return data


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



# Root 
@application.route('/')
def root():

    return render_template('root.html')


# For Debugging
@application.route('/dir')
def dir():
    dirlist = get_dir().rstrip()
    return render_template('dir.html', dirlist=dirlist)


# Home
@application.route("/home", methods=["GET", "POST"])
def home():

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
@application.route('/settings', methods=["GET", "POST"])
def settings():
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
        up_av = "Update avaible"
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
                           uptime_conv=uptime_conv)


# About
@application.route('/about', methods=["GET", "POST"])
def about():
    with open("./config/file-extensions.conf", "r") as f:
        data = f.read()

    hostname = get_hostname()
    up_path = get_upload_path()

    if is_lts_ver == "y":
        lts = "LTS"
    else:
        lts = ""

    if is_oss == "y":
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
                           change_upload_path=change_upload_path, up_path=up_path, build_ver=build_ver, build_date=build_date, version_full=version_full, version_short=version_short,
                           revision=revision, edition=edition, lts=lts, gh_o=gh_o, av_editions=av_editions, update_no=update_no, dark_mode=dark_mode, oss=oss, edition_ver=edition_ver)


# Files
@application.route("/files", methods=["GET", "POST"])
def files():

    lang = get_language()
    dir = get_dir()

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

    return render_template('files.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                                         dir=dir)


# Userlist
@application.route('/users', methods=['GET', 'GET'])
def users():

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

    else:
        title = "Benutzer"
        text = "Erstelle einen Neuen Nutzer!"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        cr_new_usr = "Nutzer hinzufügen"

    conn = sql.connect('db/users.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
    conn.close()
    

    return render_template('users.html', title=title, text=text, upload_link=upload_link, files_link=files_link, settings_link=settings_link, home_link=home_link, user_link=user_link,
                                        user_list=[], cr_new_usr=cr_new_usr)


# Create User
@application.route("/users/create", methods=['GET', 'GET'])
def create_user():

    lang = get_language()

    if lang == "english":
        title = "User Creation"
        settings_link = "Settings"
        upload_link = "Upload"
        files_link = "Files"
        home_link = "Home"
        user_link = "User"

    else:
        title = "Benutzererstellung"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"

    return render_template('create-user.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link)


# Upload
@application.route("/upload", methods=['GET', 'POST'])
def upload():

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
        change = "Change"

    else:
        title = "Hochladen"
        settings_link = "Einstellungen"
        upload_link = "Hochladen"
        files_link = "Dateien"
        home_link = "Startseite"
        user_link = "Benutzer"
        upl_up_to = "Du kannst bis zu " + upload_limit + "MB hochladen"
        change = "Ändern"

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

            file.save(os.path.join(get_upload_path().rstrip(), filename))

            path = (os.path.join(get_upload_path().rstrip(), filename))
            print("path :", path)

            result = path.split("/")
            filename2 = result[-1:]
            print("fname :", filename2)
            filename1 = " ".join(filename2)

    return render_template('upload.html', title=title, upload_link=upload_link, settings_link=settings_link, home_link=home_link, user_link=user_link, files_link=files_link,
                                          upl_up_to=upl_up_to, change=change)


# Update
@application.route("/update", methods=['GET', 'POST'])
def update(): 

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


hostip = get_ipaddr()

if __name__ == '__main__':
    application.run(host=hostip, port=80, threaded=True)
