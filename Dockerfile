FROM python:3.9 as build
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
WORKDIR /bot
COPY --from=build /root/.local /root/.local
COPY ./src .
ENV PATH=/root/.local:$PATH
CMD ["python", "main.py"]
