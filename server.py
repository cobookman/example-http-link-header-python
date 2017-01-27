import flask
app = flask.Flask(__name__)

@app.route("/")
def img_route():
  f = flask.send_file("img/image.jpeg")
  resp = flask.make_response(f)
  resp.headers["Link"] = "<https://pbs.twimg.com/profile_images/378800000822867536/3f5a00acf72df93528b6bb7cd0a4fd0c.jpeg>; rel=\"cononical\""
  return resp

if __name__ == "__main__":
  app.run()
