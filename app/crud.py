from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas
from typing import List, Optional

def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    """
    Cria um novo item no banco de dados.
    
    Args:
        db: Sessão do banco de dados
        item: Dados do item a ser criado
        
    Returns:
        O item criado com ID
        
    Raises:
        SQLAlchemyError: Em caso de erro no banco de dados
    """
    try:
        db_item = models.Item(**item.model_dump(exclude_unset=True))
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_item(db: Session, item_id: int) -> Optional[models.Item]:
    """
    Obtém um item pelo ID.
    
    Args:
        db: Sessão do banco de dados
        item_id: ID do item
        
    Returns:
        O item encontrado ou None se não existir
    """
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
    """
    Lista itens com paginação.
    
    Args:
        db: Sessão do banco de dados
        skip: Número de itens para pular
        limit: Limite máximo de itens
        
    Returns:
        Lista de itens
    """
    return db.query(models.Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate) -> Optional[models.Item]:
    """
    Atualiza um item existente.
    
    Args:
        db: Sessão do banco de dados
        item_id: ID do item a ser atualizado
        item: Dados de atualização (apenas campos modificados)
        
    Returns:
        O item atualizado ou None se não encontrado
        
    Raises:
        SQLAlchemyError: Em caso de erro no banco de dados
    """
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if not db_item:
            return None
            
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
            
        db.commit()
        db.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_item(db: Session, item_id: int) -> bool:
    """
    Remove um item do banco de dados.
    
    Args:
        db: Sessão do banco de dados
        item_id: ID do item a ser removido
        
    Returns:
        True se removido com sucesso, False se não encontrado
        
    Raises:
        SQLAlchemyError: Em caso de erro no banco de dados
    """
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if not db_item:
            return False
            
        db.delete(db_item)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise e