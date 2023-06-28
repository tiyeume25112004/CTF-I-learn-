from flask import Flask, request, Response, render_template_string
app = Flask(__name__)
FLAG="this_is_FLAG"

def waf(string):
    blacklist = ["{{", "_", "'", "\"", "[", "]", "|", "eval", "os", "system",
                  "env", "import", "builtins", "class", "flag", "mro", "base",
                    "config", "query", "request", "attr", "set", "glob", "py"]
    for word in blacklist:
        if word in len(string):
            return False
    return True

@app.route("/",methods=['POST','GET'])
def index():
    template = request.args.get("template")
    variable = request.args.get("variable")
    if not waf(template) or not waf(variable):
        return "Try harder broooo =)))"
    if len(template) == 0 or len(variable) == 0:
        return "Missing parameter required"
    data = template.replace("{FLAG}", FLAG).replace("{variable}", variable)
    return render_template_string(f"""
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>cc</title>
        </head>
        <body>
            <p1> {data} </p1>
        </body>
        </html>
        """,data=data)
if __name__=="__main__":
    app.run(port=1234)
