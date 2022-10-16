# Patrones de arquitectura utilizados
1. Factory en FinancialReportController.set_report_type
Según el tipo de reporte se crea una clase diferente para 
hacer el reporte
2. Adapter en FinancialReportController.create_report
Este método va a aceptar cualquier clase que soporte el método 
create_report
# Principios de diseño utilizados
1. Single responsibility: cada clase tiene una responsabilidad muy 
bien definida y el programa es el conjunto de las diferentes
clases realizando sus respectivas responsabilidades
2. Open closed principle: los métodos que crean diferentes partes
del reporte en ambas clases Report son privados para que estos
no se puedan modificar
3. Interface segregation: cada clase solo utiliza dependencias que necesita

# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME