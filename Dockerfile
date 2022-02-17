FROM continuumio/miniconda3:4.10.3

#Install Python libraries
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate conda for local development with orgenv kernel conda environment 
SHELL ["conda", "run", "-n", "airport_forecasting", "/bin/bash", "-c"]