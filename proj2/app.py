from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import hashlib
import getpass
import json
import subprocess
import socket
import sys

app = Flask(__name__)



@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('calc.html')





@app.route('/login',methods=['POST'])
def do_admin_login():

	
	password_in = request.form['password']
	username_in = request.form['username']
	password_in = hashlib.sha256(password_in).hexdigest()	

	sudoPass="62Gh888!"
	found=False
	df = open("cred.json","r")	
	data=json.load(df)
	for item in data:
		if item['username']==username_in and item['password']==password_in:
			print("Authentication successfull.")
			w=open("log.log","w")
			w.write(username_in)
			w.close()
			found=True
			session['logged_in']=True
			
	if not found:
		badlogin()
		flash("Username or password incorrect...")			
	return home()

def badlogin():
	w=open("log.log","w")
	w.write("")
	w.close()

@app.route('/next', methods=['POST'])
def next():
	return home()

@app.route('/logout', methods=['POST'])
def logout():
	badlogin()
	session['logged_in']=False
	return home()

@app.route('/calc', methods=['POST'])
def my_form_post():
	n1 = request.form['num1']
	n2 = request.form['num2']
	len1 = len(n1)
	len2 = len(n2)
	if len1 == 0 or len2 == 0:
		return "0"
	res = [0] * (len1 + len2)
	i_num1 = 0
	i_num2 = 0
	for i in range(len1 - 1, -1, -1):
		c = 0
		num1 = ord(n1[i]) - 48
		i_num2 = 0
		for j in range(len2 -1, -1, -1):
			num2 = ord(n2[j]) - 48
			sumTot = num1 * num2 + res[i_num1 + i_num2] + c
			c = sumTot // 10
			res[i_num1 + i_num2] = sumTot % 10
			i_num2 += 1
		if(c > 0):
			res[i_num1 + i_num2] += c
		i_num1 += 1
	i = len(res) - 1
	while(i >= 0 and res[i] == 0):
		i -= 1
	if(i == -1):
		return "0"
	s = ""
	while(i >= 0):
		s += chr(res[i] + 48)
		i -= 1
	return render_template('product.html',A=n1,B=n2,C=s)
	#return "The product of <b>" + n1 + "</b> and <b>" + n2 + "</b> is <b>"  + s + "</b>"


@app.route('/led',methods=['GET'])
def led():
	r=open("log.log","r")
	user=r.read()
	r.close()
	print(user)
	return user

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0',port=4000)
