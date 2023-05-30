from flask import Flask,render_template,request

FAI=Flask(__name__)

@FAI.route('/data',methods=['GET','POST'])
def data():
    if request.method=='POST':
        #form_data=request.form
        #print(form_data)
        return request.form['na']

    return render_template('data.html')

FAI.run(debug=True)