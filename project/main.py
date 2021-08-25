from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/call')
@login_required
def call():
    # make requests to the calling api
    url_of_message_sending_api = "https://api.mobizon.kz/service/message/sendSmsMessage?output=json&api=v1&apiKey=kza2e179fd6256289849a38ea60ad31945fd19cb292766f3fa89d0990b5c3f2f1a8854"
    headers_for_api = {
        "content-type" : "application/x-www-form-urlencoded",
        "cache-control" : "no-cache"
    }
    
    name = current_user.name
    phone_number_1 = current_user.phone_number_1
    phone_number_2 = current_user.phone_number_2
    phone_number_3 = current_user.phone_number_3

    params_and_message_for_api_1 = "recipient=7" + phone_number_1 + "&text=Тест+Компания+qutqarusy:+" + current_user.name + "+может+быть+в+беде+узнайте+все+ли+с+ним+хорошо&params%5Bvalidity%5D=1440"
    params_and_message_for_api_2 = "recipient=7" + phone_number_2 + "&text=Тест+Компания+qutqarusy:+" + current_user.name + "+может+быть+в+беде+узнайте+все+ли+с+ним+хорошо&params%5Bvalidity%5D=1440"
    params_and_message_for_api_3 = "recipient=7" + phone_number_3 + "&text=Тест+Компания+qutqarusy:+" + current_user.name + "+может+быть+в+беде+узнайте+все+ли+с+ним+хорошо&params%5Bvalidity%5D=1440"


    response_for_number_1 = requests.post(url = url_of_message_sending_api, headers=headers_for_api, data = params_and_message_for_api_1.encode('utf-8'))
    response_for_number_2 = requests.post(url = url_of_message_sending_api, headers=headers_for_api, data = params_and_message_for_api_2.encode('utf-8'))
    response_for_number_3 = requests.post(url = url_of_message_sending_api, headers=headers_for_api, data = params_and_message_for_api_3.encode('utf-8'))

    print(response_for_number_1)
    print(response_for_number_2)
    print(response_for_number_3)

    print(params_and_message_for_api_1)
    print(params_and_message_for_api_2)
    print(params_and_message_for_api_3)


    return render_template('profile-modal.html')