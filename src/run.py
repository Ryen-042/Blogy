
if __name__ == '__main__':
    from blog import create_app
    
    app = create_app()
    
    app.run(debug=True)
