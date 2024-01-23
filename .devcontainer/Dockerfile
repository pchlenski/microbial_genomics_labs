#Docker Image for Microbial Genomics BIOL BC3308 Spring 2023

FROM ubuntu 
MAINTAINER pac@cs.columbia.edu
ENV PATH="/root/miniconda3/bin:${PATH}"
ENV TINI_VERSION v0.6.0
ARG PATH="/root/miniconda3/bin:${PATH}"
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]
EXPOSE 80 8888

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget python3-pip git
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& mkdir /root/.conda \
	&& bash Miniconda3-latest-Linux-x86_64.sh -b \
	&& rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda update conda && conda update --all
RUN conda remove --force menuinst
RUN conda install python=3.7
RUN conda install -c conda-forge notebook nb_conda_kernels
RUN conda install -c conda-forge -c bioconda -c defaults snippy
RUN conda install -c bioconda bwa spades clustalw vcftools openssl=1.0\
	samtools blast fastp fastqc fasttree minimap2 bcftools sra-tools
RUN conda install -c conda-forge biopython
RUN git clone https://github.com/pchlenski/microbial_genomics_labs.git /root/biolbc3308

CMD ["jupyter", "notebook", "/root/biolbc3300/labs", "--port=8888", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
