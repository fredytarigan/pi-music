from app import create_app

if __name__ == "__main__":
    app = create_app()

    # set app to debug if log level is 'DEBUG'
    # app_debug = False
    # if app.config["LOG_LEVEL"].upper() == "DEBUG":
    #     app_debug = True

    app.run(debug=True,
            host="0.0.0.0", port="8089")
