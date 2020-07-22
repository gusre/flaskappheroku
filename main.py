from flask import *
import plotly.graph_objects as go
import plotly
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'gunasreesing@gmail.com',
	MAIL_PASSWORD = 'gunaSREE1@'
	)
mail = Mail(app)

@app.route('/sendmail',methods=['POST'])
def sendmail():
    try:
        if request.method=="POST":
            l=request.form['mail']
            msg = Message("Send Mail Tutorial!",sender="gunasreesing@gmail.com",recipients=[l])
            msg.body = "Yo!\nHave you heard the good word of Python???"           
            mail.send(msg)
        return render_template("mail.html")
    except:
        return {'Failure':'Mail not sent'}

@app.route('/sendprice')
def price():
    return render_template("mail.html")

@app.route('/plotly')
def feature():
    animals=['giraffes', 'orangutans', 'monkeys']
    fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])])
    fig.update_layout(barmode='group')
    div=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return render_template("graph.html",figure=div)

@app.route('/index')
def home():
   return render_template("feature.html")

@app.route('/')
def hello_world():
   return render_template("home.html")

if __name__ == '__main__':
   app.run()
