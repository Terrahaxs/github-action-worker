FROM public.ecr.aws/lambda/python:3.9 as build

ENV PYTHONUNBUFFERED=1
# TODO: make this multistage
RUN pip install --upgrade pip
RUN yum install -y git unzip wget jq
RUN git clone --depth=1 https://github.com/tfutils/tfenv.git /var/.tfenv
ENV PATH=/var/.tfenv/bin:/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
RUN tfenv install 1.2.9 
RUN tfenv install 1.1.9
RUN tfenv install 1.0.11
RUN tfenv install 0.15.5
RUN tfenv install 0.14.11
RUN tfenv install 0.13.7
RUN tfenv install 0.12.31

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .