## 1. Criando Um Docker Container PostgreSQL
**OBS: lembre-se de estar no diretório docker/**
**Configurações iniciais ( TESTE! )**
  ```json
  {
    "docker-name": "melodia_database",
    "database_name": "melodia",
    "password": "melodia",
    "user": "melodia",
    "port": 5444
  }
  ```
**Digite comando abaixo para criar um container PostgreSQL:**
```bash
chmod +x start_docker_postgresql.sh
./start_docker_postgresql.sh
```
Pronto! Seu container PostgreSQL foi criado com sucesso.

## 2. Inicializando o Container PostgreSQL
**Para a inicialização, caso não tenha um container PostgreSQL, crie um container PostgreSQL seguindo [a primeira instrução.](#1.-Criando-Um-Docker-Container-PostgreSQL)**
  ```bash
  chmod +x connect_docker_postgresql.sh
  ./connect_docker_postgresql.sh
  ```
