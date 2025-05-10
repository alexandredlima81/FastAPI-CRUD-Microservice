from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    "/items/",
    response_model=schemas.Item,
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo item",
    tags=["Itens"]
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Cria um novo item com todos os detalhes:
    
    - **title**: Título obrigatório (max 100 caracteres)
    - **description**: Descrição opcional
    """
    try:
        return crud.create_item(db=db, item=item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao criar item: {str(e)}"
        )

@app.get(
    "/items/",
    response_model=list[schemas.Item],
    summary="Listar todos os itens",
    tags=["Itens"]
)
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Lista todos os itens com paginação:
    
    - **skip**: Itens para pular (default 0)
    - **limit**: Limite de itens por página (default 100)
    """
    return crud.get_items(db, skip=skip, limit=limit)

@app.get(
    "/items/{item_id}",
    response_model=schemas.Item,
    summary="Obter um item específico",
    tags=["Itens"]
)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Obtém um item específico pelo ID:
    
    - **item_id**: ID do item a ser recuperado
    """
    db_item = crud.get_item(db, item_id=item_id)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    return db_item

@app.put(
    "/items/{item_id}",
    response_model=schemas.Item,
    summary="Atualizar um item",
    tags=["Itens"]
)
def update_item(
    item_id: int,
    item: schemas.ItemUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza um item existente (atualização parcial):
    
    - **item_id**: ID do item a ser atualizado
    - **title**: Novo título (opcional)
    - **description**: Nova descrição (opcional)
    """
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    return db_item

@app.delete(
    "/items/{item_id}",
    response_model=schemas.DeleteResponse,
    status_code=status.HTTP_200_OK,
    summary="Deletar um item",
    tags=["Itens"]
)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Remove um item específico:
    
    - **item_id**: ID do item a ser removido
    """
    success = crud.delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    return schemas.DeleteResponse(id=item_id)