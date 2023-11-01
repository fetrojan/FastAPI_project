"""add content column to posts table

Revision ID: ff5c348dbff9
Revises: 1e7894ce1c39
Create Date: 2023-10-31 14:18:41.210642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff5c348dbff9'
down_revision: Union[str, None] = '1e7894ce1c39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
