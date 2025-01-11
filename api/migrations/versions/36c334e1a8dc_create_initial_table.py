"""create initial table

Revision ID: 36c334e1a8dc
Revises: 3eeb9c1903da
Create Date: 2025-01-11 03:15:55.339714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36c334e1a8dc'
down_revision: Union[str, None] = '3eeb9c1903da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_threads', sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat_threads', 'deleted_at')
    # ### end Alembic commands ###
