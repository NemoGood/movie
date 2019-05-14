from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:yellow'>admin page</h1>"