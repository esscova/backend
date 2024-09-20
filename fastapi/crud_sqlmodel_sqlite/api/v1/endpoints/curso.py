from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_models import CursoModel
from core.deps import get_session

router = APIRouter()

# POST
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso:CursoModel, db:AsyncSession=Depends(get_session)):
    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )
    db.add(novo_curso)
    await db.commit()
    await db.refresh(novo_curso)

    return novo_curso

# GET
@router.get('/', response_model=List[CursoModel], status_code=status.HTTP_200_OK)
async def get_cursos(db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos:List[CursoModel] = result.scalars().all()

        return cursos
    
# GET
@router.get('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_200_OK)
async def get_curso(curso_id:int, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso:CursoModel = result.scalar_one_or_none()

        if not curso:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )
        return curso

# PUT
@router.put('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_202_ACCEPTED)
async def update_curso(curso_id:int, curso:CursoModel, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up:CursoModel = result.scalar_one_or_none()

        if not curso:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        curso_up.titulo = curso.titulo
        curso_up.aulas = curso.aulas
        curso_up.horas = curso.horas

        await session.commit()
        await session.refresh(curso_up)

        return curso_up
    
# DELETE
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id:int, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del:CursoModel = result.scalar_one_or_none()

        if not curso_del:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )

        await session.delete(curso_del)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)