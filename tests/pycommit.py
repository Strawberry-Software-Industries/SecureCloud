# here are old python codes saved

#    lang = request.form.get('lang-btn')
#
#    if lang == "lang-btn-en":
#        lang_btn_english()
#            
#    if lang == "lang-btn-de":
#        lang_btn_german()

#    def lang_btn_german():
#        with open("./config/language.conf") as f:
#            f.write("german")
#
#    def lang_btn_english():
#        with open("./config/language.conf") as f:
#            f.write('english')

# Login (Application Root)
#@app.route("/", methods=["GET", "POST"])
#def login():
#    error = None  
#
# #    lang = get_language()
#
    #if lang == "english":
     #   title = "Login"
      #  title_header = "Login"
       # username_txt = "Username"
        #password_txt = "Password"
#
#
 #   else:
  #      title = "Anmelden"
   #     title_header = "Anmelden" 
    #    username_txt = "Nutzername"
     #   password_txt = "Passwort"
#
        
 ##   if request.method == 'POST':
       # username = request.form['username']
   #     password = request.form['password']
    #completion = validate(username, password)
    #if completion ==False:
        #error = 'Invalid Credentials. Please try again.'
    #else:
            #return redirect(url_for('home'))


    #return render_template('login.html', title=title, title_header=title_header, username_txt=username_txt, password_txt=password_txt, error=error)

#def validate(username, password):
    #con = sql.connect('db/users.db')
    #completion = False
    #with con:
     #           cur = con.cursor()
      #          cur.execute("SELECT * FROM Users")
       #         rows = cur.fetchall()
        #        for row in rows:
         #           dbUser = row[0]
          #          dbPass = row[1]
           #         if dbUser==username:
            #            completion=check_password(dbPass, password)
    #return completion