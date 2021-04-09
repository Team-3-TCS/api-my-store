from conexion import *
import sys
sys.path.append("..")
from model.rol import *

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)