# No início do seu script ou aplicação
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acesse as variáveis de ambiente normalmente
minha_variavel_secreta = os.getenv("DB_CONNECTION_MYSQL")

print(minha_variavel_secreta)