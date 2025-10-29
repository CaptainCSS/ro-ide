from flask import Flask, request
import io
import contextlib
import traceback

app = Flask(__name__)


@app.route("/run", methods=["POST"])
def run_code():
    code = request.data.decode("utf-8")

    # Capture stdout
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code, {"__builtins__": {}})  # removes dangerous builtins
        except Exception:
            traceback.print_exc(file=output)

    return output.getvalue() or "No output."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)