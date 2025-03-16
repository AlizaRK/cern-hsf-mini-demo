from flask import Flask

app = Flask("__main_")

@app.route('/')
def check():
    return 'Hey! checked'

if __name__ == "__main__":
    app.run()