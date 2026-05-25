import sys
import os
from datetime import datetime, timezone, timedelta

# Add the current directory to sys.path so we can import 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import engine, SessionLocal
from app.models.base import Base
from app.models.player import Player
from app.models.group import Group
from app.models.game import Game


def seed():
    print("Iniciando o seeding do banco de dados...")

    # Limpa o banco de dados e recria as tabelas
    print("Limpando dados existentes...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        # Criar Jogadores
        print("Criando jogadores...")
        players = [
            Player(name="Alice Silva", email="alice@example.com", phone="11999999991"),
            Player(name="Bob Oliveira", email="bob@example.com", phone="11999999992"),
            Player(name="Charlie Santos", email="charlie@example.com", phone="11999999993"),
            Player(name="David Lima", email="david@example.com", phone="11999999994"),
            Player(name="Eve Costa", email="eve@example.com", phone="11999999995"),
        ]
        session.add_all(players)

        # Criar Grupos
        print("Criando grupos...")
        groups = [
            Group(
                name="Racha de Final de Semana",
                description="Grupo para os jogos de sábado de manhã.",
            ),
            Group(
                name="Futebol das Quartas",
                description="Jogo fixo no meio da semana.",
            ),
        ]
        session.add_all(groups)

        # Criar Jogos
        print("Criando jogos...")
        now = datetime.now(timezone.utc)
        
        # Jogo passado (último sábado)
        # weekday() is 0 for Monday, 5 for Saturday.
        # To get to last Saturday:
        # If today is Wednesday (2), days to subtract = 2 (Mon) + 2 (Sat) = 4? 
        # Actually: (now.weekday() + 2) % 7 will get us back to Saturday.
        days_to_last_saturday = (now.weekday() - 5) % 7
        if days_to_last_saturday == 0: days_to_last_saturday = 7
        last_saturday = now - timedelta(days=days_to_last_saturday)
        last_saturday = last_saturday.replace(hour=10, minute=0, second=0, microsecond=0)
        
        # Jogo futuro (próximo sábado)
        next_saturday = last_saturday + timedelta(days=7)

        games = [
            Game(
                played_at=last_saturday,
                location="Arena Central",
                notes="Ótimo jogo, todos compareceram.",
            ),
            Game(
                played_at=next_saturday,
                location="Arena Central",
                notes="Confirmar quem vai levar a bola.",
            ),
        ]
        session.add_all(games)

        session.commit()
        print("Banco de dados populado com sucesso!")

    except Exception as e:
        print(f"Erro durante o seeding: {e}")
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed()
