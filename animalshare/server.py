from waitress import serve
    
from animalshare.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='$PORT' )