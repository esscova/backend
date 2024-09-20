from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.artigo_model import ArtigoModel
from models.usuario_model import UsuarioModel
from schemas.artigo_schema import ArtigoSchema
from core.deps import get_current_user, get_session

router = APIRouter()

# POST
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ArtigoSchema)
async def post_artigo(artigo:ArtigoSchema, usuario_logado:UsuarioModel = Depends(get_current_user), db:AsyncSession=Depends(get_session)):
    novo_artigo:ArtigoModel = ArtigoModel(
        titulo=artigo.titulo,
        descricao=artigo.descricao,
        url_fonte=str(artigo.url_fonte),
        usuario_id = usuario_logado.id
    )
    db.add(novo_artigo)
    await db.commit()

    return novo_artigo

# GET
@router.get('/', response_model=List[ArtigoSchema], status_code=status.HTTP_200_OK)
async def get_artigos(db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel)
        result = await session.execute(query)
        artigos:List[ArtigoModel] = result.scalars().unique().all()

        return artigos
    
# GET especifico
@router.get('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_200_OK)
async def get_artigo(artigo_id:int, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id)
        result = await session.execute(query)
        artigo:ArtigoModel = result.scalars().unique().one_or_none()

        if not artigo:
            raise HTTPException(
                detail=f'Artigo com ({artigo_id}) não encontrado.',
                status_code=status.HTTP_404_NOT_FOUND
            )
        return artigo

# PUT
@router.put('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_artigo(artigo_id:int, artigo:ArtigoSchema, db:AsyncSession=Depends(get_session), usuario_logado:UsuarioModel=Depends(get_current_user)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id, ArtigoModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        artigo_up:ArtigoModel = result.scalars().unique().one_or_none()

        if not artigo_up:
            raise HTTPException(
                detail=f'Artigo com ({artigo_id}) não encontrado.',
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        if artigo.titulo:
            artigo_up.titulo = artigo.titulo
        if artigo.descricao:
            artigo_up.descricao = artigo.descricao
        if artigo.url_fonte:
            artigo_up.url_font = artigo.url_fonte
        
        await session.commit()
        await session.refresh(artigo_up)

        return artigo_up
    
# DELETE
@router.delete('/{artigo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def put_artigo(artigo_id:int, db:AsyncSession=Depends(get_session), usuario_logado:UsuarioModel=Depends(get_current_user)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id, ArtigoModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        artigo_del:ArtigoModel = result.scalars().unique().one_or_none()

        if not artigo_del:
            raise HTTPException(
                detail=f'Artigo com ({artigo_id}) não encontrado.',
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        await session.delete(artigo_del)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)