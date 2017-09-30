FROM tensorflow/tensorflow:latest-py3

MAINTAINER Ryuichirou <@K_Ryuichirou>

RUN pip --no-cache-dir install \
        edward \
        ptvsd==3.0.0
RUN mkdir /notebooks/mmt

# TensorBoard
EXPOSE 6006
# Jupyter
EXPOSE 8888
# ptvsd
EXPOSE 3000

WORKDIR "/notebooks"
VOLUME "/notebooks/mmt"

CMD ["/run_jupyter.sh", "--allow-root"]
