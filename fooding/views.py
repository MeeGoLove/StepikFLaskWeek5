from functools import wraps

from flask import abort, flash, session, redirect, request, render_template

from fooding import app, db


# ------------------------------------------------------
# Главная страница
@app.route("/")
def index_route():
    return render_template("main.html")
# ------------------------------------------------------
# Декораторы авторизации


# ------------------------------------------------------
# Страница админки


# ------------------------------------------------------
# Страница аутентификации


# ------------------------------------------------------
# Страница выхода из админки


# ------------------------------------------------------
# Страница добавления пользователя


# ------------------------------------------------------
# Страница смены пароля

