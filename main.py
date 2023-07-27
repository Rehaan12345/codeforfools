from website import create_app 

app = create_app()

if __name__ == "__main__": # Only if we run this file will this line be executed. 
    app.run(debug=True) # Runs and everytime we make a change to the code, it will automatically rerun the web server. 