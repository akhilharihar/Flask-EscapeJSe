import pytest
from flask import Flask, render_template_string
from flask_escapejse import EscapeJSe


@pytest.fixture
def app():
    app = Flask("flask_test")
    EscapeJSe(app)
    return app


@pytest.fixture
def app_ctx(app):
    with app.app_context() as ctx:
        yield ctx


def test_escapejse(app, app_ctx):
    data = "<p>{{ 'vue'|jse }}</p>"
    assert render_template_string(data, vue=21) == "<p>{{ vue }}</p>"
