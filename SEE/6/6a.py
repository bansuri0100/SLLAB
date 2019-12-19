from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def index():
	if request.method=="GET":
		return render_template('index.html',msg="Welcome for Shopping !")
	if request.method =="POST":
		
		if int(request.form['i1'])<0 or int(request.form['i2'])<0 or int(request.form['i3'])<0:
			return render_template('index.html',msg="Number of items cannot be negative")
		else:
			cost=100*int(request.form['i1'])+200* int(request.form['i2'])+50* int(request.form['i3'])
			return render_template('index.html',msg="Total Cost = Rs"+str(cost))
if __name__=='__main__':
	app.run(debug=True)				
