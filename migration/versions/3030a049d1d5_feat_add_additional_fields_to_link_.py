"""feat: add additional fields to link_clicks

Revision ID: 3030a049d1d5
Revises: 84eb4338b576
Create Date: 2024-04-21 16:37:00.835614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3030a049d1d5'
down_revision: Union[str, None] = '84eb4338b576'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###