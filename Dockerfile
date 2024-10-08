FROM python:3.12.5-bookworm AS builder
COPY requirements.txt .
RUN pip install --user --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt --upgrade

FROM python:3.12.5-slim-bookworm
ENV PATH=/root/.local:$PATH
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/"
COPY --from=builder /root/.local /root/.local
RUN ls -la
COPY . .
CMD ["python", "bot/main.py"]