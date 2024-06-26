"""feat: implement LinkModel fields

Revision ID: 51e3da169529
Revises: 195b5a706d41
Create Date: 2024-04-21 12:46:50.603169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51e3da169529'
down_revision: Union[str, None] = '195b5a706d41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('name', sa.String(), nullable=True))
    op.add_column('links', sa.Column('beneficiary', sa.String(), nullable=True))
    op.add_column('links', sa.Column('description', sa.String(), nullable=True))
    op.create_unique_constraint('uix_1', 'links', ['user_id', 'name', 'beneficiary', 'description'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_1', 'links', type_='unique')
    op.drop_column('links', 'description')
    op.drop_column('links', 'beneficiary')
    op.drop_column('links', 'name')
    # ### end Alembic commands ###
