"""feat: implement relationship user -> links

Revision ID: 365ab19bd835
Revises: c5caad8935af
Create Date: 2024-04-21 10:38:20.739621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '365ab19bd835'
down_revision: Union[str, None] = 'c5caad8935af'
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
