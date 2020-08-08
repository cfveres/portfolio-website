from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('db.txt', mode='a') as db:
        name = data['name']
        email = data['email']
        message = data['message']
        db.write(f'\n{name},{email},{message}')

def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Post error: not saved to database.'
    return 'Something went wrong. Please try again.'
