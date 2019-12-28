import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="smartward"
        )
mycursor = mydb.cursor()
sql = "SELECT * FROM users"
mycursor.execute(sql)
records = mycursor.fetchall()
username=[]
for row in records:
    username.append(row[3])
mycursor.close()


class Ui_MainWindow(object):
    def adminPageAccess(self):
        self.stackedWidget.setCurrentIndex(4)
        print('Logged in as Admin.')        
        
    def userPageAccess(self):
        self.stackedWidget.setCurrentIndex(3)
        print('Logged in as User.')
        self.back_from_userpage=QtWidgets.QPushButton(self.userpage)
        print('hi')
        self.back_from_userpage.setGeometry(QtCore.QRect(430, 490, 101, 41))
        self.back_from_userpage.setStyleSheet("border-radius:20px;\n""color:black;\n""background:red;\n""font-family:Consolas;\n""font-size:20px;\n""font-style:normal;\n""")
        self.back_from_userpage.setObjectName("back_from_userpage")
        self.back_from_userpage.setText("Back")
        ###Signup function#####################################################
        self.back_from_userpage.setAutoDefault(True)
        self.back_from_userpage.clicked.connect(self.linkPageAccess)
        
    def linkPageAccess(self):
        self.stackedWidget.setCurrentIndex(5)
        print('Choose:.')    
            
    def birth_registration(self):
        print("birth_registration_button_pushed")

    def death_registration(self):
        print("death_registration_button_pushed")

    def marriage_registration(self):
        print("marriage_registration_button_pushed")
        
    def clearsigninlabel(self):
        self.sign_empty_error_label.setText("")

    def clearsignuplabels(self):
        self.repass_error_label.setText("")                
        self.username_error_label.setText("")

    def clearsignuppage(self):
        self.signup_fname_edit.setText("")
        self.signup_lname_edit.setText("")
        self.signup_username_edit.setText("")
        self.signup_password_edit.setText("")
        self.signup_repassword_edit.setText("")
        self.signup_year_edit.setText("")
        self.signup_month_edit.setText("")
        self.signup_day_edit.setText("")

        
    def logout(self):
        self.stackedWidget.setCurrentIndex(2)
        self.statusbar.showMessage("© Smartward")
        MainWindow.setWindowTitle("Smartward-Login")
        print("Logged out.")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.statusbar.showMessage("Logged Out."+"                        "+"© Smartward")
        
      
        
    def refertohome(self):###refers to home page
        self.stackedWidget.setCurrentIndex(0)
        MainWindow.setWindowTitle("Smartward")
        self.clearsigninlabel()
        self.clearsignuppage()
        self.clearsignuplabels()
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.statusbar.showMessage("© Smartward")
        
    def refertologin(self):###refers to login page        
        self.stackedWidget.setCurrentIndex(2)
        MainWindow.setWindowTitle("Smartward-Login")
        completer=QtWidgets.QCompleter(sorted(username))
        font = QtGui.QFont()
        font.setPointSize(16)
        completer.popup().setFont(font)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.username_edit.setCompleter(completer)
        self.clearsignuppage()
        self.clearsignuplabels()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.statusbar.showMessage("© Smartward")
        
    def refertosignup(self):###refers to signup page
        self.stackedWidget.setCurrentIndex(1)
        MainWindow.setWindowTitle("Smartward-Signup")
        self.clearsigninlabel()
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.statusbar.showMessage("© Smartward")
        
    def exitwindow():
        Mainwindow.close

    def show_password(self):
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        

    def hide_password(self):
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        

    ####for signup#####################################################################
    def signupfxn(self):        
        fname_su= self.signup_fname_edit.text().title().strip()
        lname_su= self.signup_lname_edit.text().title().strip()
        username_su=self.signup_username_edit.text().lower().strip()
        password_su=self.signup_password_edit.text().strip()
        repassword_su=self.signup_repassword_edit.text().strip()
        year_su=self.signup_year_edit.text().strip()
        month_su=self.signup_month_edit.text().strip()
        date_su=self.signup_day_edit.text().strip()
        dob_su=str(year_su)+"/"+str(month_su)+"/"+str(date_su)
        if ((fname_su!="" or lname_su!="") and (password_su!="") and (repassword_su!="") and (year_su!="") and (month_su!="") and (date_su!="") and (username_su!="")):
            if ((username_su=="admin")):              
                self.signup_username_edit.setText("")
                self.username_error_label.setText("Username taken.")
            else:
                if (password_su==repassword_su):
                    mycursor=mydb.cursor()
                    sql = "INSERT INTO users (firstname,lastname,username,password,dob_year,dob_month,dob_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (fname_su,lname_su,username_su,password_su,year_su,month_su,date_su)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    mycursor.close()
                    print ("......................................")
                    print ("Signup Successful.")
                    print ("......................................")
                    username.append(username_su)
                    #print (username)
                    self.clearsignuplabels()
                    self.username_edit.setText("")                                       
                    self.refertologin()                    
                else:
                    self.signup_password_edit.setText("")
                    self.signup_repassword_edit.setText("")
                    self.repass_error_label.setText("Password do not match.")
        else:
            self.repass_error_label.setText("Empty field.")           
            
    ####################################################################################################

    ####for signin#####################################################################################
    def loginfxn(self):        
        uname_login=self.username_edit.text().lower().strip()
        password_login=self.password_edit.text().strip()
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT * FROM users WHERE username=%s"
        mycursor.execute(sql,(uname_login,))        
        records = mycursor.fetchall()
        for row in records:
            usernamefromdb=row[3].strip().lower()
            passwordfromdb=row[4].strip()
        if (uname_login=="" or password_login==""):
            self.sign_empty_error_label.setText("Username or password empty.")          
        else:            
            self.sign_empty_error_label.setText("")
            if ((uname_login=="admin" and password_login=="admin") or (uname_login==usernamefromdb and password_login==passwordfromdb)):    
                if (uname_login==usernamefromdb and password_login==passwordfromdb):
                    if (uname_login=="admin" and password_login=="admin"):
                        self.stackedWidget.setCurrentIndex(5)
                        self.statusbar.showMessage("Logged In.(Admin):"+str(uname_login)+"                          "+"© Smartward")
                        print('Logged in as Admin.:'+str(uname_login))
                        MainWindow.setWindowTitle("SmartWard-Admin- Welcome "+str(uname_login))
                        password_login=self.password_edit.setText("")
                    else:
                        self.stackedWidget.setCurrentIndex(3)
                        self.statusbar.showMessage("Logged In.(User):"+str(uname_login)+"                          "+"© Smartward")
                        print('Logged in as User.:'+str(uname_login))
                        MainWindow.setWindowTitle("SmartWard-User- Welcome "+str(uname_login))
                        password_login=self.password_edit.setText("")
                        '''elif ((uname_login not in username)):
                        self.sign_empty_error_label.setText("Not allowed.")
                        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
                        password_login=self.password_edit.setText("")'''
                else:
                    self.sign_empty_error_label.setText("Not allowed.")
                    self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
                    password_login=self.password_edit.setText("")
            else:
                self.sign_empty_error_label.setText("Not allowed.")
                self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
                password_login=self.password_edit.setText("")
        mycursor.close()
    ####################################################################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")        
        MainWindow.setFixedSize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        #(70, 45, 671, 491)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 620))
        self.stackedWidget.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")

        #######Start of Home page###################################################

        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.loginpage_refer_fromhome = QtWidgets.QPushButton(self.home)
        self.loginpage_refer_fromhome.setGeometry(QtCore.QRect(515, 330, 211, 41))
        self.loginpage_refer_fromhome.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.loginpage_refer_fromhome.setObjectName("loginpage_refer_fromhome")
        ##from home to login##################################################        
        self.loginpage_refer_fromhome.setAutoDefault(True)
        self.loginpage_refer_fromhome.clicked.connect(self.refertologin)
        ######################################################################
        self.signuppage_refer_fromhome = QtWidgets.QPushButton(self.home)
        self.signuppage_refer_fromhome.setGeometry(QtCore.QRect(515, 380, 211, 41))
        self.signuppage_refer_fromhome.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.signuppage_refer_fromhome.setObjectName("signuppage_refer_fromhome")
        ##from home to signup##################################################
        self.signuppage_refer_fromhome.setAutoDefault(True)
        self.signuppage_refer_fromhome.clicked.connect(self.refertosignup)
        ######################################################################
        self.homepage_info = QtWidgets.QLabel(self.home)
        self.homepage_info.setGeometry(QtCore.QRect(75, 70, 651, 171))
        self.homepage_info.setStyleSheet("color:white;\n"
"font-size:24px;\n"
"font-family:\"Consolas\";\n"
"border-radius:30px;")
        self.homepage_info.setAlignment(QtCore.Qt.AlignCenter)
        self.homepage_info.setObjectName("homepage_info")
        self.exit_from_home = QtWidgets.QPushButton(self.home)
        self.exit_from_home.setGeometry(QtCore.QRect(515, 430, 211, 41))
        self.exit_from_home.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.exit_from_home.setObjectName("exit_from_home")
        ####exit from home#############################################################
        self.exit_from_home.setAutoDefault(True)
        self.exit_from_home.clicked.connect(self.exitwindow)
        ###############################################################################

        ########End of home page###############################################################

        ##start of signup page################################################################
        self.stackedWidget.addWidget(self.home)
        self.signup = QtWidgets.QWidget()
        self.signup.setObjectName("signup")
        self.signup_box = QtWidgets.QGroupBox(self.signup)
        self.signup_box.setGeometry(QtCore.QRect(100, 70, 611, 391))
        self.signup_box.setStyleSheet("background:rgb(0, 0, 255);")
        self.signup_box.setTitle("")
        self.signup_box.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_box.setObjectName("signup_box")
        self.signup_label = QtWidgets.QLabel(self.signup_box)
        self.signup_label.setGeometry(QtCore.QRect(250, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("color:black;")
        self.signup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_label.setObjectName("signup_label")
        self.home_from_signup = QtWidgets.QPushButton(self.signup)
        self.home_from_signup.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.home_from_signup.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.home_from_signup.setObjectName("home_from_signup")
        ##from signup to home#########################################################
        self.home_from_signup.setAutoDefault(True)
        self.home_from_signup.clicked.connect(self.refertohome)
        ##############################################################################
        self.signup_fname_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_fname_edit.setGeometry(QtCore.QRect(30, 60, 241, 41))        
        self.signup_fname_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_fname_edit.setText("")
        self.signup_fname_edit.setObjectName("signup_fname_edit")
        self.signup_lname_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_lname_edit.setGeometry(QtCore.QRect(350, 60, 241, 41))
        self.signup_lname_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_lname_edit.setText("")
        self.signup_lname_edit.setObjectName("signup_lname_edit")
        self.signup_username_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_username_edit.setGeometry(QtCore.QRect(30, 140, 241, 41))
        self.signup_username_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_username_edit.setText("")
        self.signup_username_edit.setObjectName("signup_username_edit")
        self.signup_password_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_password_edit.setGeometry(QtCore.QRect(30, 220, 241, 41))
        self.signup_password_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_password_edit.setText("")
        self.signup_password_edit.setObjectName("signup_password_edit")       
        self.signup_repassword_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_repassword_edit.setGeometry(QtCore.QRect(350, 220, 241, 41))
        self.signup_repassword_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_repassword_edit.setText("")
        self.signup_repassword_edit.setObjectName("signup_repassword_edit")
        self.signup_year_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_year_edit.setGeometry(QtCore.QRect(30, 300, 91, 41))
        self.signup_year_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_year_edit.setText("")
        self.signup_year_edit.setObjectName("signup_year_edit")
        self.signup_month_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_month_edit.setGeometry(QtCore.QRect(125, 300, 91, 41))
        self.signup_month_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_month_edit.setText("")
        self.signup_month_edit.setObjectName("signup_month_edit")
        self.signup_day_edit = QtWidgets.QLineEdit(self.signup_box)
        self.signup_day_edit.setGeometry(QtCore.QRect(220, 300, 91, 41))
        self.signup_day_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_day_edit.setText("")
        self.signup_day_edit.setObjectName("signup_day_edit")
        self.signup_pushbutton = QtWidgets.QPushButton(self.signup_box)
        self.signup_pushbutton.setGeometry(QtCore.QRect(470, 330, 121, 41))
        self.signup_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signup_pushbutton.setObjectName("signup_pushbutton")
        ###Signup function#####################################################
        self.signup_pushbutton.setAutoDefault(True)
        self.signup_pushbutton.clicked.connect(self.signupfxn)
        ########################################################################
        self.fname_label_signup = QtWidgets.QLabel(self.signup_box)
        self.fname_label_signup.setGeometry(QtCore.QRect(100, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.fname_label_signup.setFont(font)
        self.fname_label_signup.setStyleSheet("color:white;")
        self.fname_label_signup.setObjectName("fname_label_signup")
        self.lname_label_signup = QtWidgets.QLabel(self.signup_box)
        self.lname_label_signup.setGeometry(QtCore.QRect(420, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.lname_label_signup.setFont(font)
        self.lname_label_signup.setStyleSheet("color:white;")
        self.lname_label_signup.setObjectName("lname_label_signup")
        self.uname_label_signup = QtWidgets.QLabel(self.signup_box)
        self.uname_label_signup.setGeometry(QtCore.QRect(100, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.uname_label_signup.setFont(font)
        self.uname_label_signup.setStyleSheet("color:white;")
        self.uname_label_signup.setObjectName("uname_label_signup")
        self.username_error_label = QtWidgets.QLabel(self.signup_box)
        self.username_error_label.setGeometry(QtCore.QRect(316, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_error_label.setFont(font)
        self.username_error_label.setStyleSheet("color:red;")
        self.username_error_label.setObjectName("username_error_label")
        self.password_label_signup = QtWidgets.QLabel(self.signup_box)
        self.password_label_signup.setGeometry(QtCore.QRect(100, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.password_label_signup.setFont(font)
        self.password_label_signup.setStyleSheet("color:white;")
        self.password_label_signup.setObjectName("password_label_signup")
        self.repass_label_signup = QtWidgets.QLabel(self.signup_box)
        self.repass_label_signup.setGeometry(QtCore.QRect(420, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.repass_label_signup.setFont(font)
        self.repass_label_signup.setStyleSheet("color:white;")
        self.repass_label_signup.setObjectName("repass_label_signup")
        self.repass_error_label = QtWidgets.QLabel(self.signup_box)
        self.repass_error_label.setGeometry(QtCore.QRect(320, 270, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.repass_error_label.setFont(font)
        self.repass_error_label.setStyleSheet("color:red;")
        self.repass_error_label.setObjectName("repass_error_label")
        self.year_label_signup = QtWidgets.QLabel(self.signup_box)
        self.year_label_signup.setGeometry(QtCore.QRect(60, 270, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.year_label_signup.setFont(font)
        self.year_label_signup.setStyleSheet("color:white;")
        self.year_label_signup.setObjectName("year_label_signup")
        self.month_label_signup = QtWidgets.QLabel(self.signup_box)
        self.month_label_signup.setGeometry(QtCore.QRect(140, 270, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.month_label_signup.setFont(font)
        self.month_label_signup.setStyleSheet("color:white;")
        self.month_label_signup.setObjectName("month_label_signup")
        self.date_label_signup = QtWidgets.QLabel(self.signup_box)
        self.date_label_signup.setGeometry(QtCore.QRect(230, 270, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.date_label_signup.setFont(font)
        self.date_label_signup.setStyleSheet("color:white;")
        self.date_label_signup.setObjectName("date_label_signup")
        self.signin_refer_pushbutton = QtWidgets.QPushButton(self.signup)
        self.signin_refer_pushbutton.setGeometry(QtCore.QRect(100, 470, 261, 41))
        self.signin_refer_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signin_refer_pushbutton.setObjectName("signin_refer_pushbutton")
        ##refer to signin from signup##########################################
        self.signin_refer_pushbutton.setAutoDefault(True)
        self.signin_refer_pushbutton.clicked.connect(self.refertologin)
        ########################################################################        
        self.exit_from_signuppage = QtWidgets.QPushButton(self.signup)
        self.exit_from_signuppage.setGeometry(QtCore.QRect(615, 470, 101, 41))
        self.exit_from_signuppage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_signuppage.setObjectName("exit_from_signuppage")
        ####exit from signup#############################################################
        self.exit_from_signuppage.setAutoDefault(True)
        self.exit_from_signuppage.clicked.connect(self.exitwindow)
        #################################################################################

        #######end of signup page#########################################################

        ######start of login page##########################################################
        self.stackedWidget.addWidget(self.signup)
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.signin_box = QtWidgets.QGroupBox(self.login)
        self.signin_box.setGeometry(QtCore.QRect(140, 120, 511, 321))
        self.signin_box.setStyleSheet("background:blue;")
        self.signin_box.setTitle("")
        self.signin_box.setObjectName("signin_box")
        self.home_from_signin = QtWidgets.QPushButton(self.login)
        self.home_from_signin.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.home_from_signin.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.home_from_signin.setObjectName("home_from_signin")
        ##from signin to home##############################################
        self.home_from_signin.setAutoDefault(True)
        self.home_from_signin.clicked.connect(self.refertohome)
        ###################################################################
        ####error label######################################################
        self.sign_empty_error_label = QtWidgets.QLabel(self.signin_box)
        self.sign_empty_error_label.setGeometry(QtCore.QRect(140, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_empty_error_label.setFont(font)
        self.sign_empty_error_label.setStyleSheet("color:red;")
        self.sign_empty_error_label.setObjectName("sign_empty_error_label")
        ##error label end##################################################
        self.username_edit = QtWidgets.QLineEdit(self.signin_box)
        self.username_edit.setGeometry(QtCore.QRect(130, 90, 221, 51))
        self.username_edit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.username_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        #self.username_edit.setPlaceholderText("username")
        #self.username_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.username_edit.setObjectName("username_edit")
        ##############################################################################        
        completer=QtWidgets.QCompleter(sorted(username))
        font = QtGui.QFont()
        font.setPointSize(16)
        completer.popup().setFont(font)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.username_edit.setCompleter(completer)
        #self.username_edit.returnPressed.connect(self.loginfxn)        
        #############################################################################
        self.password_edit = QtWidgets.QLineEdit(self.signin_box)
        self.password_edit.setGeometry(QtCore.QRect(130, 150, 221, 51))
        self.password_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"\n"
"")
        #self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.password_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_edit.setObjectName("password_edit")
        ##############################################################################
        self.password_edit.returnPressed.connect(self.loginfxn)        
        #############################################################################
        self.show_password_pushbutton = QtWidgets.QPushButton(self.signin_box)
        self.show_password_pushbutton.setGeometry(QtCore.QRect(360, 160, 61, 41))
        self.show_password_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.show_password_pushbutton.setObjectName("show_password_pushbutton")
        ##show password###########################################################
        self.show_password_pushbutton.setAutoDefault(True)
        self.show_password_pushbutton.clicked.connect(self.show_password)
        #########################################################################
        self.hide_password_pushbutton = QtWidgets.QPushButton(self.signin_box)
        self.hide_password_pushbutton.setGeometry(QtCore.QRect(430, 160, 61, 41))
        self.hide_password_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.hide_password_pushbutton.setObjectName("hide_password_pushbutton")
        ##hide password###########################################################
        self.hide_password_pushbutton.setAutoDefault(True)
        self.hide_password_pushbutton.clicked.connect(self.hide_password)              
        ########################################################################       
        ####login#############################################################
        self.signin_pushbutton = QtWidgets.QPushButton(self.signin_box)
        self.signin_pushbutton.setGeometry(QtCore.QRect(180, 270, 151, 41))
        self.signin_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signin_pushbutton.setObjectName("signin_pushbutton")
        ############################################################################       
        self.signin_pushbutton.setAutoDefault(True)
        self.signin_pushbutton.clicked.connect(self.loginfxn)
        ###########################################################################
        self.signup_refer_pushbutton = QtWidgets.QPushButton(self.login)
        self.signup_refer_pushbutton.setGeometry(QtCore.QRect(140, 450, 251, 41))
        self.signup_refer_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signup_refer_pushbutton.setObjectName("signup_refer_pushbutton")
        ##refer to signup from signin##########################################
        self.signup_refer_pushbutton.setAutoDefault(True)
        self.signup_refer_pushbutton.clicked.connect(self.refertosignup)
        self.sign_empty_error_label.setText("")
        ########################################################################
        self.signin_label = QtWidgets.QLabel(self.signin_box)
        self.signin_label.setGeometry(QtCore.QRect(200, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.signin_label.setFont(font)
        self.signin_label.setStyleSheet("color:Black;\n"
"font-style:bold;\n"
"font-family:\"Consolas\";")
        self.signin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_label.setObjectName("signin_label")
        self.signin_password_label = QtWidgets.QLabel(self.signin_box)
        self.signin_password_label.setGeometry(QtCore.QRect(30, 160, 91, 21))
        self.signin_password_label.setStyleSheet("font-size:18px;\n"
"font-family:\"arial\";")
        self.signin_password_label.setObjectName("signin_password_label")
        self.signin_username_label = QtWidgets.QLabel(self.signin_box)
        self.signin_username_label.setGeometry(QtCore.QRect(30, 100, 91, 21))
        self.signin_username_label.setStyleSheet("font-size:18px;\n"
"font-family:\"arial\";")
        self.signin_username_label.setObjectName("signin_username_label")  
                    
        self.exit_from_signinpage = QtWidgets.QPushButton(self.login)
        self.exit_from_signinpage.setGeometry(QtCore.QRect(555, 450, 101, 41))
        self.exit_from_signinpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_signinpage.setObjectName("exit_from_signinpage")
        ####exit from signin#############################################################
        self.exit_from_signinpage.setAutoDefault(True)
        self.exit_from_signinpage.clicked.connect(self.exitwindow)
        #################################################################################

        ####end of login page#############################################################

        ####start of user page#############################################################
        self.stackedWidget.addWidget(self.login)
        self.userpage = QtWidgets.QWidget()
        self.userpage.setObjectName("userpage")
        self.Welcome_label = QtWidgets.QLabel(self.userpage)
        self.Welcome_label.setGeometry(QtCore.QRect(200, 50, 370, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.Welcome_label.setFont(font)
        self.Welcome_label.setStyleSheet("background:yellow;\n"
"color:black;\n""border-radius:20px;")
        self.Welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_label.setObjectName("Welcome_label")


        ######open######################birth_registration###################################
        self.birth_registration_button = QtWidgets.QPushButton(self.userpage)
        self.birth_registration_button.setGeometry(QtCore.QRect(200, 130, 400, 80))
        self.birth_registration_button.setStyleSheet("color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.birth_registration_button.setObjectName("birth_registration_button")
           ###birth registration fxn###################################################
        self.birth_registration_button.setAutoDefault(True)
        self.birth_registration_button.clicked.connect(self.birth_registration)
           ###########################################################################
        ######closed##################################################################

        ######open##########################death_registration###################################
        self.death_registration_button = QtWidgets.QPushButton(self.userpage)
        self.death_registration_button.setGeometry(QtCore.QRect(200, 230, 400, 80))
        self.death_registration_button.setStyleSheet("color:black;\n"
"background:red;\n"                                                    
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.death_registration_button.setObjectName("death_registration_button")
           ###death registration fxn###################################################
        self.death_registration_button.setAutoDefault(True)
        self.death_registration_button.clicked.connect(self.death_registration)
           ###########################################################################
        ######closed##################################################################

         ######open##########################death_registration###################################
        self.marriage_registration_button = QtWidgets.QPushButton(self.userpage)
        self.marriage_registration_button.setGeometry(QtCore.QRect(200, 330, 400, 80))
        self.marriage_registration_button.setStyleSheet("color:black;\n"
"background:red;\n"                                                    
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.marriage_registration_button.setObjectName("marriage_registration_button")
           ###death registration fxn###################################################
        self.marriage_registration_button.setAutoDefault(True)
        self.marriage_registration_button.clicked.connect(self.marriage_registration)
           ###########################################################################
        ######closed##################################################################

        ######open#############################################################
        self.logout_from_loggedinpage = QtWidgets.QPushButton(self.userpage)
        self.logout_from_loggedinpage.setGeometry(QtCore.QRect(535, 490, 101, 41))
        self.logout_from_loggedinpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.logout_from_loggedinpage.setObjectName("logout_from_userpage")
           ####logout from loggedin###################################################
        self.logout_from_loggedinpage.setAutoDefault(True)
        self.logout_from_loggedinpage.clicked.connect(self.logout)
           ###########################################################################
        ######closed##################################################################       


        ######open####################################################################
        self.exit_from_loggedinpage = QtWidgets.QPushButton(self.userpage)
        self.exit_from_loggedinpage.setGeometry(QtCore.QRect(640, 490, 101, 41))
        self.exit_from_loggedinpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_loggedinpage.setObjectName("exit_from_userpage")
               ####Exit from loggedin################################################
        self.exit_from_loggedinpage.setAutoDefault(True)
        self.exit_from_loggedinpage.clicked.connect(self.exitwindow)
               #######################################################################
        ###close######################################################################

        #########end of user page##########################################################

        ####start of admin page##########################################################
        self.stackedWidget.addWidget(self.userpage)
        self.adminpage = QtWidgets.QWidget()
        self.adminpage.setObjectName("adminpage")
        self.Welcome_label_admin = QtWidgets.QLabel(self.adminpage)
        self.Welcome_label_admin.setGeometry(QtCore.QRect(200, 50, 380, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.Welcome_label_admin.setFont(font)
        self.Welcome_label_admin.setStyleSheet("background:yellow;\n"
"color:black;\n""border-radius:20px;")
        self.Welcome_label_admin.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_label_admin.setObjectName("Welcome_label_admin")
         ######open#############################################################
        self.back_from_adminpage = QtWidgets.QPushButton(self.adminpage)
        self.back_from_adminpage.setGeometry(QtCore.QRect(430, 490, 101, 41))
        self.back_from_adminpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.back_from_adminpage.setObjectName("back_from_adminpage")
           ####linkpage from admin#############################################################
        self.back_from_adminpage.setAutoDefault(True)
        self.back_from_adminpage.clicked.connect(self.linkPageAccess)
           #################################################################################

         ######open#############################################################
        self.logout_from_adminpage = QtWidgets.QPushButton(self.adminpage)
        self.logout_from_adminpage.setGeometry(QtCore.QRect(535, 490, 101, 41))
        self.logout_from_adminpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.logout_from_adminpage.setObjectName("logout_from_adminpage")
           ####logout from admin#############################################################
        self.logout_from_adminpage.setAutoDefault(True)
        self.logout_from_adminpage.clicked.connect(self.logout)
           #################################################################################
        ######closed###########################################################################

         #open########################################################################
        self.exit_from_adminpage = QtWidgets.QPushButton(self.adminpage)
        self.exit_from_adminpage.setGeometry(QtCore.QRect(640, 490, 101, 41))
        self.exit_from_adminpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_adminpage.setObjectName("exit_from_adminpage")
               ####Exit from loggedin################################################
        self.exit_from_adminpage.setAutoDefault(True)
        self.exit_from_adminpage.clicked.connect(self.exitwindow)
               #######################################################################
        ###close######################################################################

       
        #########end of admin page######################################################


        ###########################start of link page################################

        self.stackedWidget.addWidget(self.adminpage)
        self.link_page = QtWidgets.QWidget()
        self.link_page.setObjectName("link_page")
        self.link_page_label = QtWidgets.QLabel(self.link_page)
        self.link_page_label.setGeometry(QtCore.QRect(200, 50, 380, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.link_page_label.setFont(font)
        self.link_page_label.setStyleSheet("background:yellow;\n"
"color:black;\n""border-radius:20px;")
        self.link_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.link_page_label.setObjectName("link_page_label")



         ######open######################continue_as_admin##############################
        self.continue_as_admin = QtWidgets.QPushButton(self.link_page)
        self.continue_as_admin.setGeometry(QtCore.QRect(200, 130, 400, 80))
        self.continue_as_admin.setStyleSheet("color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.continue_as_admin.setObjectName("continue_as_admin")
           ###continue_as_admin fxn###################################################
        self.continue_as_admin.setAutoDefault(True)
        self.continue_as_admin.clicked.connect(self.adminPageAccess)
           ###########################################################################
        ######closed##################################################################

        ######open##########################continue_as_user###################################
        self.continue_as_user = QtWidgets.QPushButton(self.link_page)
        self.continue_as_user.setGeometry(QtCore.QRect(200, 230, 400, 80))
        self.continue_as_user.setStyleSheet("color:black;\n"
"background:red;\n"                                                    
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.continue_as_user.setObjectName("continue_as_user")
           ###continue_as_user fxn###################################################
        self.continue_as_user.setAutoDefault(True)
        self.continue_as_user.clicked.connect(self.userPageAccess)
           ###########################################################################
        ######closed##################################################################


         ######open#############################################################
        self.logout_from_linkpage = QtWidgets.QPushButton(self.link_page)
        self.logout_from_linkpage.setGeometry(QtCore.QRect(535, 490, 101, 41))
        self.logout_from_linkpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.logout_from_linkpage.setObjectName("logout_from_adminpage")
           ####logout from loggedin#############################################################
        self.logout_from_linkpage.setAutoDefault(True)
        self.logout_from_linkpage.clicked.connect(self.logout)
           #################################################################################
        ######closed###########################################################################

         #open########################################################################
        self.exit_from_linkpage = QtWidgets.QPushButton(self.link_page)
        self.exit_from_linkpage.setGeometry(QtCore.QRect(640, 490, 101, 41))
        self.exit_from_linkpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_linkpage.setObjectName("exit_from_adminpage")
               ####Exit from loggedin################################################
        self.exit_from_linkpage.setAutoDefault(True)
        self.exit_from_linkpage.clicked.connect(self.exitwindow)
               #######################################################################
        ###close######################################################################

        ####################################end of link page##########################
        
        ###############################################################################
        self.stackedWidget.addWidget(self.link_page)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("© Smartward")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartward"))
        self.loginpage_refer_fromhome.setText(_translate("MainWindow", "Login"))
        self.signuppage_refer_fromhome.setText(_translate("MainWindow", "Signup"))
        self.homepage_info.setText(_translate("MainWindow", " Welcome to our official software of Smartward!!!"))
        self.exit_from_home.setText(_translate("MainWindow", "Exit"))
        self.signup_label.setText(_translate("MainWindow", "Sign Up"))
        self.signup_pushbutton.setText(_translate("MainWindow", "Sign up"))
        self.fname_label_signup.setText(_translate("MainWindow", "First Name"))
        self.lname_label_signup.setText(_translate("MainWindow", "Last Name"))
        self.uname_label_signup.setText(_translate("MainWindow", "Username"))        
        self.password_label_signup.setText(_translate("MainWindow", "Password"))
        self.repass_label_signup.setText(_translate("MainWindow", "Re-password"))
        self.year_label_signup.setText(_translate("MainWindow", "Year"))
        self.month_label_signup.setText(_translate("MainWindow", "Month"))
        self.date_label_signup.setText(_translate("MainWindow", "Date"))
        self.signin_refer_pushbutton.setText(_translate("MainWindow", "Or Sign in instead??"))
        self.home_from_signup.setText(_translate("MainWindow", "Home"))
        self.exit_from_signuppage.setText(_translate("MainWindow", "Exit"))
        self.signin_pushbutton.setText(_translate("MainWindow", "Sign in"))
        self.signin_label.setText(_translate("MainWindow", "Sign In"))
        self.signin_password_label.setText(_translate("MainWindow", "Password"))
        self.signin_username_label.setText(_translate("MainWindow", "Username"))
        self.hide_password_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.show_password_pushbutton.setText(_translate("MainWindow", "Show"))
        self.signup_refer_pushbutton.setText(_translate("MainWindow", "Create an account"))
        self.home_from_signin.setText(_translate("MainWindow", "Home"))
        self.exit_from_signinpage.setText(_translate("MainWindow", "Exit"))
        self.Welcome_label.setText(_translate("MainWindow", "Welcome to your user page!!!"))
        self.birth_registration_button.setText(_translate("MainWindow", "Birth Registration"))
        self.death_registration_button.setText(_translate("MainWindow", "Death Registration"))
        self.marriage_registration_button.setText(_translate("MainWindow", "Marriage Registration"))
        self.logout_from_loggedinpage.setText(_translate("MainWindow", "Log out"))
        self.exit_from_loggedinpage.setText(_translate("MainWindow", "Exit"))
        self.Welcome_label_admin.setText(_translate("MainWindow", "Welcome to your admin page!!!"))
        self.back_from_adminpage.setText(_translate("MainWindow", "Back"))
        self.logout_from_adminpage.setText(_translate("MainWindow", "Log out"))
        self.exit_from_adminpage.setText(_translate("MainWindow", "Exit"))
        self.link_page_label.setText(_translate("MainWindow", "I would like to:"))
        self.logout_from_linkpage.setText(_translate("MainWindow", "Log out"))
        self.exit_from_linkpage.setText(_translate("MainWindow", "Exit"))
        self.continue_as_admin.setText(_translate("MainWindow", "Continue as admin"))
        self.continue_as_user.setText(_translate("MainWindow", "Continue as user"))
        
               


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())