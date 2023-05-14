# MLOPS-Experiment
## Prerequisites:
 - Install [python](https://www.python.org/) 
    ```
    brew install python@3.9
    ```
 - Install requirements
    ```
    pip install -r requirements.txt
    ```
## The Project
 - Run [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/)
    ```
    jupyter-lab
    ```

## MLFlow

## Prerequisites:
 - Install zlib (fixed an error for me)
   ```
   brew install zlib
   ```

## Commands
   ```
   # Build
   $ docker build -t mlops-experiment -f Dockerfile .

   # Train and register model
   $ mlflow run . --build-image

   # Serve model locally
   $ ./serve.sh

   # Inference
   $ curl http://127.0.0.1:5001/invocations \
      -H 'Content-Type: application/json'   \
      -d '{"inputs":[[0.1,0.1,0.1,0.1],[0.1,0.1,0.1,0.1],[0.1,0.1,0.1,0.1],[10,10,10000,1000],[0.1,0.1,0.1,0.1],[0.1,0.1,0.1,0.1]]}' 
   ```